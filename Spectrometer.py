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
import qimage2ndarray
#import configparser to read from conf file
import configparser

#import numpy and math for easy data handling
import numpy as np
import math
import imutils

# import Opencv module
import cv2




class Spectrometer(QThread):
    raw_spectrum_stream = pyqtSignal(np.ndarray)

    dark_spectrum_stream = pyqtSignal(np.ndarray)
    emission_spectrum_stream =  pyqtSignal(np.ndarray)
    reference_spectrum_stream =  pyqtSignal(np.ndarray)
    transmission_spectrum_stream = pyqtSignal(np.ndarray)

    image_overview_stream = pyqtSignal(np.ndarray)
    image_cropped_stream = pyqtSignal(np.ndarray)
    downsampling = 0.5            #  % of original

    stream_open = False
    stream = False
    spectral_sensitivity_calibrated = False


    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)


    def run(self):
        self.setup()
        self.cap = cv2.VideoCapture(0)
        self.set_video_capture_settings()

        while(True):
            self.viewCam()
            time.sleep(0.05)


    def stop(self):
        if(self.stream_open):
            # release video capture
            self.cap.release()


    def viewCam(self):
        if(self.stream):
            self.stream_open = True
            # read image in BGR format
            ret, image = self.cap.read()

            empty_image = True
            attempts = 0
            while(empty_image):
                try:
                    # convert image to RGB format
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    empty_image = False
                except:
                    attempts = attempts + 1
                    print(str(attempts) + " attempts")
                if(attempts > 20):
                    print("Video connection failed")
                    self.cap.release()
                    self.run()
                    break

            if(self.rotation_global!= 0):
                # Global rotation (center image is center of rotation)
                image = imutils.rotate(image, self.rotation_global)

            if(self.rotation_spectrum!= 0):
                # Spectrum rotation (center of rotation is center of spectrum)
                M = cv2.getRotationMatrix2D((round((self.start_x+self.stop_x)/2),self.central_line) , self.rotation_spectrum, 1.0)
                (h, w) = image.shape[:2]
                image = cv2.warpAffine(image, M, (w, h))

            # extract spectral data
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            line_range = round(self.no_of_lines/2)
            for n in range(-line_range,line_range):
                self.intensities = self.intensities + np.flip(gray[self.central_line+int(n)][self.width-self.stop_x:self.width-self.start_x])

            # if the number of averages has been met, proceed to calculate averaged spectrum and plot
            if (self.cntr == self.averages - 1):
                self.intensities = self.intensities/self.averages

                # check if any special acqusition has been selected (i.e. dark, emission, reference or transmission)
                if (self.acquireDark):
                    #self.intensitiesDark = self.intensities
                    self.intensitiesDark = self.intensities
                    self.acquireDark = False
                    self.dark_spectrum_stream.emit(self.intensitiesDark)

                elif (self.acquireEmission):
                    #self.intensitiesEmission = self.intensities-self.intensitiesDark
                    intensities_temp = self.intensities-self.intensitiesDark
                    self.intensitiesDark = np.divide(intensities_temp, self.spectral_sensitivity, out=np.zeros_like(intensities_temp), where=self.spectral_sensitivity!=0)

                    self.acquireEmission = False
                    self.emission_spectrum_stream.emit(self.intensitiesEmission)


                elif (self.acquireReference):
                    #self.intensitiesReference = self.intensities
                    temp_intensities = self.intensities-self.intensitiesDark
                    self.intensitiesReference = np.divide(temp_intensities, self.spectral_sensitivity, out=np.zeros_like(self.intensities), where=self.spectral_sensitivity!=0)

                    self.acquireReference = False
                    self.reference_spectrum_stream.emit(self.intensitiesReference)


                elif (self.acquireTransmission):
                    temp_intensities = self.intensities-self.intensitiesDark
                    # Handle division by 0 by replacing output elements with 0
                    temp_intensities_corrected = np.divide(temp_intensities, self.spectral_sensitivity, out=np.zeros_like(temp_intensities), where=self.spectral_sensitivity!=0)
                    self.intensitiesTransmission= np.divide(temp_intensities_corrected, self.intensitiesReference, out=np.zeros_like(temp_intensities_corrected), where=self.intensitiesReference!=0)

                    self.acquireTransmission = False
                    self.transmission_spectrum_stream.emit(self.intensitiesTransmission)

                #if (sum(self.intensitiesDark)>0 and sum(self.intensitiesReference)>0 and sum(self.intensitiesTransmission)>0):
                #    self.updateCalcPlot()

                self.cntr = 0
                self.raw_spectrum_stream.emit((self.intensities-self.intensitiesDark)/self.spectral_sensitivity)


            self.cntr = self.cntr + 1


            # highlight the data-line
            for i in range(0,2):
                image[self.central_line-round(self.no_of_lines/2)-2+i][self.width-self.stop_x:self.width-self.start_x][:] = 255
                image[self.central_line+round(self.no_of_lines/2)-2+i][self.width-self.stop_x:self.width-self.start_x][:] = 255

            # overview image
            image_overview = image
            # Downsample to reduce data flow (does not affect spectral resolution)
            image_overview_downsampled = self.downsample_image(image_overview)

            # Crop image
            image_cropped = image[self.central_line-round(self.no_of_lines/2)-30:self.central_line+round(self.no_of_lines/2)+30, self.width-self.stop_x+5:self.width-self.start_x-5]


            # Send numpy array as signal
            self.image_overview_stream.emit(image_overview_downsampled)
            # Send numpy array as signal
            self.image_cropped_stream.emit(image_cropped)

    def downsample_image(self, image):
        width = int(image.shape[1] * self.downsampling)
        height = int(image.shape[0] * self.downsampling)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

        return resized_image

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

        if(self.spectral_sensitivity_calibrated == False):
            self.spectral_sensitivity = np.ones(self.bins)

        self.acquireDark = False
        self.acquireEmission = False
        self.acquireReference = False
        self.acquireTransmission = False

    def set_video_capture_settings(self):
        # The following commands does not seems to work on all platforms (although I haven't found alternatives)
        # (worked for me on Windows systems, not on Mac OS)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)      # 0.75 -> Auto exposure, 0.25 -> Manual exposure

        #self.cap.set(cv2.CAP_PROP_EXPOSURE,-1)
        #sself.cap.set(cv2.CAP_PROP_GAIN, 0)

        self.cap.set(cv2.CAP_PROP_EXPOSURE,-1)
        self.cap.set(cv2.CAP_PROP_GAIN, 1)

        # set width and height
        self.cap.set(3,self.width)
        self.cap.set(4,self.height)
        print('set Video')

    @pyqtSlot()
    def terminate(self):
        self.stop()

    @pyqtSlot()
    def pause(self):
        self.stream = False

    @pyqtSlot()
    def unpause(self):
        if(self.stream_open):
            self.set_video_capture_settings()
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
    def set_crop(self, crop = True):
        self.crop = crop

    @pyqtSlot(int)
    def set_cam_no(self, cam_no = 0):
        self.cam_no = cam_no

    @pyqtSlot(float)
    def set_downsampling(self, downsampling = 0.5):
        self.downsampling = downsampling

    @pyqtSlot(np.ndarray)
    def set_spectral_sensitivity(self, spectral_sensitivity = []):
        self.spectral_sensitivity = spectral_sensitivity
        self.spectral_sensitivity_calibrated = True
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
