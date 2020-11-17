
import os
import time

# import system module
import sys

#import numpy and math for easy data handling
import numpy as np
import math as m

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt


# CONSTANTS
Kb = 1.28e-23      # W⋅m**−2⋅K**−4
c = 3e8
h = 6.63e-34

wavelengths = np.arange(400,900,0.5)
uncorrected_intensity_data = np.ones(len(wavelengths))
black_body_temperature = 2800
spectral_sensitivity = np.array([])

def planck_radiation_model(waves, T):
  return ((2*m.pi*h*(c**2))/(waves**5))/(np.exp((h*c)/(waves*Kb*T))-1)


def get_spectral_sensitivity():
  waves  = wavelengths*1E-9
  intensities_black_body = planck_radiation_model(waves = waves, T = black_body_temperature)
  spectral_sensitivity = uncorrected_intensity_data/intensities_black_body
  spectral_sensitivity = spectral_sensitivity/np.max(spectral_sensitivity)

  plt.plot(wavelengths,intensities_black_body)
  plt.show()
  return spectral_sensitivity

get_spectral_sensitivity()
