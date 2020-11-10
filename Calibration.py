
import os
import time
import re
# import system module
import sys
from datetime import datetime
#import numpy and math for easy data handling
import numpy as np
import math as m

from scipy.optimize import curve_fit

class Calibration:
  def __init__(self):
      self.pixel_wavelength_calibrated = False
      self.spectral_sensitivity_calibrated = False

      self.uncorrected_intensity_data = np.array([])
      self.spectral_sensitivity = np.array([])
      self.pixels = np.array([])
      self.pixel_wavelength_points = np.array([])
      self.wavelengts = np.array([])
      self.black_body_temperature = 0

      # CONSTANTS
      self.Kb = 5.67e-8      # W⋅m**−2⋅K**−4
      self.c = 3e8
      self.h = 6.63e-34

  def set_uncorrected_intensity_data(self, intensities = ''):
      self.uncorrected_intensity_data = intensities
      self.uncorrected_intensity_data_set = True

  def set_pixels(self, pixels = ''):
      self.pixels = pixels
      self.pixels_set = True

  def set_pixel_wavelength_points(self, pixels = '', wavelengths = ''):
      self.pixel_wavelength_points_pixels = pixels
      self.pixel_wavelength_points_wavelengths = wavelengths
      self.pixel_wavelength_points_set = True

  def set_wavelengths(self, wavelengths = ''):
      self.wavelengths = wavelengths

  def set_pixels(self, pixels = ''):
      self.pixels = pixels

  def get_wavelengths(self, pixels = ''):
      self.pixels = pixels

      # curve_fit(pixel_wavelength_model, pixels, wavelength)
      popt, pcov = curve_fit(self._pixel_wavelength_model,
                             self.pixel_wavelength_points_pixels,
                             self.pixel_wavelength_points_wavelengths)
      self.popt = popt
      self.wavelengths = self._pixel_wavelength_model(self.pixels, *popt)
      self.pixel_wavelength_calibrated = True
      return self.wavelengths, self.popt

  def set_black_body_temperature(self, temperature = ''):
      self.black_body_temperature = temperature

  def get_spectral_sensitivity(self):
      waves  = self.wavelengths*1E-9
      intensities_black_body = self._planck_radiation_model(waves = waves,
                                                           T = self.black_body_temperature)
      self.spectral_sensitivity = self.uncorrected_intensity_data/intensities_black_body
      self.spectral_sensitivity = self.spectral_sensitivity/np.max(self.spectral_sensitivity)
      self.spectral_sensitivity_calibrated = True
      return self.spectral_sensitivity

  def set_pixel_wavelength_coeffs(self, coeffs = ''):
      self.popt = coeffs

  def set_spectral_sensitivity(self, spectral_sensitivity = ''):
      self.spectral_sensitivity = spectral_sensitivity

  def set_calibration_status(self,calibration_type = '', calibrated = ''):
      if(calibration_type == 'pixel_wavelength'):
          self.pixel_wavelength_calibrated = calibrated
      elif(calibration_type == 'spectral_sensitivity'):
          self.spectral_sensitivity_calibrated = calibrated

  def _pixel_wavelength_model(self, x, a, b, c, d):
      return a + b*x + c*x**2 + d*x**3

  def _planck_radiation_model(self, waves, T):
      return (2*m.pi*self.h*(self.c**2))*(waves**-5)/(np.exp((self.h*self.c)/(waves*self.Kb*T))-1)

  def save(self):
      if(self.pixel_wavelength_calibrated):
          self._export_calibration_data_txt()
      else:
          raise Exception("Pixel-Wavelength calibration is not set or compromised")

      self._save_acquisition_settings()

  def set_save_path(self, save_path = ''):
      self.save_path = save_path
      self.timestamp = datetime.now().strftime("%y%m%d-%H%M")
      folder_name = self.timestamp + "_calibration"
      self.save_path = os.path.join(self.save_path, folder_name)
      os.makedirs(self.save_path)

  def set_acquisition_settings(self, config = ''):
      self.config = config

      self.config['PixelWavelengthCalibration'] = {
                  'pixel_wavelength_points_pixels': self.pixel_wavelength_points_pixels,
                  'pixel_wavelength_points_wavelengths' : self.pixel_wavelength_points_wavelengths,
                  'popt' : self.popt,
                  'pixels' : self.pixels,
                  'wavelengths' : np.round(self.wavelengths,4)
             }

      if(self.spectral_sensitivity_calibrated):
          self.config['SpectralSensitivityCalibration'] = {
                      'black_body_temperature' : self.black_body_temperature,
                      'uncorrected_intensity_data': self.uncorrected_intensity_data,
                      'spectral_sensitivity' : self.spectral_sensitivity,
                 }


  def _save_acquisition_settings(self):
      self.save_acquisition_settings_path = os.path.join(self.save_path, 'settings.conf')
      try:
          with open(self.save_acquisition_settings_path, 'w') as configfile:
              self.config.write(configfile)
              print('Successfully saved settings')
      except:
              print('Error saving to config file')

  def _export_calibration_data_txt(self):

      save_txt_path = os.path.join(self.save_path, 'calibration_data.txt')
      time_header = 'Timestamp:' + self.timestamp + "\n\n"
      pixel_wavelength_header = ("[Pixel-Wavelength]\n"
                                 "Calibration pixels:{}\n"
                                 "Calibration wavelengths (nm):{}\n"
                                 "Calibration polynomial coefficients:{}\n\n").format(\
                                self.pixel_wavelength_points_pixels,
                                self.pixel_wavelength_points_wavelengths,
                                self.popt)

      data_header = ("[Data]\n"
                    "Row 1: Pixels\n"
                    "Row 2: Calculated wavelengths (nm)\n")
      data = np.array([self.pixels,
                       self.wavelengths])

      if(self.spectral_sensitivity_calibrated):
          spectral_sensitivity_header = ("[Spectral sensitivity] \nBlack-body temperature: "
                                        "{}K\n\n").format(self.black_body_temperature)
          data_header = data_header + "Row 3: Uncorrected intensity data\nRow 4: Spectral sensitivity\n"
          np.vstack([data, self.uncorrected_intensity_data])
          np.vstack([data, self.spectral_sensitivity])

      joined_header = time_header+pixel_wavelength_header+spectral_sensitivity_header+data_header

      np.savetxt(save_txt_path, data, fmt='%.2f', delimiter=',', header=joined_header)
