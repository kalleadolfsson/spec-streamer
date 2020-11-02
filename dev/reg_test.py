
import os
import time

# import system module
import sys

#import numpy and math for easy data handling
import numpy as np
import math

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

def pixel_wavelength_model( x, a, b, c):
  return a + b*x + c*x**2 + c*x**3


pixels = np.arange(750, 1200,1)
# curve_fit(pixel_wavelength_model, pixels, wavelength)

pixel_wavelength_points_pixels = np.array([750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200])
pixel_wavelength_points_wavelengths = np.array([350, 421, 498, 561, 625, 690, 755, 832, 900, 965])


popt, pcov = curve_fit(pixel_wavelength_model, pixel_wavelength_points_pixels, pixel_wavelength_points_wavelengths)
plt.plot(pixels, pixel_wavelength_model(pixels, *popt), 'g--',)
plt.plot(pixel_wavelength_points_pixels, pixel_wavelength_points_wavelengths, 'r*',)
plt.show()


#return self.wavelengths
