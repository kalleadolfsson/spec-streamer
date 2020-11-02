
import os
import time

# import system module
import sys

#import numpy and math for easy data handling
import numpy as np
import math

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt



class Calibration:
  def __init__(self):
      self.calibration_type = ''
      self.uncorrected_intensity_data = np.array([])
      self.corrected_intensity_data = np.array([])
      self.pixels = np.array([])
      self.pixel_wavelength_points = np.array([])
      self.wavelengts = np.array([])


  def set_calibration_type(self, calibration_type):
      self.calibration_type = experiment_type
      self.calibration_type_set = True

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

  def get_wavelengths(self, pixels = ''):
      self.pixels = pixels

      # curve_fit(pixel_wavelength_model, pixels, wavelength)
      popt, pcov = curve_fit(self.pixel_wavelength_model, self.pixel_wavelength_points_pixels, self.pixel_wavelength_points_wavelengths)

      self.wavelengths = self.pixel_wavelength_model(self.pixels, *popt)
      return self.wavelengths

  def pixel_wavelength_model(self, x, a, b, c):
      return a + b*x + c*x**2 + c*x**3
