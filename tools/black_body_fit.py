import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization
import math as m
import scipy.constants

# Application example: load and fit data to black body curve (Planck radiation law)

# Constants
h = scipy.constants.Planck
kb = scipy.constants.k
c = scipy.constants.c

# Kelvin to Celsius offset
K2C = 273

# Load data
data = np.loadtxt("experiment_data.txt", delimiter = ",", skiprows=1)
waves = data[0,:]
intensities = data[1,:]

# Normalize intensity data to prevent overflow during curve fitting
intensities = intensities/np.max(intensities)

# Planck radiation law
def planckFunc(wavelengths, temperature, amplitude):
    return amplitude*(2*h*(c**2)/(wavelengths**5))*np.exp(((h*c)/((wavelengths*kb*temperature)))-1)**(-1)

# First guess for lsq curve fitting
x0 = np.array([1500, 5E-10])

# Least squares optimization
fit_out = (optimization.curve_fit(planckFunc, waves*1e-9, intensities, x0, maxfev=12000))

# Extract relevant params from curve fitting output (Temperature in Kelvin and amplitude)
Tfit = fit_out[0][0]
fitAmp = fit_out[0][1]

# Plot results
plt.figure(1)
text = 'T = {}C'.format(np.round(Tfit-K2C,2))
plt.text(550,0.5,text)
plt.plot(waves,intensities/np.max(intensities))
plt.plot(waves,planckFunc(waves*1e-9, Tfit, fitAmp))
plt.grid(True)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized intensity (A.U.)')
plt.show()
