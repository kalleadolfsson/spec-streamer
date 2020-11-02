import os
import re
import subprocess
import time

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, QObject, QEventLoop, pyqtSignal, pyqtSlot

#import configparser to read from conf file
import configparser

#import numpy and math for easy data handling
import numpy as np
import math


# import Opencv module
import cv2




class Spectrometer(QThread):
    raw_spectrum_stream = pyqtSignal(np.ndarray)

    dark_spectrum_stream = pyqtSignal(np.ndarray)
    emission_spectrum_stream =  pyqtSignal(np.ndarray)
    reference_spectrum_stream =  pyqtSignal(np.ndarray)
    transmission_spectrum_stream = pyqtSignal(np.ndarray)

    image_stream = pyqtSignal(QPixmap)

    stream_open = False
    stream = False
    #def __init__(self, parent = None):
    #    QThread.__init__(self, parent)

    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        # Create Timer
        #self.imageTimer = QTimer()
        #self.imageTimer.moveToThread(self)
        # set imageTimer timeout callback function
        #self.imageTimer.timeout.connect(self.viewCam)

    def run(self):
        self.setup()
        self.cap = cv2.VideoCapture(self.cam_no)
        # The following commands does not seems to work on all platforms (although I haven't found alternatives)
        # (worked for me on Windows systems, not on Mac OS)
        self.set_video_capture_settings()

        while(True):
            self.viewCam()
            time.sleep(0.025)


    def stop(self):
        if(self.stream_open):
            # release video capture
            self.cap.release()


    def viewCam(self):
        if(self.stream):
            self.stream_open = True
            # read image in BGR format
            ret, image = self.cap.read()

            # convert image to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            if(self.rotation_global!= 0):
                # Global rotation (center image is center of rotation)
                M = cv2.getRotationMatrix2D((round((self.width)/2),round((self.height)/2)) , self.rotation_global, 1.0)
                (h, w) = image.shape[:2]
                image = cv2.warpAffine(image, M, (w, h))

            if(self.rotation_spectrum!= 0):
                # Spectrum rotation (center of rotation is center of spectrum)
                M = cv2.getRotationMatrix2D((round((self.start_x+self.stop_x)/2),self.central_line) , self.rotation_spectrum, 1.0)
                (h, w) = image.shape[:2]
                image = cv2.warpAffine(image, M, (w, h))

            # extract spectral data
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            line_range = round(self.no_of_lines/2)
            for n in range(-line_range,line_range):
                self.intensities = self.intensities + gray[self.central_line+int(n)][self.start_x:self.stop_x]

            # if the number of averages has been met, proceed to calculate averaged spectrum and plot
            if (self.cntr == self.averages - 1):
                self.intensities = self.intensities/self.averages

                # check if any special acqusition has been selected (i.e. dark, emission, reference or transmission)
                if (self.acquireDark):
                    self.intensitiesDark = self.intensities
                    self.acquireDark = False
                    self.dark_spectrum_stream.emit(self.intensitiesDark)

                elif (self.acquireEmission):
                    self.intensitiesEmission = self.intensities-self.intensitiesDark
                    self.acquireEmission = False
                    self.emission_spectrum_stream.emit(self.intensitiesEmission)


                elif (self.acquireReference):
                    self.intensitiesReference = self.intensities
                    self.acquireReference = False
                    self.reference_spectrum_stream.emit(self.intensitiesReference)


                elif (self.acquireTransmission):
                    temp_intensities = self.intensities-self.intensitiesDark
                    # Handle division by 0 by replacing output elements with 0
                    self.intensitiesTransmission = np.divide(temp_intensities, self.intensitiesReference-self.intensitiesDark, out=np.zeros_like(temp_intensities), where=self.intensitiesReference!=0)
                    self.acquireTransmission = False
                    self.transmission_spectrum_stream.emit(self.intensitiesTransmission)

                #if (sum(self.intensitiesDark)>0 and sum(self.intensitiesReference)>0 and sum(self.intensitiesTransmission)>0):
                #    self.updateCalcPlot()

                self.cntr = 0
                self.raw_spectrum_stream.emit(self.intensities)


            self.cntr = self.cntr + 1

            # highlight the data-line
            image[self.central_line-round(self.no_of_lines/2)][self.start_x:self.stop_x][:] = 255
            image[self.central_line+round(self.no_of_lines/2)][self.start_x:self.stop_x][:] = 255


            height, width, channel = image.shape


            # Crop image
            if(self.crop):
                image = image[self.central_line-round(self.no_of_lines/2)-30:self.central_line+round(self.no_of_lines/2)+30, self.start_x-5:self.stop_x+5]
                self.scale = self.scale_cropped
            else:
                self.scale = self.scale_overview

            # resize image
            width = int(image.shape[1] * self.scale / 100)
            height = int(image.shape[0] * self.scale / 100)
            dim = (width, height)
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

            step = channel * width

            # create QImage from image
            qImg = QImage(resized.data, width, height, step, QImage.Format_RGB888)

            # Send QImage as signal
            self.image_stream.emit(QPixmap.fromImage(qImg))

    def setup(self):
        # Additional acquisition settings
        self.bins = self.stop_x-self.start_x

        # Needs to be defined in a more dynamic way
        self.waves = np.arange(self.start_x,self.stop_x,1)

        self.cntr = 0
        self.intensities = np.zeros(self.bins)

        # Transmission spectrum settings
        self.intensitiesDark = np.zeros(self.bins)
        self.intensitiesEmission = np.zeros(self.bins)
        self.intensitiesReference = np.zeros(self.bins)
        self.intensitiesTransmission = np.zeros(self.bins)

        self.acquireDark = False
        self.acquireEmission = False
        self.acquireReference = False
        self.acquireTransmission = False

    def set_video_capture_settings(self):
        # The following commands does not seems to work on all platforms (although I haven't found alternatives)
        # (worked for me on Windows systems, not on Mac OS)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)      # 0.75 -> Auto exposure, 0.25 -> Manual exposure
        self.cap.set(cv2.CAP_PROP_EXPOSURE,-1)
        self.cap.set(cv2.CAP_PROP_GAIN, 1)

        # set width and height
        self.cap.set(3,self.width)
        self.cap.set(4,self.height)



    @pyqtSlot()
    def terminate(self):
        self.stop()


    @pyqtSlot()
    def pause(self):
        self.stream = False

    @pyqtSlot()
    def unpause(self):
        self.stream = True

    @pyqtSlot()
    def apply(self):
        self.setup()
        print('updated')
    # Set acquisition properties
    @pyqtSlot(int)
    def set_integration_time(self, integration_time = 20):
        self.integration_time = integration_time

    @pyqtSlot(int)
    def set_averages(self, averages = 5):
        self.averages = averages

    @pyqtSlot(int)
    def set_gain(self, gain = 20):
        self.gain = gain

    @pyqtSlot(int)
    def set_width(self, width = 1280):
        self.width = width

    @pyqtSlot(int)
    def set_height(self, height = 1024):
        self.height = height

    @pyqtSlot(int)
    def set_rotation_global(self, rotation_global = 180):
        self.rotation_global = rotation_global

    @pyqtSlot(int)
    def set_rotation_spectrum(self, rotation_spectrum = 177):
        self.rotation_spectrum = rotation_spectrum

    @pyqtSlot(int)
    def set_central_line(self, central_line = 500):
        self.central_line = central_line

    @pyqtSlot(int)
    def set_no_of_lines(self, no_of_lines = 5):
        self.no_of_lines = no_of_lines

    @pyqtSlot(int)
    def set_start_x(self, start_x = 750):
        self.start_x = start_x

    @pyqtSlot(int)
    def set_stop_x(self, stop_x = 1230):
        self.stop_x = stop_x

    @pyqtSlot(int)
    def set_scale_overview(self, scale_overview = 50):
        self.scale_overview = scale_overview

    @pyqtSlot(int)
    def set_scale_cropped(self, scale_cropped = 150):
        self.scale_cropped = scale_cropped

    @pyqtSlot(int)
    def set_crop(self, crop = True):
        self.crop = crop

    @pyqtSlot(int)
    def set_cam_no(self, cam_no = 0):
        self.cam_no = cam_no


    # Set acqusition mode
    @pyqtSlot()
    def acquireDarkSpectrum(self):
        self.acquireDark = True
        self.cntr = 0

    @pyqtSlot()
    def acquireEmissionSpectrum(self):
        self.acquireEmission = True
        self.cntr = 0

    @pyqtSlot()
    def acquireReferenceSpectrum(self):
        self.acquireReference = True
        self.cntr = 0

    @pyqtSlot()
    def acquireTransmissionSpectrum(self):
        self.acquireTransmission = True
        self.cntr = 0
