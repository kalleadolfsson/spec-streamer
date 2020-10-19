"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

import os
import re
import subprocess

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
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


        # Read acquisition settings from spectrometer conf file if available
        self.read_from_file = False
        #self.apply_acquisition_settings(load_config_file = True, config_path = 'conf/Laptop_teaching.conf')

        self.setup_signals()
        self.apply_acquisition_settings()



    def setup_signals(self):

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)

        # VIP
        self.ui.junkyard_photonics_label.setText("by junkyard-photonics")

        # ACQUISITION CONTROLS
        # set live_button callback clicked  function
        self.ui.live_button.clicked.connect(self.controlTimer)
        # set apply_acquisition_settings_button callback clicked  function
        self.ui.apply_acquisition_settings_button.clicked.connect(self.apply_acquisition_settings)
        # set load_acquisition_settings_button callback clicked function
        self.ui.load_acquisition_settings_button.clicked.connect(self.load_acquisition_settings)
        # set load_acquisition_settings_button callback clicked function
        self.ui.save_acquisition_settings_button.clicked.connect(self.save_acquisition_settings)


        # Toggle tab container (main menu)
        self.ui.acquisition_button.clicked.connect(lambda: self.main_menu_switch(choice = 'acquisition'))
        self.ui.calibration_button.clicked.connect(lambda: self.main_menu_switch(choice = 'calibration'))
        self.ui.experiment_button.clicked.connect(lambda: self.main_menu_switch(choice = 'experiment'))

        # Let Enter-key trigger callback on all QLineEdit objects
        self.ui.detector_integration_time_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.detector_averages_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.detector_gain_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.detector_width_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.detector_height_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_rotation_global_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_rotation_spectrum_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_start_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_stop_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_line_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_lines_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.image_scale_overview_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.image_scale_cropped_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.image_camera_no_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.spectrum_start_input.returnPressed.connect(self.apply_acquisition_settings)
        self.ui.image_crop_box.clicked.connect(self.apply_acquisition_settings)

        # TRANSMISSION SPECTRUM CONTROLS
        # if button for "acquire dark spectrum" has been pressed
        self.ui.dark_button.clicked.connect(self.acquireDarkSpectrum)
        # if button for "acquire reference spectrum" has been pressed
        self.ui.reference_button.clicked.connect(self.acquireReferenceSpectrum)
        # if button for "acquire sample spectrum" has been pressed
        self.ui.sample_button.clicked.connect(self.acquireSampleSpectrum)

    def main_menu_switch(self, choice = 'acquisition'):

        if(choice == 'acquisition'):
            self.ui.tab_container.setCurrentIndex(0)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
        elif(choice == 'calibration'):
            self.ui.tab_container.setCurrentIndex(1)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
        elif(choice == 'experiment'):
            self.ui.tab_container.setCurrentIndex(2)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")



    def load_acquisition_settings(self):
        # Open dialog for loading acquisition settings
        config_file_path = QFileDialog.getOpenFileName(self, "Load settings", "conf", "Config Files (*.conf)")
        self.load_config_file_path = config_file_path[0]
        self.load_config_file_name = os.path.split(self.load_config_file_path)[-1]

        # Setup configparser for reading from config file
        config = configparser.ConfigParser()
        config.read(self.load_config_file_path)

        # set spectrum variables from config file
        self.spectrometer_name = config['SpectrometerConfig']['spectrometer_name']

        # Detector
        self.integration_time = config['SpectrometerConfig'].getint('integration_time')
        self.averages = config['SpectrometerConfig'].getint('averages')
        self.gain = config['SpectrometerConfig'].getint('gain')
        self.width = config['SpectrometerConfig'].getint('width')
        self.height = config['SpectrometerConfig'].getint('height')

        # Spectrum config
        self.rotation_global = config['SpectrometerConfig'].getfloat('rotation_global')
        self.rotation_spectrum = config['SpectrometerConfig'].getfloat('rotation_spectrum')
        self.start = config['SpectrometerConfig'].getint('start')
        self.stop = config['SpectrometerConfig'].getint('stop')
        self.central_line = config['SpectrometerConfig'].getint('central_line')
        self.no_of_lines = config['SpectrometerConfig'].getint('no_of_lines')

        # Image
        self.scale_overview = config['SpectrometerConfig'].getint('scale_overview')
        self.scale_cropped = config['SpectrometerConfig'].getint('scale_cropped')
        self.crop = config['SpectrometerConfig'].getboolean('crop')
        if(self.crop):
            self.scale = self.scale_cropped
        else:
            self.scale = self.scale_overview
        self.cam_no = config['SpectrometerConfig'].getint('cam_no')

        # Update variables in acquisition settings form
        self.update_text_in_acquisition_input_form()


    def save_acquisition_settings(self):
        # Open dialog for saving acquisition settings

        config_file_path = QFileDialog.getSaveFileName(self, "Save settings", "conf", "Config Files (*.conf)")
        self.save_config_file_path = config_file_path[0]

        # Setup configparser for writing to config file
        config = configparser.ConfigParser()
        config['SpectrometerConfig'] = {'spectrometer_name': self.spectrometer_name,
                                        'integration_time' : self.integration_time,
                                        'averages' : self.averages,
                                        'gain' : self.gain,
                                        'width' : self.width,
                                        'height' : self.height,
                                        'rotation_global' : self.rotation_global,
                                        'rotation_spectrum' : self.rotation_spectrum,
                                        'central_line' : self.central_line,
                                        'no_of_lines' : self.no_of_lines,
                                        'start' : self.start,
                                        'stop' : self.stop,
                                        'scale_overview' : self.scale_overview,
                                        'scale_cropped' : self.scale_cropped,
                                        'crop' : self.crop,
                                        'cam_no' : self.cam_no}

        try:
            with open(self.save_config_file_path, 'w') as configfile:
                config.write(configfile)
            print('Successfully saved settings')
        except:
            print('Error saving to config file')


    def apply_acquisition_settings(self, load_config_file = False, config_path = ''):

        # set spectrum variables from acquisition settings form
        self.read_acquisition_input_form()

        # Additional acquisition settings
        self.bins = self.stop-self.start

        # Needs to be defined in a more dynamic way
        self.waves = np.arange(300,700,400/self.bins)

        self.cntr = 0
        self.intensities = np.zeros(self.bins)


        # Transmission spectrum settings
        self.intensitiesDark = np.zeros(self.bins)
        self.intensitiesReference = np.zeros(self.bins)
        self.intensitiesSample = np.zeros(self.bins)
        self.intensitiesTransmission = np.zeros(self.bins)

        self.acquireDark = False
        self.acquireReference = False
        self.acquireSample = False

    def read_acquisition_input_form(self):
        # Read current values from acqusition settings form

        self.spectrometer_name = self.ui.spectrometer_name_input.text()

        # Detector
        self.integration_time = int(re.sub("\D","",self.ui.detector_integration_time_input.text()))
        self.averages = int(re.sub("\D","",self.ui.detector_averages_input.text()))
        self.gain = int(re.sub("\D","",self.ui.detector_gain_input.text()))
        self.width = int(re.sub("\D","",self.ui.detector_width_input.text()))
        self.height = int(re.sub("\D","",self.ui.detector_height_input.text()))

        # Spectrum config
        self.rotation_global = float(re.sub("\D","",self.ui.spectrum_rotation_global_input.text()))
        self.rotation_spectrum = float(re.sub("\D","",self.ui.spectrum_rotation_spectrum_input.text()))
        self.start = int(re.sub("\D","",self.ui.spectrum_start_input.text()))
        self.stop = int(re.sub("\D","",self.ui.spectrum_stop_input.text()))
        self.central_line = int(re.sub("\D","",self.ui.spectrum_line_input.text()))
        self.no_of_lines = int(re.sub("\D","",self.ui.spectrum_lines_input.text()))

        # Image
        self.scale_overview = int(re.sub("\D","",self.ui.image_scale_overview_input.text()))
        self.scale_cropped = int(re.sub("\D","",self.ui.image_scale_cropped_input.text()))
        self.crop = bool(self.ui.image_crop_box.isChecked())
        if(self.crop):
            self.scale = self.scale_cropped
        else:
            self.scale = self.scale_overview
        self.cam_no = int(re.sub("\D","",self.ui.image_camera_no_input.text()))

    def update_text_in_acquisition_input_form(self):
        self.ui.spectrometer_name_input.setText(self.spectrometer_name)

        # Detector
        self.ui.detector_integration_time_input.setText(str(self.integration_time))
        self.ui.detector_averages_input.setText(str(self.averages))
        self.ui.detector_gain_input.setText(str(self.gain))
        self.ui.detector_width_input.setText(str(self.width))
        self.ui.detector_height_input.setText(str(self.height))

        # Spectrum config
        self.ui.spectrum_rotation_global_input.setText(str(self.rotation_global))
        self.ui.spectrum_rotation_spectrum_input.setText(str(self.rotation_spectrum))
        self.ui.spectrum_start_input.setText(str(self.start))
        self.ui.spectrum_stop_input.setText(str(self.stop))
        self.ui.spectrum_line_input.setText(str(self.central_line))
        self.ui.spectrum_lines_input.setText(str(self.no_of_lines))

        # Image
        self.ui.image_scale_overview_input.setText(str(self.scale_overview))
        self.ui.image_scale_cropped_input.setText(str(self.scale_cropped))

        if(self.crop):
            self.ui.image_crop_box.setChecked(True)
        else:
            self.ui.image_crop_box.setChecked(False)
        self.ui.image_camera_no_input.setText(str(self.cam_no))



    # view camera
    def viewCam(self):

        # read image in BGR format
        ret, image = self.cap.read()

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Global rotation (center image is center of rotation)
        M = cv2.getRotationMatrix2D((round((self.width)/2),round((self.height)/2)) , self.rotation_global, 1.0)
        (h, w) = image.shape[:2]
        image = cv2.warpAffine(image, M, (w, h))

        # Spectrum rotation (center of rotation is center of spectrum)
        M = cv2.getRotationMatrix2D((round((self.start+self.stop)/2),self.central_line) , self.rotation_spectrum, 1.0)
        (h, w) = image.shape[:2]
        image = cv2.warpAffine(image, M, (w, h))

        # extract spectral data
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        line_range = round(self.no_of_lines/2)
        for n in range(-line_range,line_range):
            self.intensities = self.intensities + gray[self.central_line+int(n)][self.start:self.stop]

        # if the number of averages has been met, proceed to calculate averaged spectrum and plot
        if (self.cntr == self.averages - 1):
            self.intensities = self.intensities/self.averages

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

    # Transmission spectra
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
        self.ui.spec_plot.fig.patch.set_alpha(0.)
        self.ui.spec_plot.fig.plot(self.waves,self.intensities,c='k', lw=2)
        self.ui.spec_plot.fig.set_xlabel('Wavelength(nm)')
        self.ui.spec_plot.fig.set_ylabel('Intensity')
        self.ui.spec_plot.fig.set_title('Spectrum')
        self.ui.spec_plot.fig.set_xlim(300,700)
        self.ui.spec_plot.fig.set_ylim(0, 255*01.3*self.no_of_lines)
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
            self.cap = cv2.VideoCapture(self.cam_no)

            # The following commands does not seems to work on all platforms (although I haven't found alternatives)
            # (worked for me on Windows systems, not on Mac OS)
            self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)      # 0.75 -> Auto exposure, 0.25 -> Manual exposure
            self.cap.set(cv2.CAP_PROP_EXPOSURE,-1)
            self.cap.set(cv2.CAP_PROP_GAIN, 1)

            # set width and height
            self.cap.set(3,self.width)
            self.cap.set(4,self.height)

            # start timer
            self.timer.start(5)
            # update live_button text
            self.ui.live_button.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update live_button text
            self.ui.live_button.setText("Live")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
