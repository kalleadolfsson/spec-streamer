import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt("experiment_data.txt", delimiter = ",", skiprows=1)
waves = data[0,:]
intensities = data[1,:]

# Plot results
plt.figure(1)
plt.plot(waves,intensities)
plt.grid(True)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized intensity (A.U.)')
plt.show()
