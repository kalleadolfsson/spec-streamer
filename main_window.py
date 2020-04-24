"""
by K. Adolfsson
(Video feed using QtDesigner OpenCV is based on tutorial by Berrouba.A)
"""



# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import subprocess

#import numpy and math for easy data handling
import numpy as np
import math

# import matplot library
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt

# import Opencv module
import cv2

from ui_main_window import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # spectrum variables
        self.start = 840
        self.stop = 1085
        self.bins = self.stop-self.start
        self.line = 606
        self.rotation = 88
        self.averages = 10
        self.waves = np.arange(400,650,250/self.bins)
        self.cntr = 0
        self.intensities = np.zeros(self.bins)

        self.intensitiesDark = np.zeros(self.bins)
        self.intensitiesReference = np.zeros(self.bins)
        self.intensitiesSample = np.zeros(self.bins)
        self.intensitiesTransmission = np.zeros(self.bins)

        self.acquireDark = False
        self.acquireReference = False
        self.acquireSample = False


        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        # set averages
        self.ui.set_averages_button.clicked.connect(self.setAverages)
        # if button for "acquire dark spectrum" has been pressed
        self.ui.dark_button.clicked.connect(self.acquireDarkSpectrum)
        # if button for "acquire reference spectrum" has been pressed
        self.ui.reference_button.clicked.connect(self.acquireReferenceSpectrum)
        # if button for "acquire sample spectrum" has been pressed
        self.ui.sample_button.clicked.connect(self.acquireSampleSpectrum)

    # view camera
    def viewCam(self):

        # read image in BGR format
        ret, image = self.cap.read()

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape


        num_rows, num_cols = image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), self.rotation, 1)
        image = cv2.warpAffine(image, rotation_matrix, (num_cols, num_rows))


        # extract spectral data
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        self.intensities = self.intensities + gray[self.line][self.start:self.stop]

        # if the number of averages has been met, proceed to calculate averaged spectrum and plot
        if (self.cntr == self.averages - 1):
            self.intensities = self.intensities/self.averages
            self.intensities = np.flip(self.intensities)

        # check if any special acqusition has been selected (i.e. dark, ref or sample)
            if (self.acquireDark):
                self.intensitiesDark = self.intensities
                self.acquireDark = False
                self.setCheckBox(0)

            elif (self.acquireReference):
                self.intensitiesReference = self.intensities
                self.acquireReference = False
                self.setCheckBox(1)

            elif (self.acquireSample):
                self.intensitiesSample = self.intensities
                self.acquireSample = False
                self.setCheckBox(2)

            if (sum(self.intensitiesDark)>0 and sum(self.intensitiesReference)>0 and sum(self.intensitiesSample)>0):
                self.updateCalcPlot()

            self.cntr = 0
            self.updatePlot()

        self.cntr = self.cntr + 1

        # highlight the data-line
        image[self.line][self.start:self.stop][:] = 255

        height, width, channel = image.shape


        scale_percent = 40 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

        step = channel * width
        # create QImage from image
        qImg = QImage(resized.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    def setAverages(self):
        self.averages = int(self.ui.averages_input.text())
        self.intensities = np.zeros(self.bins)
        self.cntr = 0

    def acquireDarkSpectrum(self):
        self.acquireDark = True
        self.cntr = 0

    def acquireReferenceSpectrum(self):
        self.acquireReference = True
        self.cntr = 0

    def acquireSampleSpectrum(self):
        self.acquireSample = True
        self.cntr = 0

    # checks relevant checkbox to show user that a spectrum has been stored
    def setCheckBox(self, specCheck):
        if(specCheck == 0):
            self.ui.dark_ok.setChecked(True)
        elif(specCheck == 1):
            self.ui.reference_ok.setChecked(True)
        elif(specCheck == 2):
            self.ui.sample_ok.setChecked(True)

    # update "raw" spectrum plot
    def updatePlot(self):

        #   --------PLOT SPECTRUM --------
        self.ui.spec_plot.fig.clear()
        self.ui.spec_plot.fig.plot(self.waves,self.intensities,c='k', lw=2)
        self.ui.spec_plot.fig.set_xlabel('Wavelength(nm)')
        self.ui.spec_plot.fig.set_ylabel('Intensity')
        self.ui.spec_plot.fig.set_title('Spectrum')
        self.ui.spec_plot.fig.set_xlim(450,650)
        self.ui.spec_plot.fig.set_ylim(0, 255)
        self.ui.spec_plot.fig.grid(True)
        self.ui.spec_plot.draw()
        self.ui.spec_plot.update()
        self.ui.spec_plot.repaint()

    # update transmission spectrum plot
    def updateCalcPlot(self):
        self.intensitiesTransmission = (self.intensitiesSample-self.intensitiesDark)/(self.intensitiesReference-self.intensitiesDark)

        #   --------PLOT CALCULATED TRANSMISSION SPECTRUM --------
        self.ui.calc_plot.fig.clear()
        self.ui.calc_plot.fig.plot(self.waves,self.intensitiesTransmission,c='k', lw=2)
        self.ui.calc_plot.fig.set_xlabel('Wavelength(nm)')
        self.ui.calc_plot.fig.set_ylabel('Intensity')
        self.ui.calc_plot.fig.set_title('Transmission spectrum')
        self.ui.calc_plot.fig.set_xlim(450,650)
        self.ui.calc_plot.fig.set_ylim(0, 1.2) #max(self.intensitiesTransmission))
        self.ui.calc_plot.fig.grid(True)
        self.ui.calc_plot.draw()
        self.ui.calc_plot.update()
        self.ui.calc_plot.repaint()

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(1)

            # set width and height
            self.cap.set(3,1920)
            self.cap.set(4,1080)

            # start timer
            self.timer.start(30)

            self.cap.set(cv2.CAP_PROP_EXPOSURE,-10)

            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
