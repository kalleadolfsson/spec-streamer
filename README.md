# README

### GOAL
The primary goal of the project is to develop an intuitive software that allows for advanced spectral analysis with USB-camera-based spectrometers.

### CONTRIBUTION

######  Please find CONTRIBUTION.md for further information about contributing

### Dependencies
pandas==0.24.2\
numpy==1.16.3\
scipy==1.3.0\
xlwt==1.3.0\
imutils==0.5.3\
qimage2ndarray==1.8.3\
matplotlib==3.1.0\
opencv_contrib_python==4.1.2.30\
pyqtgraph==0.11.0\
PyQt5==5.15.1\

### USAGE
#### Startup
Run command:
´´´python
python3 main_window.py
´´´

A prerequisite for the software to start, is that a USB-camera device with opencv-compatibility is connected. Although compatibility depends primarily on the camera device used, Windows and Linux appears to have better openCV support than Mac (where some openCV functions are not supported).

Connecting a USB camera (or if there is an integrated USB-camera available) is normally all it takes for the software to start up and serve continuous video stream and a line plot. If the software is percieved as slow/non-responsive it is likely due to too large images being served in the video stream and this can be reduced (without reducing spectral resolution) by reducing the downsampling parameter.

It is up to the user to achieve a spectral projection in the image. When this is achieved, the line plot ranges can be specified to make sure that the spectral projection is maximized within the line data window. A cropped window showing the extent of the window used for the lineplot helps to tune this.

#### Calibration
The pixel data (x-axis) can then be transformed to wavelength by pixel wavelength calibration. By identifying known spectral peaks (most easily done using a fluorescent light or low energy light source and searching for the expected peaks) and noting at what pixels the respective peaks are centered around, the wavlength vs pixel no projection can be calculated and applied to express the x-axis in wavelength (nanometers, nm).

Once the pixel wavelength calibration has been conducted, it is possible to calibrate for the spectral sensitivity. This is carried out by obtaining a spectral projection from a black body of known temperature (for instance a common halogen lamp, which are typically 2800-3000K, normally stated at the box).

After calibration, any changes to the acquisition can/will compromise the calibration. It is also important to note that because there are so many different USB-cameras with different optical performance, sensor specs and openCV functionality it is impossible to guarantee valid calibrations.

#### Experiments
The software currently has an experiment section where the purpose is to simplify data acquisition and analysis for some basic experimental flows (currently support for Transmission and Emission). The idea is to follow the suggested flow and the operations associated with each experiment is carried out automatically to arrive at the calculated "end-plot" (e.g. the Transmission plot in the Transmission experiment).

#### Saving/Loading settings and data
The experimental data can be saved as an Experiment, where all the plots, raw data and settings (including calibrations) are saved as images and in various data formats for post analysis or for loading at later time.

Settings can be saved from the acquisition menu but is also saved when saving calibration or an experiment.

Individual plots and/or associated raw data can be saved by clicking at the ".png" or ".txt" buttons next to each plot.

#### General
###### Command for compiling Qt-GUI
```python
python3 -m PyQt5.uic.pyuic -x ui_main_window.ui -o ui_main_window.py
```
