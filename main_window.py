"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

import os

import re

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

#import configparser to read from conf file
import configparser

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


        # Read acquisition params from spectrometer conf file if available
        self.read_from_file = True
        self.set_params('conf/Laptop_teaching.conf')

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

    def set_params(self, config_path = ''):

        if(self.read_from_file):
            path_ = re.split('\/',config_path)
            config_path = os.path.join( path_[0], path_[1])

            config = configparser.ConfigParser()
            # change this to param set from terminal or from file selected in UI
            config.read(config_path)

            # set spectrum variables from config file
            self.detector = config['SpectrometerConfig']['detector']
            self.width = config['SpectrometerConfig'].getint('width')
            self.height = config['SpectrometerConfig'].getint('height')
            self.flip90 = config['SpectrometerConfig'].getboolean('flip90')
            self.flip180 = config['SpectrometerConfig'].getboolean('flip180')
            self.reverse_order = config['SpectrometerConfig'].getboolean('reverse_order')
            self.fine_tilt = config['SpectrometerConfig'].getfloat('fine_tilt')
            self.central_line = config['SpectrometerConfig'].getint('central_line')
            self.no_of_lines = config['SpectrometerConfig'].getint('no_of_lines')
            self.start = config['SpectrometerConfig'].getint('start')
            self.stop = config['SpectrometerConfig'].getint('stop')
            self.averages = config['SpectrometerConfig'].getint('averages')
            self.scale = config['SpectrometerConfig'].getfloat('scale')
            self.crop = config['SpectrometerConfig'].getboolean('crop')
        else:
            # set spectrum variables manually
            self.detector = '-'
            self.width = 1280
            self.height = 1024
            self.flip90 = False
            self.flip180 = False
            self.reverse_order = False
            self.fine_tilt = 0
            self.central_line = 585
            self.no_of_lines =5
            self.start = 490
            self.stop = 860
            self.averages = 2
            self.scale = 40
            self.crop = False

        # Additional acquisition params
        self.bins = self.stop-self.start

        # Needs to be defined in a more dynamic way
        self.waves = np.arange(300,700,400/self.bins)

        self.cntr = 0
        self.intensities = np.zeros(self.bins)

        self.intensitiesDark = np.zeros(self.bins)
        self.intensitiesReference = np.zeros(self.bins)
        self.intensitiesSample = np.zeros(self.bins)
        self.intensitiesTransmission = np.zeros(self.bins)

        self.acquireDark = False
        self.acquireReference = False
        self.acquireSample = False


    # view camera
    def viewCam(self):

        # read image in BGR format
        ret, image = self.cap.read()

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # If projection is primarily vertical
        if(self.flip90):
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

        if(self.flip180):
            image = cv2.rotate(image, cv2.ROTATE_180)


        # Fine tune tilt angle compensation
        M = cv2.getRotationMatrix2D((round((self.start+self.stop)/2),self.central_line) , self.fine_tilt, 1.0)
        (h, w) = image.shape[:2]
        image = cv2.warpAffine(image, M, (w, h))
        print(image.shape)
        # extract spectral data
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        line_range = round(self.no_of_lines/2)
        for n in range(-line_range,line_range):
            self.intensities = self.intensities + gray[self.central_line+int(n)][self.start:self.stop]

        # if the number of averages has been met, proceed to calculate averaged spectrum and plot
        if (self.cntr == self.averages - 1):
            self.intensities = self.intensities/self.averages
            if(self.reverse_order):
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
        image[self.central_line-round(self.no_of_lines/2)][self.start:self.stop][:] = 255
        image[self.central_line+round(self.no_of_lines/2)][self.start:self.stop][:] = 255


        height, width, channel = image.shape


        # Crop image
        if(self.crop):
            image = image[self.central_line-round(self.no_of_lines/2)-30:self.central_line+round(self.no_of_lines/2)+30, self.start-5:self.stop+5]

        # resize image
        width = int(image.shape[1] * self.scale / 100)
        height = int(image.shape[0] * self.scale / 100)
        dim = (width, height)
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
        self.ui.spec_plot.fig.set_xlim(300,700)
        self.ui.spec_plot.fig.set_ylim(0, 255*0.3*self.no_of_lines)
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
        self.ui.calc_plot.fig.set_xlim(300,700)
        self.ui.calc_plot.fig.set_ylim(0, max(self.intensitiesTransmission))
        self.ui.calc_plot.fig.grid(True)
        self.ui.calc_plot.draw()
        self.ui.calc_plot.update()
        self.ui.calc_plot.repaint()

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
            #self.cap.set(cv2.CAP_PROP_EXPOSURE,-1)
            #self.cap.set(cv2.CAP_PROP_GAIN, 1)


            # set width and height
            self.cap.set(3,1280)
            self.cap.set(4,1024)

            # start timer
            self.timer.start(20)
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
