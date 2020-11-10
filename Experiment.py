
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

class Experiment:
  def __init__(self):
      self.experiment_type = ''
      self.plot_data = np.array([])
      self.plot_frames = []
      self.frame_names = []
      self.plot_names  = []
      self.save_path = ''
      self.save_images_path = ''
      self.save_data_path = ''


      self.experiment_type_set = False
      self.plot_frames_set = False
      self.plot_data_set = False

  def set_experiment_type(self, experiment_type):
      self.experiment_type = experiment_type
      self.experiment_type_set = True

  def set_plot_data(self, plot_names = [],plot_data = ''):
      self.plot_data = plot_data
      self.plot_names = plot_names
      self.plot_data_set = True

  def set_plot_frames(self, plot_frames = []):
      self.plot_frames = plot_frames
      self.plot_frames_set = True

  def set_frame_names(self, frame_names = []):
      self.frame_names = frame_names

  def set_acquisition_settings(self, config = ''):
      self.config = config

  def set_save_path(self, save_path = ''):
      self.save_path = save_path
      self.save_images_path = save_path
      self.save_data_path = save_path

  def set_data_types(self, data_types = []):
      self.data_types = data_types

  def save(self):

      if(self.plot_frames_set and self.plot_data_set):
          self._make_experiment_catalogs()
          self._save_images()
          self._save_data()
          self._save_acquisition_settings()

      elif(self.plot_frames_set):
          self._save_images()

      elif(self.plot_data_set):
          self._save_data(self.data_types)


  def _save_images(self):
      cntr = 0
      for frame in self.plot_frames:
          img = frame.grab()
          img.save(os.path.join(self.save_images_path, self.frame_names[cntr] + ".png"))
          cntr = cntr + 1

  def _save_data(self, data_type = ['csv','mat','xls','txt']):
      if('csv' in data_type):
          self._export_data_csv()

      if('mat' in data_type):
          self._export_data_mat()

      if('xls' in data_type):
          self._export_data_excel()

      if('txt' in data_type):
          self._export_data_txt()


  def _export_data_csv(self):
      save_csv_path = os.path.join(self.save_data_path, 'experiment_data.csv')
      time_stamp = datetime.now().strftime("%y%m%d-%H%M")

      data = np.array([])
      data_header = 'Timestamp:' + time_stamp
      cntr = 0
      first = True
      for row in self.plot_data:
          if(first):
              data_header = data_header + 'Row 1: Wavelengths (nm), Row 2: {}, '.format(self.plot_names[cntr])
              data = [row.getData()[0],
                      row.getData()[1]]
              first = False
          else:
              np.vstack([data, row.getData()[1]])
              data_header = data_header + 'Row {}: {}, '.format(str(cntr+2), self.plot_names[cntr])
          cntr = cntr + 1
      np.savetxt(save_csv_path, data, fmt='%.2f', delimiter=',', header=data_header)


  def _export_data_mat(self):
      save_mat_path = os.path.join(self.save_data_path, 'experiment_data.mat')
      dict = {}
      cntr = 0
      first = True
      for row in self.plot_data:
          if(first):
              dict['Wavelengths'] = row.getData()[0]
              dict[self.plot_names[cntr]] = row.getData()[1]
              first = True
          else:
              dict[self.plot_names[cntr]] = row.getData()[1]
          cntr = cntr + 1
      sio.savemat(save_mat_path, dict)


  def _export_data_excel(self):
      save_xls_path = os.path.join(self.save_data_path, 'experiment_data.xls')

      df = DataFrame({})
      cntr = 0
      first = True
      for row in self.plot_data:
          if(first):
              df = DataFrame({'Wavelengths (nm)': row.getData()[0]})
              df.append(DataFrame({self.plot_names[cntr]: row.getData()[1]}), sort=True)
              first = True
          else:
              df.append(DataFrame({self.plot_names[cntr]: row.getData()[1]}), sort=True)
          cntr = cntr + 1
          df.to_excel(save_xls_path, sheet_name='sheet1', index=False)



  def _export_data_txt(self):
      save_txt_path = os.path.join(self.save_data_path, 'experiment_data.txt')
      time_stamp = datetime.now().strftime("%y%m%d-%H%M")

      data = np.array([])
      data_header = 'Timestamp:' + time_stamp
      cntr = 0
      first = True
      for row in self.plot_data:
          if(first):
              data_header = data_header + 'Row 1: Wavelengths (nm), Row 2: {}, '.format(self.plot_names[cntr])
              data = [row.getData()[0],
                      row.getData()[1]]
              first = False
          else:
              np.vstack([data, row.getData()[1]])
              data_header = data_header + 'Row {}: {}, '.format(str(cntr+2), self.plot_names[cntr])
          cntr = cntr + 1
      np.savetxt(save_txt_path, data, fmt='%.2f', delimiter=',', header=data_header)

  def _save_acquisition_settings(self):
      self.save_acquisition_settings_path = os.path.join(self.save_settings_path, 'settings.txt')
      try:
          with open(self.save_acquisition_settings_path, 'w') as configfile:
              self.config.write(configfile)
              print('Successfully saved settings')
      except:
              print('Error saving to config file')

  def _make_experiment_catalogs(self):
      # Make folders for experiment
      timestamp = datetime.now().strftime("%y%m%d-%H%M")
      folder_name = timestamp + '_' + self.experiment_type
      self.save_path = os.path.join(self.save_path, folder_name)
      os.makedirs(self.save_path)
      self.save_images_path = os.path.join(self.save_path, 'images')
      os.makedirs(self.save_images_path)
      self.save_data_path = os.path.join(self.save_path, 'data')
      os.makedirs(self.save_data_path)
      self.save_settings_path = os.path.join(self.save_path, 'settings')
      os.makedirs(self.save_settings_path)
