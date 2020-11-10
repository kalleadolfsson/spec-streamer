
import os
import re
import subprocess
import time
from datetime import datetime
import csv
import xlwt
import pandas as pd
from pandas import DataFrame

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap, QScreen
from PyQt5.QtCore import QTimer, QThread, QObject, QEventLoop, pyqtSignal, pyqtSlot

#import configparser to read from conf file
import configparser

#import numpy and math for easy data handling
import numpy as np
import math
import scipy.io as sio

# import matplot library
#from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
#import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pyqtgraph.exporters


# import Opencv module
import cv2



class Acquisition:
  def __init__(self, spectrometer, ui):
      self.spectrometer = spectrometer
      self.ui = ui
      self.pixel_wavelength_calibrated = False
      self.spectral_sensitivity_calibrated = False

  def update_acquisition(self):
      # Check current state by reading button text (could do this another way)
      if(self.ui.live_button.text() == "Live"):
          # update live_button text
          self.unpause_acquisition()
      else:
          # update live_button text
          self.pause_acquisition()

  def restart_acquisition(self, calibration_compromised = False):
      if(calibration_compromised):
          self.pixel_wavelength_calibrated = False
          self.spectral_sensitivity_calibrated = False
      self.pause_acquisition()
      self.read_acquisition_input_form()
      self.set_wavelengths()
      print('Here')
      self.update_spectrometer_settings()
      #self.setup_plots()
      self.unpause_acquisition()

  def start_acquisition(self):
      self.update_spectrometer_settings()
      self.spectrometer.start()

  def pause_acquisition(self):
      self.spectrometer.pause()
      self.ui.live_button.setText("Live")

  def unpause_acquisition(self):
      self.spectrometer.unpause()
      self.ui.live_button.setText("Stop")

  def stop_acquisition(self):
      self.spectrometer.stop()
      self.spectrometer.quit()

  def update_spectrometer_settings(self):
      self.spectrometer.set_integration_time(self.integration_time)
      self.spectrometer.set_averages(self.averages)
      self.spectrometer.set_gain(self.gain)
      self.spectrometer.set_width(self.width)
      self.spectrometer.set_height(self.height)
      self.spectrometer.set_rotation_global(self.rotation_global)
      self.spectrometer.set_rotation_spectrum(self.rotation_spectrum)
      self.spectrometer.set_central_line(self.central_line)
      self.spectrometer.set_no_of_lines(self.no_of_lines)
      self.spectrometer.set_start_x(self.start_x)
      self.spectrometer.set_stop_x(self.stop_x)
      self.spectrometer.set_scale_overview(self.scale_overview)
      self.spectrometer.set_scale_cropped(self.scale_cropped)
      self.spectrometer.set_crop(self.crop)
      self.spectrometer.set_cam_no(self.cam_no)
      self.spectrometer.apply()

  def load_acquisition_settings(self):
      self.pause_acquisition()
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
      self.start_x = config['SpectrometerConfig'].getint('start_x')
      self.stop_x = config['SpectrometerConfig'].getint('stop_x')
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
      self.restart_acquisition()

  def save_acquisition_settings(self):
      # Open dialog for saving acquisition settings
      self.update_settings_config_parser()
      config_file_path = QFileDialog.getSaveFileName(self, "Save settings", "conf", "Config Files (*.conf)")
      self.save_config_file_path = config_file_path[0]
      self.write_acquisition_settings_to_file(save_path = self.save_config_file_path)

  def create_settings_config_parser(self):
      # Setup configparser for writing to config file
      self.config = configparser.ConfigParser()

  def write_acquisition_settings_to_file(self, save_path = ''):
      try:
          with open(save_path, 'w') as configfile:
              self.config.write(configfile)
          print('Successfully saved settings')
      except:
          print('Error saving to config file')

  def update_settings_config_parser(self):
      # Setup configparser for writing to config file
      self.config['SpectrometerConfig'] = {'spectrometer_name': self.spectrometer_name,
                                           'integration_time' : self.integration_time,
                                           'averages' : self.averages,
                                           'gain' : self.gain,
                                           'width' : self.width,
                                           'height' : self.height,
                                           'rotation_global' : self.rotation_global,
                                           'rotation_spectrum' : self.rotation_spectrum,
                                           'central_line' : self.central_line,
                                           'no_of_lines' : self.no_of_lines,
                                           'start_x' : self.start_x,
                                           'stop_x' : self.stop_x,
                                           'scale_overview' : self.scale_overview,
                                           'scale_cropped' : self.scale_cropped,
                                           'crop' : self.crop,
                                           'cam_no' : self.cam_no}



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
      self.start_x = int(re.sub("\D","",self.ui.spectrum_start_x_input.text()))
      self.stop_x = int(re.sub("\D","",self.ui.spectrum_stop_x_input.text()))
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
      print("update_text_in_acquisition_input_form" + str(self.rotation_global))
      self.ui.spectrum_rotation_global_input.setText(str(self.rotation_global))
      self.ui.spectrum_rotation_spectrum_input.setText(str(self.rotation_spectrum))
      self.ui.spectrum_start_x_input.setText(str(self.start_x))
      self.ui.spectrum_stop_x_input.setText(str(self.stop_x))
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

  def set_wavelengths(self):
      if(self.pixel_wavelength_calibrated):
          self.ui.raw_plot_lambda_label.setText('λ (nm)')
          self.ui.calc_plot_1_lambda_label.setText('λ (nm)')
          self.ui.calc_plot_1_combo_lambda_label.setText('λ (nm)')
          self.ui.calc_plot_2_lambda_label.setText('λ (nm)')
          self.ui.calc_plot_2_combo_lambda_label.setText('λ (nm)')
          self.ui.calc_plot_3_lambda_label.setText('λ (nm)')
      else:
          self.bins = self.stop_x-self.start_x
          self.waves = np.arange(self.start_x,self.stop_x,1)
          self.ui.raw_plot_lambda_label.setText('Pixel #')
          self.ui.calc_plot_1_lambda_label.setText('Pixel #')
          self.ui.calc_plot_1_combo_lambda_label.setText('Pixel #')
          self.ui.calc_plot_2_lambda_label.setText('Pixel #')
          self.ui.calc_plot_2_combo_lambda_label.setText('Pixel #')
          self.ui.calc_plot_3_lambda_label.setText('Pixel #')
      return self.waves

  def set_pixel_wavelength_calibration_status(self, status = 'False', wavelengths = ''):
      self.pixel_wavelength_calibrated = status
      if(status == 'False'):
          self.waves = np.arange(self.start_x,self.stop_x,1)
      else:
          self.waves = wavelengths


  def set_spectral_sensitivity_calibration_status(self, status = 'False'):
      self.spectral_sensitivity_calibrated = status
