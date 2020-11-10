

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
from ui_main_window import *
from Spectrometer import *
from Experiment import *
from Calibration import *

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

        self.spectrometer = Spectrometer()
        self.acquisition = Acquisition(self.spectrometer)
        self.calibration = Calibration()

        self.plot_acquisition_mode = 'experiment'
        self.read_acquisition_input_form()
        self.setup_containers()
        self.setup_plots()
        self.setup_gui_signals()
        self.create_settings_config_parser()
        self.start_acquisition()

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
        self.update_spectrometer_settings()
        self.setup_plots()
        self.unpause_acquisition()

    def start_acquisition(self):
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
        self.pixel_wavelength_calibrated = False
        self.spectral_sensitivity_calibrated = False
        self.set_wavelengths()
        self.intensitiesRaw = np.zeros(len(self.waves))
        self.intensitiesDark = np.zeros(len(self.waves))
        self.intensitiesReference = np.zeros(len(self.waves))
        self.intensitiesEmission = np.zeros(len(self.waves))
        self.intensitiesTransmission = np.zeros(len(self.waves))
        # Needs to be defined in a more dynamic way


    def setup_thread_signals(self):
        # show image in img_label
        self.spectrometer.image_stream.connect(self.update_image)
        self.spectrometer.raw_spectrum_stream.connect(self.raw_spectrum_recieved)
        self.spectrometer.dark_spectrum_stream.connect(self.dark_spectrum_recieved)
        self.spectrometer.emission_spectrum_stream.connect(self.emission_spectrum_recieved)
        self.spectrometer.reference_spectrum_stream.connect(self.reference_spectrum_recieved)
        self.spectrometer.transmission_spectrum_stream.connect(self.transmission_spectrum_recieved)

    def raw_spectrum_recieved(self, data = ''):
        self.intensitiesRaw = data
        self.update_plot(plot_line = self.raw_plot_line, data = data)

    def dark_spectrum_recieved(self, data = ''):
        self.intensitiesDark = data
        self.update_plot(plot_line = self.calc_plot_1_line, data = data)
        self.update_plot(plot_line = self.calc_plot_1_combo_line, data = data)

    def reference_spectrum_recieved(self, data = ''):
        self.intensitiesReference = data
        self.update_plot(plot_line = self.calc_plot_2_line, data = data)
        self.update_plot(plot_line = self.calc_plot_2_combo_line, data = data)

    def emission_spectrum_recieved(self, data = ''):
        self.intensitiesEmission = data
        self.update_plot(plot_line = self.calc_plot_3_line, data = data)
        self.pause_acquisition()

    def transmission_spectrum_recieved(self, data = ''):
        self.intensitiesTransmission = data
        self.update_plot(plot_line = self.calc_plot_3_line, data = data)
        self.pause_acquisition()

    def acquire_dark_spectrum(self):
        self.spectrometer.acquireDarkSpectrum()
        # if button for "acquire dark spectrum" has been pressed
        self.setCheckBox(0)

    def acquire_emission_spectrum(self):
        # if button for "acquire transmission spectrum" has been pressed
        self.spectrometer.acquireEmissionSpectrum()
        self.setCheckBox(1)

    def acquire_reference_spectrum(self):
        # if button for "acquire reference spectrum" has been pressed
        self.spectrometer.acquireReferenceSpectrum()
        self.setCheckBox(1)

    def acquire_transmission_spectrum(self):
        # if button for "acquire transmission spectrum" has been pressed
        self.spectrometer.acquireTransmissionSpectrum()
        self.setCheckBox(2)


    def calibration_back_button(self):
        self.clear_calibration_pane()
        if(self.calibration_choice == 'pixel_wavelength'):
            self.pixel_wavelength_back()
        if(self.calibration_choice == 'spectral_sensitivity'):
            self.spectral_sensitivity_back()

    def calibration_next_button(self):
        self.clear_calibration_pane()
        if(self.calibration_choice == 'pixel_wavelength'):
            self.pixel_wavelength_next()
        if(self.calibration_choice == 'spectral_sensitivity'):
            self.spectral_sensitivity_next()


    def clear_calibration_pane(self):
        self.ui.calibration_plot_acquisition_flow_frame.hide()
        self.ui.calibration_identify_peaks_frame.hide()
        self.ui.calibration_pixel_wavelength_polynomial_frame.hide()
        self.ui.calibration_get_spectral_sensitivity_frame.hide()
        self.ui.calibration_set_black_body_frame.hide()
        self.ui.calibration_identify_peaks_frame.hide()
        self.ui.calibration_next_button.hide()
        self.ui.calibration_back_button.hide()

    def set_calibration_flow_labels(self,stage = ''):
        pixel_wavelength_label_text = ['Acquire spectra','Identify peaks', 'Get projection']
        spectral_sensitivity_label_text = ['Acquire spectra','Set black-body', 'Get spectral sensitivity']

        labels =    [self.ui.calibration_step_1_label,
                    self.ui.calibration_step_2_label,
                    self.ui.calibration_step_3_label]
        cntr = 0
        for label in labels:
            if(cntr == stage):
                label.setStyleSheet("color:#24262b;outline-width: 0ps;border-radius: 0px;border-style: solid;border-width: 0px;")
            else:
                label.setStyleSheet("color:#9ba4b4;outline-width: 0ps;border-radius: 0px;border-style: solid;border-width: 0px;")
            if(self.calibration_choice == 'pixel_wavelength'):
                label.setText(pixel_wavelength_label_text[cntr])
            elif(self.calibration_choice == 'spectral_sensitivity'):
                label.setText(spectral_sensitivity_label_text[cntr])
            cntr = cntr + 1



    def pixel_wavelength_next(self):
        if(self.pixel_wavelength_stage == 0):
            self.pixel_wavelength_stage = self.pixel_wavelength_stage + 1
            self.ui.calibration_identify_peaks_frame.show()
            self.ui.calibration_back_button.show()
            self.ui.calibration_next_button.show()
            self.set_calibration_flow_labels(stage = 1)

        elif(self.pixel_wavelength_stage == 1):
            self.pixel_wavelength_stage = self.pixel_wavelength_stage + 1
            self.ui.calibration_pixel_wavelength_polynomial_frame.show()
            self.ui.calibration_back_button.show()

            self.set_calibration_flow_labels(stage = 2)
            pixels, wavelengths = self.get_pixel_wavelength_points()
            self.calibration.set_pixel_wavelength_points(pixels,wavelengths)
            self.waves, coeffs = self.calibration.get_wavelengths(self.waves)
            self.ui.pixel_wavelength_polynomial_coeffs_a_label.setText("A = "+str(float('%.3g' % coeffs[0])))
            self.ui.pixel_wavelength_polynomial_coeffs_b_label.setText("B = "+str(float('%.3g' % coeffs[1])))
            self.ui.pixel_wavelength_polynomial_coeffs_c_label.setText("C = "+str(float('%.3g' % coeffs[2])))
            self.ui.pixel_wavelength_polynomial_coeffs_d_label.setText("D = "+str(float('%.3g' % coeffs[3])))

            self.pixel_wavelength_calibrated = True
            self.restart_acquisition()

    def pixel_wavelength_back(self):
        if(self.pixel_wavelength_stage == 1):
            self.ui.calibration_plot_acquisition_flow_frame.show()
            self.pixel_wavelength_stage = self.pixel_wavelength_stage - 1
            self.ui.calibration_next_button.show()
            self.set_calibration_flow_labels(stage = 0)

        elif(self.pixel_wavelength_stage == 2):
            self.pixel_wavelength_stage = self.pixel_wavelength_stage - 1
            self.ui.calibration_identify_peaks_frame.show()
            self.ui.calibration_next_button.show()
            self.ui.calibration_back_button.show()
            self.set_calibration_flow_labels(stage = 1)

    def remove_pixel_wavelength_item(self, item):
        self.ui.pixel_wavelength_list.takeItem(self.ui.pixel_wavelength_list.row(item))

    def add_pixel_wavelength_item(self):
        pixel_temp = int(re.sub("\D","",self.ui.pixel_input.text()))
        wavelength_temp = float(re.sub("\D","",self.ui.wavelength_input.text()))
        item = "{}                            {} ".format(pixel_temp, wavelength_temp)
        self.ui.pixel_wavelength_list.addItem(item)
        self.ui.pixel_input.setText('')
        self.ui.wavelength_input.setText('')

    def get_pixel_wavelength_points(self):
        itemsTextList =  [str(self.ui.pixel_wavelength_list.item(i).text()) for i in range(self.ui.pixel_wavelength_list.count())]
        pixels = np.zeros(self.ui.pixel_wavelength_list.count())
        wavelengths = np.zeros(self.ui.pixel_wavelength_list.count())
        cntr = 0
        for item in itemsTextList:
          temp_item = item.split()
          pixels[cntr] = float(temp_item[0])
          wavelengths[cntr] = float(temp_item[1])
          cntr = cntr + 1
        return pixels, wavelengths

    def calibration_start_pane(self):
        self.clear_calibration_pane()
        self.ui.calibration_plot_acquisition_flow_frame.show()
        self.ui.calibration_next_button.show()
        self.set_calibration_flow_labels(stage = 0)

    def spectral_sensitivity_next(self):
        if(self.spectral_sensitivity_stage == 0):
            self.spectral_sensitivity_stage = self.spectral_sensitivity_stage + 1
            self.ui.calibration_back_button.show()
            self.ui.calibration_next_button.show()
            self.ui.calibration_set_black_body_frame.show()
            self.set_calibration_flow_labels(stage = 1)

        elif(self.spectral_sensitivity_stage == 1):
            self.spectral_sensitivity_stage = self.spectral_sensitivity_stage + 1
            self.ui.calibration_back_button.show()

            black_body_temperature = self.get_black_body_temperature()
            #uncorrected_intensities = self.spectrometer.get_uncorrected_intensities()
            self.calibration.set_uncorrected_intensity_data(intensities = self.intensitiesRaw)
            self.calibration.set_black_body_temperature(temperature = black_body_temperature)
            spectral_sensitivty = self.calibration.get_spectral_sensitivity()
            self.spectrometer.set_spectral_sensitivity(spectral_sensitivity = spectral_sensitivty)
            self.set_calibration_flow_labels(stage = 2)
            self.restart_acquisition()

    def spectral_sensitivity_back(self):
        if(self.spectral_sensitivity_stage == 1):
            self.spectral_sensitivity_stage = self.spectral_sensitivity_stage - 1
            self.ui.calibration_plot_acquisition_flow_frame.show()
            self.ui.calibration_next_button.show()
            self.set_calibration_flow_labels(stage = 0)

        elif(self.spectral_sensitivity_stage == 2):
            self.spectral_sensitivity_stage = self.spectral_sensitivity_stage - 1
            self.ui.calibration_set_black_body_frame.show()
            self.ui.calibration_next_button.show()
            self.ui.calibration_back_button.show()
            self.set_calibration_flow_labels(stage = 1)

    def get_black_body_temperature(self):
        black_body_temperature = float(re.sub("\D","",self.ui.black_body_temperature_input.text()))
        return black_body_temperature

    def save_plot_png(self, plot_frame = [],  frame_name = []):
        self.sub_experiment_png = Experiment()
        self.sub_experiment_png.set_plot_frames(plot_frames = [plot_frame])
        self.sub_experiment_png.set_frame_names(frame_names = [frame_name] )
        self.export_experiment(self.sub_experiment_png)

    def save_plot_txt(self, plot_name = [],  plot_data = '' ):
        self.sub_experiment_txt = Experiment()
        self.sub_experiment_txt.set_plot_data(plot_names = [plot_name],
                                              plot_data = plot_data)
        self.sub_experiment_txt.set_data_types(data_types = ['txt'])
        self.export_experiment(self.sub_experiment_txt)

    def setup_gui_signals(self):

        # VIP
        self.ui.spec_tools_label.setText("by spec-tools")

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

        self.ui.detector_width_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.detector_height_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.spectrum_rotation_global_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.spectrum_rotation_spectrum_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.spectrum_start_x_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.spectrum_stop_x_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.spectrum_line_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))
        self.ui.spectrum_lines_input.returnPressed.connect(lambda: self.restart_acquisition(calibration_compromised = True))

        self.ui.image_scale_overview_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_scale_cropped_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_camera_no_input.returnPressed.connect(self.restart_acquisition)
        self.ui.image_crop_box.clicked.connect(self.restart_acquisition)



        # CALIBRATION CONTROLS
        # MENU
        # if button for "Pixel wavelength" calibration has been pressed
        self.ui.calibration_menu_pixel_wavelength_button.clicked.connect(lambda: self.calibration_menu_switch(choice = 'pixel_wavelength'))
        # if button for "Spectral sensitivity" calibration has been pressed
        self.ui.calibration_menu_spectral_sensitivity_button.clicked.connect(lambda: self.calibration_menu_switch(choice = 'spectral_sensitivity'))

        self.ui.save_calibration_button.clicked.connect(self.export_calibration)

        # Specific spectrum acquisition
        # if button for "acquire dark spectrum" has been pressed
        self.ui.calibration_acquire_dark_spectrum_button.clicked.connect(self.acquire_dark_spectrum)
        # if button for "acquire reference spectrum" has been pressed
        self.ui.calibration_acquire_reference_spectrum_button.clicked.connect(self.acquire_reference_spectrum)
        # if button for "acquire transmission spectrum" has been pressed
        self.ui.calibration_acquire_transmission_spectrum_button.clicked.connect(self.acquire_transmission_spectrum)
        # if button for "acquire emission spectrum" has been pressed
        self.ui.calibration_acquire_emission_spectrum_button.clicked.connect(self.acquire_emission_spectrum)

        self.ui.calibration_next_button.clicked.connect(self.calibration_next_button)
        self.ui.calibration_back_button.clicked.connect(self.calibration_back_button)

        self.ui.pixel_wavelength_list.itemClicked.connect(self.remove_pixel_wavelength_item)
        self.ui.add_pixel_wavelength_point_button.clicked.connect(self.add_pixel_wavelength_item)

        # if button for "clear" has been pressed
        self.ui.clear_calibration_button.clicked.connect(self.clear_spectra)


        # GET CURSOR DATA FROM FRAMES/PLOTS
        #proxy = pg.SignalProxy(self.ui.raw_plot.scene().sigMouseMoved, rateLimit=60, slot=self.cursor_in_plot)
        #pg.SignalProxy(self.ui.raw_plot.scene().sigMouseMoved, rateLimit=60, slot=lambda: print('hello'))
        self.ui.raw_plot.scene().sigMouseMoved.connect(self.cursor_in_raw_plot)

        self.ui.calc_plot_3.scene().sigMouseMoved.connect(self.cursor_in_calc_plot_3)

        # EXPERIMENT CONTROLS
        # MENU
        # if button for "Transmission" experiment has been pressed
        self.ui.experiment_menu_transmission_button.clicked.connect(lambda: self.experiment_menu_switch(choice = 'transmission'))
        # if button for "emission" experiment has been pressed
        self.ui.experiment_menu_emission_button.clicked.connect(lambda: self.experiment_menu_switch(choice = 'emission'))

        # Specific spectrum acquisition
        # if button for "acquire dark spectrum" has been pressed
        self.ui.experiment_acquire_dark_spectrum_button.clicked.connect(self.acquire_dark_spectrum)
        # if button for "acquire reference spectrum" has been pressed
        self.ui.experiment_acquire_reference_spectrum_button.clicked.connect(self.acquire_reference_spectrum)
        # if button for "acquire transmission spectrum" has been pressed
        self.ui.experiment_acquire_transmission_spectrum_button.clicked.connect(self.acquire_transmission_spectrum)
        # if button for "acquire emission spectrum" has been pressed
        self.ui.experiment_acquire_emission_spectrum_button.clicked.connect(self.acquire_emission_spectrum)

        # Save experiment data
        self.main_experiment = Experiment()
        # if button for "export data" has been pressed
        self.ui.export_experiment_button.clicked.connect(lambda: self.export_experiment(self.main_experiment))
        # if button for "clear" has been pressed
        self.ui.clear_experiment_button.clicked.connect(self.clear_spectra)


        # Save data from individual plots
        # if button for ".png" has been pressed for raw_plot
        self.ui.save_raw_plot_png_button.clicked.connect(lambda: self.save_plot_png(plot_frame = self.ui.raw_plot_frame,  frame_name = 'Raw' ))
        # if button for ".txt" has been pressed for raw_plot
        self.ui.save_raw_plot_txt_button.clicked.connect(lambda: self.save_plot_txt(plot_name = ['Raw'],  plot_data = [self.raw_plot_line] ))

        # if button for ".png" has been pressed for calc_plot_1
        self.ui.save_calc_plot_1_png_button.clicked.connect(lambda: self.save_plot_png(plot_frame = self.ui.calc_plot_1_frame,  frame_name = self.ui.calc_plot_1_label.text() ))
        # if button for ".txt" has been pressed for calc_plot_1
        self.ui.save_calc_plot_1_txt_button.clicked.connect(lambda: self.save_plot_txt(plot_name = self.ui.calc_plot_1_label.text(),  plot_data = self.self.ui.calc_plot_1_line ))

        # if button for ".png" has been pressed for calc_plot_2
        self.ui.save_calc_plot_2_png_button.clicked.connect(lambda: self.save_plot_png(plot_frame = self.ui.calc_plot_2_frame,  frame_name = self.ui.calc_plot_2_label.text() ))
        # if button for ".txt" has been pressed for calc_plot_2
        self.ui.save_calc_plot_2_txt_button.clicked.connect(lambda: self.save_plot_txt(plot_name = self.ui.calc_plot_2_label.text(),  plot_data = self.self.ui.calc_plot_2_line ))


        # if button for ".png" has been pressed for calc_plot_3
        self.ui.save_calc_plot_3_png_button.clicked.connect(lambda: self.save_plot_png(plot_frame = self.ui.calc_plot_3_frame,  frame_name = self.ui.calc_plot_3_label.text() ))
        # if button for ".txt" has been pressed for calc_plot_3
        self.ui.save_calc_plot_3_txt_button.clicked.connect(lambda: self.save_plot_txt(plot_name = self.ui.calc_plot_3_label.text(),  plot_data = self.ui.calc_plot_3_line ))

        self.main_menu_switch()
        self.calibration_menu_switch()
        self.experiment_menu_switch()

    def main_menu_switch(self, choice = 'acquisition'):

        if(choice == 'acquisition'):
            self.ui.main_menu_tab.setCurrentIndex(0)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.image_label.show()
            self.ui.main_menu_calibration_tab.hide()
            self.ui.side_plots_frame.hide()

        elif(choice == 'calibration'):
            self.ui.main_menu_tab.setCurrentIndex(1)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.image_label.hide()
            self.ui.main_menu_calibration_tab.show()
            self.ui.side_plots_frame.show()
            self.clear_spectra()
            self.plot_acquisition_mode = 'calibration'

        elif(choice == 'experiment'):
            self.ui.main_menu_tab.setCurrentIndex(2)
            self.ui.acquisition_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.calibration_button.setStyleSheet("border-bottom-width: 0px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.experiment_button.setStyleSheet("border-bottom-width: 2px;background-color:#14274e; color:#f1f6f9; border-radius: 0px;border-style: solid;border-color: #f1f6f9;font-family: helvetica;")
            self.ui.image_label.hide()
            self.ui.main_menu_calibration_tab.show()
            self.ui.side_plots_frame.show()
            self.clear_spectra()
            self.plot_acquisition_mode = 'experiment'


    def experiment_menu_switch(self, choice = 'transmission'):
        self.experiment_choice = choice
        self.main_experiment.set_experiment_type(experiment_type = choice)

        if(choice == 'transmission'):
            self.clear_spectra()
            self.resetCheckBox()
            self.ui.experiment_acquire_dark_spectrum_button.show()
            self.ui.experiment_acquire_reference_spectrum_button.show()
            self.ui.experiment_acquire_transmission_spectrum_button.show()
            self.ui.experiment_acquire_emission_spectrum_button.hide()

            self.ui.experiment_no_1_label.show()
            self.ui.experiment_no_2_label.show()
            self.ui.experiment_no_3_label.show()

            self.ui.save_calc_plot_2_png_button.show()
            self.ui.save_calc_plot_2_txt_button.show()


            self.ui.experiment_check_label_1.show()
            self.ui.experiment_check_label_2.show()
            self.ui.experiment_check_label_3.show()


            self.update_plot(plot_line = self.calc_plot_1_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_1_combo_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_2_line, data = self.intensitiesReference)
            self.update_plot(plot_line = self.calc_plot_2_combo_line, data = self.intensitiesReference)
            self.update_plot(plot_line = self.calc_plot_3_line, data = self.intensitiesTransmission)


            self.ui.calc_plot_1_combo.show()
            self.ui.calc_plot_2_combo.show()
            self.ui.calc_plot_3.show()

            self.ui.calc_plot_1_combo_label.show()
            self.ui.calc_plot_1_combo_i_label.show()
            self.ui.calc_plot_2_combo_lambda_label.show()

            self.ui.calc_plot_2_combo_label.show()
            self.ui.calc_plot_2_combo_i_label.show()
            self.ui.calc_plot_2_combo_lambda_label.show()

            self.ui.calc_plot_3_label.show()
            self.ui.calc_plot_3_lambda_label.show()
            self.ui.calc_plot_3_i_label.show()

            self.ui.calc_plot_1_combo_label.setText("Dark")
            self.ui.calc_plot_2_combo_label.setText("Reference")
            self.ui.calc_plot_3_label.setText("Transmission")

            self.ui.experiment_menu_transmission_button.setStyleSheet("color: #24262b;border-bottom-width: 2px;border-color: #24262b;border-style:solid;")
            self.ui.experiment_menu_emission_button.setStyleSheet("color: #24262b;border-bottom-width: 0px;border-color: #24262b;border-style:solid;")

            self.main_experiment.set_plot_frames(plot_frames = [self.ui.raw_plot_frame,self.ui.calc_plot_1_2_combo_frame,self.ui.calc_plot_3_frame])
            self.main_experiment.set_frame_names(frame_names = ['Raw', 'DarkAndReference', 'Transmission'])
            self.main_experiment.set_plot_data(plot_names = ['Raw', 'Dark', 'Reference', 'Transmission'],
                                               plot_data = [self.raw_plot_line,self.calc_plot_1_line,self.calc_plot_2_line,self.calc_plot_3_line])

        elif(choice == 'emission'):
            self.clear_spectra()
            self.resetCheckBox()
            self.ui.experiment_acquire_dark_spectrum_button.show()
            self.ui.experiment_acquire_reference_spectrum_button.hide()
            self.ui.experiment_acquire_transmission_spectrum_button.hide()
            self.ui.experiment_acquire_emission_spectrum_button.show()

            self.ui.experiment_no_1_label.show()
            self.ui.experiment_no_2_label.show()
            self.ui.experiment_no_3_label.hide()

            self.ui.save_calc_plot_2_png_button.hide()
            self.ui.save_calc_plot_2_txt_button.hide()

            self.ui.experiment_check_label_1.show()
            self.ui.experiment_check_label_2.show()
            self.ui.experiment_check_label_3.hide()

            self.update_plot(plot_line = self.calc_plot_1_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_1_combo_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_3_line, data = self.intensitiesEmission)

            self.ui.calc_plot_1_combo.show()
            self.ui.calc_plot_2_combo.hide()
            self.ui.calc_plot_3.show()

            self.ui.calc_plot_1_combo_label.show()
            self.ui.calc_plot_2_combo_label.hide()
            self.ui.calc_plot_3_label.show()

            self.ui.calc_plot_2_combo_lambda_label.hide()
            self.ui.calc_plot_2_i_label.hide()

            self.ui.calc_plot_1_combo_label.setText("Dark")
            self.ui.calc_plot_3_label.setText("Emission")

            self.ui.experiment_menu_transmission_button.setStyleSheet("color: #24262b;border-bottom-width: 0px;border-color: #24262b;border-style:solid;")
            self.ui.experiment_menu_emission_button.setStyleSheet("color: #24262b;border-bottom-width: 2px;border-color: #24262b;border-style:solid;")

            self.main_experiment.set_plot_frames(plot_frames = [self.ui.raw_plot_frame,self.ui.calc_plot_1_2_combo_frame,self.ui.calc_plot_3_frame])
            self.main_experiment.set_frame_names(frame_names = ['Raw', 'Dark', 'Transmission'])
            self.main_experiment.set_plot_data(plot_names = ['Raw', 'Dark',  'Emission'],
                                               plot_data = [self.raw_plot_line,self.calc_plot_1_combo_line,self.calc_plot_3_line])



    def calibration_menu_switch(self, choice = 'pixel_wavelength'):
        self.calibration_choice = choice

        if(choice == 'pixel_wavelength'):
            self.pixel_wavelength_stage = 0
            self.calibration_start_pane()
            self.clear_spectra()
            self.resetCheckBox()
            self.ui.calibration_acquire_dark_spectrum_button.show()
            self.ui.calibration_acquire_reference_spectrum_button.show()
            self.ui.calibration_acquire_transmission_spectrum_button.show()
            self.ui.calibration_acquire_emission_spectrum_button.hide()

            self.ui.calibration_no_1_label.show()
            self.ui.calibration_no_2_label.show()
            self.ui.calibration_no_3_label.show()

            self.ui.save_calc_plot_2_png_button.show()
            self.ui.save_calc_plot_2_txt_button.show()

            self.ui.calibration_check_label_1.show()
            self.ui.calibration_check_label_2.show()
            self.ui.calibration_check_label_3.show()


            self.update_plot(plot_line = self.calc_plot_1_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_1_combo_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_2_line, data = self.intensitiesReference)
            self.update_plot(plot_line = self.calc_plot_2_combo_line, data = self.intensitiesReference)
            self.update_plot(plot_line = self.calc_plot_3_line, data = self.intensitiesTransmission)


            self.ui.calc_plot_1_combo.show()
            self.ui.calc_plot_2_combo.show()
            self.ui.calc_plot_3.show()

            self.ui.calc_plot_1_combo_label.show()
            self.ui.calc_plot_1_combo_i_label.show()
            self.ui.calc_plot_2_combo_lambda_label.show()

            self.ui.calc_plot_2_combo_label.show()
            self.ui.calc_plot_2_combo_i_label.show()
            self.ui.calc_plot_2_combo_lambda_label.show()

            self.ui.calc_plot_3_label.show()
            self.ui.calc_plot_3_lambda_label.show()
            self.ui.calc_plot_3_i_label.show()

            self.ui.calc_plot_1_combo_label.setText("Dark")
            self.ui.calc_plot_2_combo_label.setText("Reference")
            self.ui.calc_plot_3_label.setText("Transmission")

            self.ui.calibration_menu_pixel_wavelength_button.setStyleSheet("color: #24262b;border-bottom-width: 2px;border-color: #24262b;border-style:solid;")
            self.ui.calibration_menu_spectral_sensitivity_button.setStyleSheet("color: #24262b;border-bottom-width: 0px;border-color: #24262b;border-style:solid;")

        elif(choice == 'spectral_sensitivity'):
            self.spectral_sensitivity_stage = 0
            self.calibration_start_pane()

            self.ui.calibration_identify_peaks_frame.hide()
            self.ui.calibration_pixel_wavelength_polynomial_frame.hide()
            self.ui.calibration_back_button.hide()

            self.clear_spectra()
            self.resetCheckBox()
            self.ui.calibration_acquire_dark_spectrum_button.show()
            self.ui.calibration_acquire_reference_spectrum_button.show()
            self.ui.calibration_acquire_transmission_spectrum_button.show()
            self.ui.calibration_acquire_emission_spectrum_button.hide()

            self.ui.calibration_no_1_label.show()
            self.ui.calibration_no_2_label.show()
            self.ui.calibration_no_3_label.show()

            self.ui.save_calc_plot_2_png_button.show()
            self.ui.save_calc_plot_2_txt_button.show()

            self.ui.calibration_check_label_1.show()
            self.ui.calibration_check_label_2.show()
            self.ui.calibration_check_label_3.show()


            self.update_plot(plot_line = self.calc_plot_1_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_1_combo_line, data = self.intensitiesDark)
            self.update_plot(plot_line = self.calc_plot_2_line, data = self.intensitiesReference)
            self.update_plot(plot_line = self.calc_plot_2_combo_line, data = self.intensitiesReference)
            self.update_plot(plot_line = self.calc_plot_3_line, data = self.intensitiesTransmission)


            self.ui.calc_plot_1_combo.show()
            self.ui.calc_plot_2_combo.show()
            self.ui.calc_plot_3.show()

            self.ui.calc_plot_1_combo_label.show()
            self.ui.calc_plot_1_combo_i_label.show()
            self.ui.calc_plot_2_combo_lambda_label.show()

            self.ui.calc_plot_2_combo_label.show()
            self.ui.calc_plot_2_combo_i_label.show()
            self.ui.calc_plot_2_combo_lambda_label.show()

            self.ui.calc_plot_3_label.show()
            self.ui.calc_plot_3_lambda_label.show()
            self.ui.calc_plot_3_i_label.show()

            self.ui.calc_plot_1_combo_label.setText("Dark")
            self.ui.calc_plot_2_combo_label.setText("Reference")
            self.ui.calc_plot_3_label.setText("Transmission")

            self.ui.calibration_menu_pixel_wavelength_button.setStyleSheet("color: #24262b;border-bottom-width: 0px;border-color: #24262b;border-style:solid;")
            self.ui.calibration_menu_spectral_sensitivity_button.setStyleSheet("color: #24262b;border-bottom-width: 2px;border-color: #24262b;border-style:solid;")


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

    def set_wavelengths(self):
        if(self.pixel_wavelength_calibrated == True):
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


    def cursor_in_raw_plot(self,evt):
        mousePoint = self.vb_raw.mapSceneToView(evt)
        self.ui.cursor_raw_label.setText("x: {}, y: {}".format(round(mousePoint.x(),1), round(mousePoint.y(),1)))

    def cursor_in_calc_plot_3(self,evt):
        mousePoint = self.vb_calc_3.mapSceneToView(evt)
        self.ui.cursor_calc_3_label.setText("x: {}, y: {}".format(round(mousePoint.x(),1), round(mousePoint.y(),1)))

    def setup_plots(self):
        self.raw_plot_line, self.vb_raw = self.setup_plot(self.ui.raw_plot)
        self.calc_plot_1_line, self.vb_calc_1 = self.setup_plot(self.ui.calc_plot_1)
        self.calc_plot_1_combo_line, self.vb_calc_1_combo  = self.setup_plot(self.ui.calc_plot_1_combo)
        self.calc_plot_2_line, self.vb_calc_2  = self.setup_plot(self.ui.calc_plot_2)
        self.calc_plot_2_combo_line, self.vb_calc_2_combo  = self.setup_plot(self.ui.calc_plot_2_combo)
        self.calc_plot_3_line, self.vb_calc_3  = self.setup_plot(self.ui.calc_plot_3)

    # checks relevant checkbox to show user that a spectrum has been stored
    def setCheckBox(self, specCheck):
        check_path = os.path.join('gui_images', "green_check.png")
        if(self.plot_acquisition_mode == 'experiment'):
            if(specCheck == 0):
                self.ui.experiment_check_label_1.setPixmap(QtGui.QPixmap(check_path))
            elif(specCheck == 1):
                self.ui.experiment_check_label_2.setPixmap(QtGui.QPixmap(check_path))
            elif(specCheck == 2):
                self.ui.experiment_check_label_3.setPixmap(QtGui.QPixmap(check_path))
        elif(self.plot_acquisition_mode == 'calibration'):
            if(specCheck == 0):
                self.ui.calibration_check_label_1.setPixmap(QtGui.QPixmap(check_path))
            elif(specCheck == 1):
                self.ui.calibration_check_label_2.setPixmap(QtGui.QPixmap(check_path))
            elif(specCheck == 2):
                self.ui.calibration_check_label_3.setPixmap(QtGui.QPixmap(check_path))

    def resetCheckBox(self):
        if(self.plot_acquisition_mode == 'experiment'):
            self.ui.experiment_check_label_1.clear()
            self.ui.experiment_check_label_2.clear()
            self.ui.experiment_check_label_3.clear()
        elif(self.plot_acquisition_mode == 'calibration'):
            self.ui.calibration_check_label_1.clear()
            self.ui.calibration_check_label_2.clear()
            self.ui.calibration_check_label_3.clear()


    def setup_plot(self, plot_item = ''):
        plot_item.clear()
        pen = pg.mkPen(color="#14274e", width=1, style=QtCore.Qt.SolidLine)
        plot_line = plot_item.plot(self.waves,np.zeros(len(self.waves)), pen=pen)
        plot_item.setBackground('w')
        #self.ui.calc_plot_3.setYRange(0, 255*01.3*self.no_of_lines, padding=0)
        #plot_item.setXRange(300,700, padding=0.1)
        vb = plot_item.getViewBox()
        vb.setBackgroundColor("#f1f6f9")
        vb.setBorder(color="#8d93ab", width=1, style=QtCore.Qt.SolidLine)
        return plot_line, vb


    # update spectrum plot
    def update_plot(self, plot_line = '', data = ''):
        plot_line.setData(self.waves,data)

    def clear_spectra(self):
        self.setup_plots()
        self.resetCheckBox()
        self.unpause_acquisition()


    def export_calibration(self):
        save_calibration_path  = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.update_settings_config_parser()
        self.calibration.set_acquisition_settings(config = self.config)
        self.calibration.set_save_path(save_path = save_calibration_path)
        self.calibration.save()

    def export_experiment(self, experiment = ''):
        save_images_path  = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.update_settings_config_parser()
        experiment.set_acquisition_settings(config = self.config)
        experiment.set_save_path(save_path = save_images_path)
        experiment.save()




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
