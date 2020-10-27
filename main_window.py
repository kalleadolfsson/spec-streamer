

import os
import re
import subprocess
import time
from datetime import datetime
import csv
import pandas as pd


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

# import matplot library
#from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
#import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pyqtgraph.exporters


# import Opencv module
import cv2
from ui_main_window import *
from Spectrometer import *



class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #data_stream_to_thread = pyqtSignal(int)

        # Read acquisition settings from spectrometer conf file if available
        self.read_from_file = False
        # initial GUI params
        self.ui.calc_plot.hide()

        self.read_acquisition_input_form()
        self.setup_containers()
        self.setup_plots()
        self.setup_gui_signals()
        self.start_acquisition()

    def update_acquisition(self):
        # Check current state by reading button text (could do this another way)
        if(self.ui.live_button.text() == "Live"):
            # update live_button text
            self.unpause_acquisition()
        else:
            # update live_button text
            self.pause_acquisition()

    def restart_acquisition(self):
        self.pause_acquisition()
        self.read_acquisition_input_form()
        self.update_spectrometer_settings()
        time.sleep(0.001)
        self.setup_plots()
        self.unpause_acquisition()

    def start_acquisition(self):
        self.spectrometer = Spectrometer()
        self.setup_thread_signals()
        self.update_spectrometer_settings()
        self.setup_plots()
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

    def update_image(self, img = ''):
        self.ui.image_label.setPixmap(img)

    def setup_containers(self):
        # Setup data storage containers
        self.bins = self.stop_x-self.start_x
        self.waves = np.arange(300,700,400/self.bins)
        self.intensitiesDark = np.zeros(len(self.waves))
        self.intensitiesReference = np.zeros(len(self.waves))
        self.intensitiesFluorescence = np.zeros(len(self.waves))
        self.intensitiesTransmission = np.zeros(len(self.waves))
        # Needs to be defined in a more dynamic way


    def setup_thread_signals(self):
        # show image in img_label
        self.spectrometer.image_stream.connect(self.update_image)

        self.spectrometer.raw_spectrum_stream.connect(self.update_raw_plot)
        self.spectrometer.dark_spectrum_stream.connect(self.dark_spectrum_recieved)
        self.spectrometer.fluorescence_spectrum_stream.connect(self.fluorescence_spectrum_recieved)
        self.spectrometer.reference_spectrum_stream.connect(self.reference_spectrum_recieved)
        self.spectrometer.transmission_spectrum_stream.connect(self.transmission_spectrum_recieved)



    def dark_spectrum_recieved(self, data = ''):
        self.intensitiesDark = data
        self.update_calc_plot(data)

    def reference_spectrum_recieved(self, data = ''):
        self.intensitiesReference = data
        self.update_calc_plot_2(data)

    def fluorescence_spectrum_recieved(self, data = ''):
        self.intensitiesFluorescence = data
        self.update_calc_plot_3(data)
        self.pause_acquisition()

    def transmission_spectrum_recieved(self, data = ''):
        self.intensitiesTransmission = data
        self.update_calc_plot_3(data)
        self.pause_acquisition()

    def acquire_dark_spectrum(self):
        self.spectrometer.acquireDarkSpectrum()
        # if button for "acquire dark spectrum" has been pressed
        self.setCheckBox(0)

    def acquire_fluorescence_spectrum(self):
        # if button for "acquire transmission spectrum" has been pressed
        self.spectrometer.acquireFluorescenceSpectrum()
        self.setCheckBox(1)

    def acquire_reference_spectrum(self):
        # if button for "acquire reference spectrum" has been pressed
        self.spectrometer.acquireReferenceSpectrum()
        self.setCheckBox(1)

    def acquire_transmission_spectrum(self):
        # if button for "acquire transmission spectrum" has been pressed
        self.spectrometer.acquireTransmissionSpectrum()
        self.setCheckBox(2)


    def setup_gui_signals(self):

        # VIP
        self.ui.junkyard_photonics_label.setText("by junkyard-photonics")

        # ACQUISITION CONTROLS
        # set live_button callback clicked  function
        self.ui.live_button.clicked.connect(self.update_acquisition)
        # set apply_acquisition_settings_button callback clicked  function
        self.ui.apply_acquisition_settings_button.clicked.connect(self.restart_acquisition)
        # set load_acquisition_settings_button callback clicked function
        self.ui.load_acquisition_settings_button.clicked.connect(self.load_acquisition_settings)
        # set load_acquisition_settings_button callback clicked function
        self.ui.save_acquisition_settings_button.clicked.connect(self.save_acquisition_settings)


        # Toggle tab container (main menu)
        self.ui.acquisition_button.clicked.connect(lambda: self.main_menu_switch(choice = 'acquisition'))
        self.ui.calibration_button.clicked.connect(lambda: self.main_menu_switch(choice = 'calibration'))
        self.ui.experiment_button.clicked.connect(lambda: self.main_menu_switch(choice = 'experiment'))

        # Let Enter-key trigger callback on all QLineEdit objects
        self.ui.detector_integration_time_input.returnPressed.connect(self.restart_acquisition)
        self.ui.detector_averages_input.returnPressed.connect(self.restart_acquisition)
        self.ui.detector_gain_input.returnPressed.connect(self.restart_acquisition)
        self.ui.detector_width_input.returnPressed.connect(self.restart_acquisition)
        self.ui.detector_height_input.returnPressed.connect(self.restart_acquisition)
        self.ui.spectrum_rotation_global_input.returnPressed.connect(self.restart_acquisition)
        self.ui.spectrum_rotation_spectrum_input.returnPressed.connect(self.restart_acquisition)
        self.ui.spectrum_start_x_input.returnPressed.connect(self.restart_acquisition)
        self.ui.spectrum_stop_x_input.returnPressed.connect(self.restart_acquisition)
        self.ui.spectrum_line_input.returnPressed.connect(self.restart_acquisition)
        self.ui.spectrum_lines_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_scale_overview_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_scale_cropped_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_camera_no_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_crop_box.clicked.connect(self.restart_acquisition)



        # EXPERIMENT CONTROLS
        # MENU
        # if button for "Transmission" experiment has been pressed
        self.ui.experiment_menu_transmission_button.clicked.connect(lambda: self.experiment_menu_switch(choice = 'transmission'))
        # if button for "Fluorescence" experiment has been pressed
        self.ui.experiment_menu_fluorescence_button.clicked.connect(lambda: self.experiment_menu_switch(choice = 'fluorescence'))

        # Specific spectrum acquisition
        # if button for "acquire dark spectrum" has been pressed
        self.ui.acquire_dark_spectrum_button.clicked.connect(self.acquire_dark_spectrum)
        # if button for "acquire reference spectrum" has been pressed
        self.ui.acquire_reference_spectrum_button.clicked.connect(self.acquire_reference_spectrum)
        # if button for "acquire transmission spectrum" has been pressed
        self.ui.acquire_transmission_spectrum_button.clicked.connect(self.acquire_transmission_spectrum)
        # if button for "acquire fluorescence spectrum" has been pressed
        self.ui.acquire_fluorescence_spectrum_button.clicked.connect(self.acquire_fluorescence_spectrum)

        # Save experiment data
        # if button for "export data" has been pressed
        self.ui.export_experiment_button.clicked.connect(self.export_experiment)
        # if button for "clear" has been pressed
        self.ui.clear_experiment_button.clicked.connect(self.clear_experiment)

        self.main_menu_switch()
        self.experiment_menu_switch()

    def main_menu_switch(self, choice = 'acquisition'):

        if(choice == 'acquisition'):
            self.ui.main_menu_tab.setCurrentIndex(0)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.image_label.show()

        elif(choice == 'calibration'):
            self.ui.main_menu_tab.setCurrentIndex(1)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.image_label.hide()


        elif(choice == 'experiment'):
            self.ui.main_menu_tab.setCurrentIndex(2)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.image_label.hide()



    def experiment_menu_switch(self, choice = 'transmission'):
        if(choice == 'transmission'):
            self.ui.acquire_dark_spectrum_button.show()
            self.ui.acquire_reference_spectrum_button.show()
            self.ui.acquire_transmission_spectrum_button.show()
            self.ui.acquire_fluorescence_spectrum_button.hide()

            self.ui.experiment_no_1_label.show()
            self.ui.experiment_no_2_label.show()
            self.ui.experiment_no_3_label.show()

            self.ui.experiment_1_ok_check.show()
            self.ui.experiment_2_ok_check.show()
            self.ui.experiment_3_ok_check.show()


            self.update_calc_plot(self.intensitiesDark)
            self.update_calc_plot_2(self.intensitiesReference)
            self.update_calc_plot_3(self.intensitiesTransmission)

            self.ui.calc_plot.show()
            self.ui.calc_plot_2.show()
            self.ui.calc_plot_3.show()

            self.ui.calc_plot_label.show()
            self.ui.calc_plot_2_label.show()
            self.ui.calc_plot_3_label.show()

            self.ui.calc_plot_3_lambda_label.show()
            self.ui.calc_plot_3_i_label.show()

            self.ui.calc_plot_label.setText("Dark")
            self.ui.calc_plot_2_label.setText("Reference")
            self.ui.calc_plot_3_label.setText("Transmission")

            self.ui.experiment_menu_transmission_button.setStyleSheet("color: #24262b;border-bottom-width: 2px;border-color: #24262b;border-style:solid;")
            self.ui.experiment_menu_fluorescence_button.setStyleSheet("color: #24262b;border-bottom-width: 0px;border-color: #24262b;border-style:solid;")


        elif(choice == 'fluorescence'):
            self.ui.acquire_dark_spectrum_button.show()
            self.ui.acquire_reference_spectrum_button.hide()
            self.ui.acquire_transmission_spectrum_button.hide()
            self.ui.acquire_fluorescence_spectrum_button.show()

            self.ui.experiment_no_1_label.show()
            self.ui.experiment_no_2_label.hide()
            self.ui.experiment_no_3_label.show()

            self.ui.experiment_1_ok_check.show()
            self.ui.experiment_2_ok_check.hide()
            self.ui.experiment_3_ok_check.show()

            self.update_calc_plot(self.intensitiesDark)
            self.update_calc_plot_3(self.intensitiesFluorescence)

            self.ui.calc_plot.show()
            self.ui.calc_plot_2.hide()
            self.ui.calc_plot_3.show()

            self.ui.calc_plot_label.show()
            self.ui.calc_plot_2_label.hide()
            self.ui.calc_plot_3_label.show()

            self.ui.calc_plot_2_lambda_label.hide()
            self.ui.calc_plot_2_i_label.hide()

            self.ui.calc_plot_label.setText("Dark")
            self.ui.calc_plot_3_label.setText("Fluorescence")

            self.ui.experiment_menu_transmission_button.setStyleSheet("color: #24262b;border-bottom-width: 0px;border-color: #24262b;border-style:solid;")
            self.ui.experiment_menu_fluorescence_button.setStyleSheet("color: #24262b;border-bottom-width: 2px;border-color: #24262b;border-style:solid;")


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
        print("load_acquisition_settings" + str(self.rotation_global))
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

        config_file_path = QFileDialog.getSaveFileName(self, "Save settings", "conf", "Config Files (*.conf)")
        self.save_config_file_path = config_file_path[0]

        # Setup configparser for writing to config file
        config = configparser.ConfigParser()
        config['SpectrometerConfig'] = {'spectrometer_name': self.spectrometer_name,
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

        try:
            with open(self.save_config_file_path, 'w') as configfile:
                config.write(configfile)
            print('Successfully saved settings')
        except:
            print('Error saving to config file')


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


    def setup_plots(self):
        self.raw_plot_line = self.setup_plot(self.ui.raw_plot)
        self.calc_plot_line = self.setup_plot(self.ui.calc_plot)
        self.calc_plot_2_line = self.setup_plot(self.ui.calc_plot_2)
        self.calc_plot_3_line = self.setup_plot(self.ui.calc_plot_3)

    # checks relevant checkbox to show user that a spectrum has been stored
    def setCheckBox(self, specCheck):
        if(specCheck == 0):
            self.ui.experiment_1_ok_check.setChecked(True)
        elif(specCheck == 1):
            self.ui.experiment_2_ok_check.setChecked(True)
        elif(specCheck == 2):
            self.ui.experiment_3_ok_check.setChecked(True)

    def setup_raw_plot(self):
        self.ui.raw_plot.clear()
        pen = pg.mkPen(color="#14274e", width=1, style=QtCore.Qt.SolidLine)
        self.raw_plot_line = self.ui.raw_plot.plot(self.waves,np.zeros(len(self.waves)), pen=pen)
        self.ui.raw_plot.setBackground('w')
        #self.ui.raw_plot.setYRange(0, 255*01.3*self.no_of_lines, padding=0)
        self.ui.raw_plot.setXRange(300,700, padding=0.1)
        vb_raw = self.ui.raw_plot.getViewBox()
        vb_raw.setBackgroundColor("#f1f6f9")
        vb_raw.setBorder(color="#8d93ab", width=1, style=QtCore.Qt.SolidLine)

    def setup_calc_plot(self):
        self.ui.calc_plot.clear()
        pen = pg.mkPen(color="#14274e", width=1, style=QtCore.Qt.SolidLine)
        self.calc_plot_line = self.ui.calc_plot.plot(self.waves,np.zeros(len(self.waves)), pen=pen)
        self.ui.calc_plot.setBackground('w')
        #self.ui.calc_plot.setYRange(0, 255*01.3*self.no_of_lines, padding=0)
        self.ui.calc_plot.setXRange(300,700, padding=0.1)
        vb_calc = self.ui.calc_plot.getViewBox()
        vb_calc.setBackgroundColor("#f1f6f9")
        vb_raw.setBorder(color="#8d93ab", width=1, style=QtCore.Qt.SolidLine)

    def setup_calc_plot_2(self):
        self.ui.calc_plot_2.clear()
        pen = pg.mkPen(color="#14274e", width=1, style=QtCore.Qt.SolidLine)
        self.calc_plot_2_line = self.ui.calc_plot_2.plot(self.waves,np.zeros(len(self.waves)), pen=pen)
        self.ui.calc_plot_2.setBackground('w')
        #self.ui.calc_plot_2.setYRange(0, 255*01.3*self.no_of_lines, padding=0)
        self.ui.calc_plot_2.setXRange(300,700, padding=0.1)
        vb_calc_2 = self.ui.calc_plot_2.getViewBox()
        vb_calc_2.setBackgroundColor("#f1f6f9")
        vb_raw.setBorder(color="#8d93ab", width=1, style=QtCore.Qt.SolidLine)

    def setup_calc_plot_3(self):
        self.ui.calc_plot_3.clear()
        pen = pg.mkPen(color="#14274e", width=1, style=QtCore.Qt.SolidLine)
        self.calc_plot_3_line = self.ui.calc_plot_3.plot(self.waves,np.zeros(len(self.waves)), pen=pen)
        self.ui.calc_plot_3.setBackground('w')
        #self.ui.calc_plot_3.setYRange(0, 255*01.3*self.no_of_lines, padding=0)
        self.ui.calc_plot_3.setXRange(300,700, padding=0.1)
        vb_calc_3 = self.ui.calc_plot_3.getViewBox()
        vb_calc_3.setBackgroundColor("#f1f6f9")
        vb_raw.setBorder(color="#8d93ab", width=1, style=QtCore.Qt.SolidLine)

    def setup_plot(self, plot_item = ''):
        plot_item.clear()
        pen = pg.mkPen(color="#14274e", width=1, style=QtCore.Qt.SolidLine)
        plot_line = plot_item.plot(self.waves,np.zeros(len(self.waves)), pen=pen)
        plot_item.setBackground('w')
        #self.ui.calc_plot_3.setYRange(0, 255*01.3*self.no_of_lines, padding=0)
        plot_item.setXRange(300,700, padding=0.1)
        vb = plot_item.getViewBox()
        vb.setBackgroundColor("#f1f6f9")
        vb.setBorder(color="#8d93ab", width=1, style=QtCore.Qt.SolidLine)
        return plot_line


    # update "raw" spectrum plot
    def update_raw_plot(self, data = ''):
        self.raw_plot_line.setData(self.waves,data)

    # update dark spectrum plot
    def update_calc_plot(self, data = ''):
        self.calc_plot_line.setData(self.waves,data)

    # update reference spectrum plot
    def update_calc_plot_2(self, data = ''):
        self.calc_plot_2_line.setData(self.waves,data)

    # update transmission spectrum plot
    def update_calc_plot_3(self, data = ''):
        self.calc_plot_3_line.setData(self.waves,data)

    def clear_experiment(self):
        self.setup_plots()
        self.unpause_acquisition()


    def export_images(self, save_images_path = ''):
        img = self.ui.raw_plot_frame.grab()
        img.save(os.path.join(save_images_path, "Raw.png"))

        img2 = self.ui.calc_plot_frame.grab()
        filename_calc_plot = self.ui.calc_plot_label.text() +"AND"+self.ui.calc_plot_2_label.text()+ ".png"
        img2.save(os.path.join(save_images_path, filename_calc_plot))

        img4 = self.ui.calc_plot_3_frame.grab()
        filename_calc_plot_3 = self.ui.calc_plot_3_label.text() + ".png"
        img4.save(os.path.join(save_images_path, filename_calc_plot_3))



    def export_data(self, save_data_path = ''):
        save_data_path = os.path.join(save_data_path, 'experiment_data.csv')
        data = [self.raw_plot_line.getData()[0],
                self.raw_plot_line.getData()[1],
                self.calc_plot_line.getData()[1],
                self.calc_plot_2_line.getData()[1],
                self.calc_plot_3_line.getData()[1]]

        time_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        data_header = 'Times tamp:' + time_stamp + ', Row 1: Wavelengths (nm), Row 2: '+self.ui.raw_plot_label.text() +', Row 3: '+self.ui.calc_plot_label.text() +', Row 4: '+self.ui.calc_plot_2_label.text() +', Row 5: '+self.ui.calc_plot_3_label.text()  
        np.savetxt(save_data_path, data, fmt='%.2f', delimiter=',', header=data_header)



    def export_experiment(self):
        # Open dialog for saving experimental data
        save_experiment_path  = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        folder_name = datetime.now().strftime("%Y%m%d-%H%M%S")
        save_experiment_path = os.path.join(save_experiment_path, folder_name)
        os.makedirs(save_experiment_path)
        self.export_images(save_images_path = save_experiment_path)
        self.export_data(save_data_path = save_experiment_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
