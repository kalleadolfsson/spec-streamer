# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1327, 850)
        Form.setStyleSheet("background-color: white")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(699, 142, 541, 311))
        self.image_label.setMaximumSize(QtCore.QSize(800, 16777215))
        self.image_label.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.spec_plot = MplPlot(Form)
        self.spec_plot.setGeometry(QtCore.QRect(643, 480, 650, 350))
        self.spec_plot.setObjectName("spec_plot")
        self.calc_plot = MplPlot(Form)
        self.calc_plot.setEnabled(False)
        self.calc_plot.setGeometry(QtCore.QRect(642, 110, 650, 350))
        self.calc_plot.setObjectName("calc_plot")
        self.junkyard_photonics_label = QtWidgets.QLabel(Form)
        self.junkyard_photonics_label.setGeometry(QtCore.QRect(1190, -1, 141, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.junkyard_photonics_label.setFont(font)
        self.junkyard_photonics_label.setStyleSheet("background-color:white;\n"
"font-family: helvetica;\n"
"color:#14274e;")
        self.junkyard_photonics_label.setOpenExternalLinks(True)
        self.junkyard_photonics_label.setObjectName("junkyard_photonics_label")
        self.tab_container = QtWidgets.QTabWidget(Form)
        self.tab_container.setEnabled(True)
        self.tab_container.setGeometry(QtCore.QRect(20, 70, 591, 761))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tab_container.setPalette(palette)
        self.tab_container.setAutoFillBackground(False)
        self.tab_container.setStyleSheet("background-color: white;\n"
"margin: 0px;\n"
"padding:0px;\n"
"border: 0px;")
        self.tab_container.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_container.setTabBarAutoHide(True)
        self.tab_container.setObjectName("tab_container")
        self.acquisition_containerPage1 = QtWidgets.QWidget()
        self.acquisition_containerPage1.setObjectName("acquisition_containerPage1")
        self.image_scale_cropped_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.image_scale_cropped_label.setGeometry(QtCore.QRect(350, 117, 121, 20))
        self.image_scale_cropped_label.setStyleSheet("color: #24262b;")
        self.image_scale_cropped_label.setObjectName("image_scale_cropped_label")
        self.detector_width_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.detector_width_input.setGeometry(QtCore.QRect(136, 170, 41, 21))
        self.detector_width_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_width_input.setObjectName("detector_width_input")
        self.image_crop_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.image_crop_label.setGeometry(QtCore.QRect(355, 143, 121, 20))
        self.image_crop_label.setStyleSheet("color: #24262b;")
        self.image_crop_label.setObjectName("image_crop_label")
        self.detector_resolution_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.detector_resolution_label.setGeometry(QtCore.QRect(22, 170, 111, 20))
        self.detector_resolution_label.setStyleSheet("color: #24262b;")
        self.detector_resolution_label.setObjectName("detector_resolution_label")
        self.image_camera_no_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.image_camera_no_input.setGeometry(QtCore.QRect(469, 171, 51, 21))
        self.image_camera_no_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_camera_no_input.setObjectName("image_camera_no_input")
        self.x_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.x_label.setGeometry(QtCore.QRect(181, 169, 16, 20))
        self.x_label.setStyleSheet("color: #24262b;")
        self.x_label.setObjectName("x_label")
        self.spectrum_rotation_global_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrum_rotation_global_input.setGeometry(QtCore.QRect(184, 264, 51, 21))
        self.spectrum_rotation_global_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_global_input.setObjectName("spectrum_rotation_global_input")
        self.detector_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.detector_frame.setGeometry(QtCore.QRect(16, 77, 251, 141))
        self.detector_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.detector_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detector_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detector_frame.setObjectName("detector_frame")
        self.spectrometer_name_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrometer_name_input.setGeometry(QtCore.QRect(346, 265, 181, 21))
        self.spectrometer_name_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrometer_name_input.setObjectName("spectrometer_name_input")
        self.spectrum_stop_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_stop_label.setGeometry(QtCore.QRect(101, 345, 81, 16))
        self.spectrum_stop_label.setStyleSheet("color: #24262b;")
        self.spectrum_stop_label.setObjectName("spectrum_stop_label")
        self.load_acquisition_settings_button = QtWidgets.QPushButton(self.acquisition_containerPage1)
        self.load_acquisition_settings_button.setGeometry(QtCore.QRect(17, 35, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.load_acquisition_settings_button.setFont(font)
        self.load_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.load_acquisition_settings_button.setObjectName("load_acquisition_settings_button")
        self.image_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.image_frame.setGeometry(QtCore.QRect(310, 77, 251, 141))
        self.image_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image_settings_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.image_settings_label.setGeometry(QtCore.QRect(400, 69, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.image_settings_label.setFont(font)
        self.image_settings_label.setStyleSheet("color: #24262b;")
        self.image_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_settings_label.setObjectName("image_settings_label")
        self.spectrum_line_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_line_label.setGeometry(QtCore.QRect(104, 369, 81, 20))
        self.spectrum_line_label.setStyleSheet("color: #24262b;")
        self.spectrum_line_label.setObjectName("spectrum_line_label")
        self.spectrum_rotation_global_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_rotation_global_label.setGeometry(QtCore.QRect(83, 265, 101, 20))
        self.spectrum_rotation_global_label.setStyleSheet("color: #24262b;")
        self.spectrum_rotation_global_label.setObjectName("spectrum_rotation_global_label")
        self.detector_integration_time_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.detector_integration_time_label.setGeometry(QtCore.QRect(46, 94, 131, 16))
        self.detector_integration_time_label.setStyleSheet("color: #24262b;")
        self.detector_integration_time_label.setObjectName("detector_integration_time_label")
        self.detector_gain_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.detector_gain_input.setGeometry(QtCore.QRect(184, 143, 51, 21))
        self.detector_gain_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_gain_input.setObjectName("detector_gain_input")
        self.spectrum_settings_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_settings_label.setGeometry(QtCore.QRect(84, 245, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrum_settings_label.setFont(font)
        self.spectrum_settings_label.setStyleSheet("color: #24262b;")
        self.spectrum_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spectrum_settings_label.setObjectName("spectrum_settings_label")
        self.spectrum_start_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrum_start_input.setGeometry(QtCore.QRect(183, 317, 51, 21))
        self.spectrum_start_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_start_input.setObjectName("spectrum_start_input")
        self.spectrometer_name_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrometer_name_label.setGeometry(QtCore.QRect(370, 244, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrometer_name_label.setFont(font)
        self.spectrometer_name_label.setStyleSheet("color: #24262b;")
        self.spectrometer_name_label.setObjectName("spectrometer_name_label")
        self.detector_height_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.detector_height_input.setGeometry(QtCore.QRect(193, 170, 41, 21))
        self.detector_height_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_height_input.setObjectName("detector_height_input")
        self.detector_gain_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.detector_gain_label.setGeometry(QtCore.QRect(97, 144, 81, 20))
        self.detector_gain_label.setStyleSheet("color: #24262b;")
        self.detector_gain_label.setObjectName("detector_gain_label")
        self.detector_settings_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.detector_settings_label.setGeometry(QtCore.QRect(103, 69, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label.setFont(font)
        self.detector_settings_label.setStyleSheet("color: #24262b;")
        self.detector_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label.setObjectName("detector_settings_label")
        self.spectrum_stop_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrum_stop_input.setGeometry(QtCore.QRect(182, 343, 51, 21))
        self.spectrum_stop_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_stop_input.setObjectName("spectrum_stop_input")
        self.image_scale_overview_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.image_scale_overview_input.setGeometry(QtCore.QRect(470, 91, 51, 21))
        self.image_scale_overview_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_scale_overview_input.setObjectName("image_scale_overview_input")
        self.image_scale_overview_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.image_scale_overview_label.setGeometry(QtCore.QRect(346, 92, 121, 20))
        self.image_scale_overview_label.setStyleSheet("color: #24262b;")
        self.image_scale_overview_label.setObjectName("image_scale_overview_label")
        self.save_acquisition_settings_button = QtWidgets.QPushButton(self.acquisition_containerPage1)
        self.save_acquisition_settings_button.setGeometry(QtCore.QRect(89, 35, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_acquisition_settings_button.setFont(font)
        self.save_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_acquisition_settings_button.setObjectName("save_acquisition_settings_button")
        self.image_crop_box = QtWidgets.QCheckBox(self.acquisition_containerPage1)
        self.image_crop_box.setEnabled(True)
        self.image_crop_box.setGeometry(QtCore.QRect(470, 144, 31, 20))
        self.image_crop_box.setText("")
        self.image_crop_box.setCheckable(True)
        self.image_crop_box.setChecked(False)
        self.image_crop_box.setObjectName("image_crop_box")
        self.spectrometer_name_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.spectrometer_name_frame.setGeometry(QtCore.QRect(310, 254, 251, 51))
        self.spectrometer_name_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.spectrometer_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrometer_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrometer_name_frame.setObjectName("spectrometer_name_frame")
        self.apply_acquisition_settings_button = QtWidgets.QPushButton(self.acquisition_containerPage1)
        self.apply_acquisition_settings_button.setGeometry(QtCore.QRect(310, 335, 131, 41))
        self.apply_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.apply_acquisition_settings_button.setObjectName("apply_acquisition_settings_button")
        self.spectrum_line_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrum_line_input.setGeometry(QtCore.QRect(182, 369, 51, 21))
        self.spectrum_line_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_line_input.setObjectName("spectrum_line_input")
        self.spectrum_rotation_spectrum_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_rotation_spectrum_label.setGeometry(QtCore.QRect(62, 291, 121, 20))
        self.spectrum_rotation_spectrum_label.setStyleSheet("color: #24262b;")
        self.spectrum_rotation_spectrum_label.setObjectName("spectrum_rotation_spectrum_label")
        self.detector_averages_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.detector_averages_label.setGeometry(QtCore.QRect(114, 119, 60, 16))
        self.detector_averages_label.setStyleSheet("color: #24262b;")
        self.detector_averages_label.setObjectName("detector_averages_label")
        self.spectrum_rotation_spectrum_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrum_rotation_spectrum_input.setGeometry(QtCore.QRect(183, 290, 51, 21))
        self.spectrum_rotation_spectrum_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_spectrum_input.setObjectName("spectrum_rotation_spectrum_input")
        self.spectrum_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.spectrum_frame.setGeometry(QtCore.QRect(17, 254, 251, 171))
        self.spectrum_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.spectrum_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrum_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrum_frame.setObjectName("spectrum_frame")
        self.live_button = QtWidgets.QPushButton(self.acquisition_containerPage1)
        self.live_button.setGeometry(QtCore.QRect(460, 334, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.live_button.setFont(font)
        self.live_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.live_button.setObjectName("live_button")
        self.image_scale_cropped_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.image_scale_cropped_input.setGeometry(QtCore.QRect(470, 118, 51, 21))
        self.image_scale_cropped_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_scale_cropped_input.setObjectName("image_scale_cropped_input")
        self.spectrum_start_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_start_label.setGeometry(QtCore.QRect(101, 317, 81, 20))
        self.spectrum_start_label.setStyleSheet("color: #24262b;")
        self.spectrum_start_label.setObjectName("spectrum_start_label")
        self.spectrum_lines_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_lines_label.setGeometry(QtCore.QRect(109, 394, 71, 20))
        self.spectrum_lines_label.setStyleSheet("color: #24262b;")
        self.spectrum_lines_label.setObjectName("spectrum_lines_label")
        self.spectrum_lines_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.spectrum_lines_input.setGeometry(QtCore.QRect(182, 394, 51, 21))
        self.spectrum_lines_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_lines_input.setObjectName("spectrum_lines_input")
        self.image_camera_no_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.image_camera_no_label.setGeometry(QtCore.QRect(401, 173, 71, 16))
        self.image_camera_no_label.setStyleSheet("color: #24262b;")
        self.image_camera_no_label.setObjectName("image_camera_no_label")
        self.detector_integration_time_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.detector_integration_time_input.setGeometry(QtCore.QRect(184, 91, 51, 21))
        self.detector_integration_time_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_integration_time_input.setObjectName("detector_integration_time_input")
        self.detector_averages_input = QtWidgets.QLineEdit(self.acquisition_containerPage1)
        self.detector_averages_input.setGeometry(QtCore.QRect(184, 117, 51, 21))
        self.detector_averages_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_averages_input.setObjectName("detector_averages_input")
        self.spectrometer_name_frame.raise_()
        self.spectrum_frame.raise_()
        self.detector_frame.raise_()
        self.image_frame.raise_()
        self.image_scale_cropped_label.raise_()
        self.detector_width_input.raise_()
        self.image_crop_label.raise_()
        self.detector_resolution_label.raise_()
        self.image_camera_no_input.raise_()
        self.x_label.raise_()
        self.spectrum_rotation_global_input.raise_()
        self.spectrometer_name_input.raise_()
        self.spectrum_stop_label.raise_()
        self.load_acquisition_settings_button.raise_()
        self.image_settings_label.raise_()
        self.spectrum_line_label.raise_()
        self.spectrum_rotation_global_label.raise_()
        self.detector_integration_time_label.raise_()
        self.detector_gain_input.raise_()
        self.spectrum_settings_label.raise_()
        self.spectrum_start_input.raise_()
        self.spectrometer_name_label.raise_()
        self.detector_height_input.raise_()
        self.detector_gain_label.raise_()
        self.detector_settings_label.raise_()
        self.spectrum_stop_input.raise_()
        self.image_scale_overview_input.raise_()
        self.image_scale_overview_label.raise_()
        self.save_acquisition_settings_button.raise_()
        self.image_crop_box.raise_()
        self.apply_acquisition_settings_button.raise_()
        self.spectrum_line_input.raise_()
        self.spectrum_rotation_spectrum_label.raise_()
        self.detector_averages_label.raise_()
        self.spectrum_rotation_spectrum_input.raise_()
        self.live_button.raise_()
        self.image_scale_cropped_input.raise_()
        self.spectrum_start_label.raise_()
        self.spectrum_lines_label.raise_()
        self.spectrum_lines_input.raise_()
        self.image_camera_no_label.raise_()
        self.detector_integration_time_input.raise_()
        self.detector_averages_input.raise_()
        self.tab_container.addTab(self.acquisition_containerPage1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_container.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.reference_button = QtWidgets.QPushButton(self.tab)
        self.reference_button.setGeometry(QtCore.QRect(90, 169, 171, 31))
        self.reference_button.setStyleSheet("background-color:#8d93ab;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.reference_button.setObjectName("reference_button")
        self.sample_ok = QtWidgets.QCheckBox(self.tab)
        self.sample_ok.setEnabled(False)
        self.sample_ok.setGeometry(QtCore.QRect(270, 234, 31, 20))
        self.sample_ok.setText("")
        self.sample_ok.setCheckable(True)
        self.sample_ok.setObjectName("sample_ok")
        self.reference_ok = QtWidgets.QCheckBox(self.tab)
        self.reference_ok.setEnabled(False)
        self.reference_ok.setGeometry(QtCore.QRect(270, 174, 31, 20))
        self.reference_ok.setText("")
        self.reference_ok.setCheckable(True)
        self.reference_ok.setObjectName("reference_ok")
        self.sample_button = QtWidgets.QPushButton(self.tab)
        self.sample_button.setGeometry(QtCore.QRect(90, 227, 171, 31))
        self.sample_button.setStyleSheet("background-color:#8d93ab;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.sample_button.setObjectName("sample_button")
        self.dark_ok = QtWidgets.QCheckBox(self.tab)
        self.dark_ok.setEnabled(False)
        self.dark_ok.setGeometry(QtCore.QRect(270, 112, 31, 20))
        self.dark_ok.setText("")
        self.dark_ok.setCheckable(True)
        self.dark_ok.setObjectName("dark_ok")
        self.dark_button = QtWidgets.QPushButton(self.tab)
        self.dark_button.setGeometry(QtCore.QRect(90, 108, 171, 31))
        self.dark_button.setStyleSheet("background-color:#8d93ab;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.dark_button.setObjectName("dark_button")
        self.detector_settings_label_3 = QtWidgets.QLabel(self.tab)
        self.detector_settings_label_3.setGeometry(QtCore.QRect(47, 108, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label_3.setFont(font)
        self.detector_settings_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label_3.setObjectName("detector_settings_label_3")
        self.detector_settings_label_4 = QtWidgets.QLabel(self.tab)
        self.detector_settings_label_4.setGeometry(QtCore.QRect(47, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label_4.setFont(font)
        self.detector_settings_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label_4.setObjectName("detector_settings_label_4")
        self.detector_settings_label_5 = QtWidgets.QLabel(self.tab)
        self.detector_settings_label_5.setGeometry(QtCore.QRect(47, 227, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label_5.setFont(font)
        self.detector_settings_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label_5.setObjectName("detector_settings_label_5")
        self.transmission_label = QtWidgets.QLabel(self.tab)
        self.transmission_label.setGeometry(QtCore.QRect(222, 70, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.transmission_label.setFont(font)
        self.transmission_label.setAlignment(QtCore.Qt.AlignCenter)
        self.transmission_label.setObjectName("transmission_label")
        self.fluorescence_label = QtWidgets.QLabel(self.tab)
        self.fluorescence_label.setGeometry(QtCore.QRect(220, 380, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fluorescence_label.setFont(font)
        self.fluorescence_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fluorescence_label.setObjectName("fluorescence_label")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setGeometry(QtCore.QRect(20, 80, 541, 221))
        self.frame_5.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setGeometry(QtCore.QRect(20, 390, 541, 221))
        self.frame_6.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.raise_()
        self.frame_5.raise_()
        self.reference_button.raise_()
        self.sample_ok.raise_()
        self.reference_ok.raise_()
        self.sample_button.raise_()
        self.dark_ok.raise_()
        self.dark_button.raise_()
        self.detector_settings_label_3.raise_()
        self.detector_settings_label_4.raise_()
        self.detector_settings_label_5.raise_()
        self.transmission_label.raise_()
        self.fluorescence_label.raise_()
        self.tab_container.addTab(self.tab, "")
        self.experiment_button = QtWidgets.QPushButton(Form)
        self.experiment_button.setGeometry(QtCore.QRect(740, 66, 140, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_button.setFont(font)
        self.experiment_button.setStyleSheet("background-color:#14274e;\n"
"color:#f1f6f9;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-bottom-width: 0px;\n"
"border-color: #f1f6f9;\n"
"font-family: helvetica;\n"
"\n"
"")
        self.experiment_button.setObjectName("experiment_button")
        self.calibration_button = QtWidgets.QPushButton(Form)
        self.calibration_button.setGeometry(QtCore.QRect(583, 66, 140, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_button.setFont(font)
        self.calibration_button.setStyleSheet("background-color:#14274e;\n"
"color:#f1f6f9;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-bottom-width: 0px;\n"
"border-color: #f1f6f9;\n"
"font-family: helvetica;\n"
"")
        self.calibration_button.setObjectName("calibration_button")
        self.acquisition_button = QtWidgets.QPushButton(Form)
        self.acquisition_button.setGeometry(QtCore.QRect(450, 66, 100, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.acquisition_button.setFont(font)
        self.acquisition_button.setStyleSheet("background-color:#14274e;\n"
"color:#f1f6f9;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-bottom-width: 2px;\n"
"border-color: #f1f6f9;\n"
"font-family: helvetica;\n"
"")
        self.acquisition_button.setObjectName("acquisition_button")
        self.spectrometer_name_frame_3 = QtWidgets.QFrame(Form)
        self.spectrometer_name_frame_3.setGeometry(QtCore.QRect(0, 19, 1331, 91))
        self.spectrometer_name_frame_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #9ba4b4;\n"
"background-color:#14274e")
        self.spectrometer_name_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrometer_name_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrometer_name_frame_3.setObjectName("spectrometer_name_frame_3")
        self.spec_mate_label = QtWidgets.QLabel(Form)
        self.spec_mate_label.setGeometry(QtCore.QRect(553, 21, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.spec_mate_label.setFont(font)
        self.spec_mate_label.setAutoFillBackground(False)
        self.spec_mate_label.setStyleSheet("color:#f1f6f9;\n"
"border-width:0px;\n"
"background-color: #14274e")
        self.spec_mate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spec_mate_label.setObjectName("spec_mate_label")
        self.junkyard_photonics__label_2 = QtWidgets.QLabel(Form)
        self.junkyard_photonics__label_2.setGeometry(QtCore.QRect(715, 26, 31, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.junkyard_photonics__label_2.setFont(font)
        self.junkyard_photonics__label_2.setStyleSheet("background-color:#14274e;\n"
"font-family: helvetica;\n"
"color:#9ba4b4;")
        self.junkyard_photonics__label_2.setObjectName("junkyard_photonics__label_2")
        self.tab_container.raise_()
        self.spectrometer_name_frame_3.raise_()
        self.calc_plot.raise_()
        self.image_label.raise_()
        self.spec_plot.raise_()
        self.junkyard_photonics_label.raise_()
        self.experiment_button.raise_()
        self.calibration_button.raise_()
        self.acquisition_button.raise_()
        self.spec_mate_label.raise_()
        self.junkyard_photonics__label_2.raise_()

        self.retranslateUi(Form)
        self.tab_container.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "spec-tool // Open source spectral analysis"))
        self.junkyard_photonics_label.setText(_translate("Form", "by junkyard-photonics"))
        self.image_scale_cropped_label.setText(_translate("Form", "Scale cropped (%):"))
        self.detector_width_input.setText(_translate("Form", "1280"))
        self.image_crop_label.setText(_translate("Form", "Crop to spectrum:"))
        self.detector_resolution_label.setText(_translate("Form", "Resolution (WxH):"))
        self.image_camera_no_input.setText(_translate("Form", "0"))
        self.x_label.setText(_translate("Form", "x"))
        self.spectrum_rotation_global_input.setText(_translate("Form", "0"))
        self.spectrometer_name_input.setText(_translate("Form", "ELP"))
        self.spectrum_stop_label.setText(_translate("Form", "Stop (x-val):"))
        self.load_acquisition_settings_button.setText(_translate("Form", "Load"))
        self.image_settings_label.setText(_translate("Form", "Image"))
        self.spectrum_line_label.setText(_translate("Form", "Line (y-val):"))
        self.spectrum_rotation_global_label.setText(_translate("Form", "Rotation global:"))
        self.detector_integration_time_label.setText(_translate("Form", "Integration time (ms):"))
        self.detector_gain_input.setText(_translate("Form", "20"))
        self.spectrum_settings_label.setText(_translate("Form", "Spectrum config"))
        self.spectrum_start_input.setText(_translate("Form", "750"))
        self.spectrometer_name_label.setText(_translate("Form", "Spectrometer name"))
        self.detector_height_input.setText(_translate("Form", "1024"))
        self.detector_gain_label.setText(_translate("Form", "Gain (0-100):"))
        self.detector_settings_label.setText(_translate("Form", "Detector"))
        self.spectrum_stop_input.setText(_translate("Form", "1230"))
        self.image_scale_overview_input.setText(_translate("Form", "40"))
        self.image_scale_overview_label.setText(_translate("Form", "Scale overview (%):"))
        self.save_acquisition_settings_button.setText(_translate("Form", "Save"))
        self.apply_acquisition_settings_button.setText(_translate("Form", "Apply settings"))
        self.spectrum_line_input.setText(_translate("Form", "500"))
        self.spectrum_rotation_spectrum_label.setText(_translate("Form", "Rotation spectrum:"))
        self.detector_averages_label.setText(_translate("Form", "Averages:"))
        self.spectrum_rotation_spectrum_input.setText(_translate("Form", "0"))
        self.live_button.setText(_translate("Form", "Live"))
        self.image_scale_cropped_input.setText(_translate("Form", "150"))
        self.spectrum_start_label.setText(_translate("Form", "Start (x-val):"))
        self.spectrum_lines_label.setText(_translate("Form", "No of lines:"))
        self.spectrum_lines_input.setText(_translate("Form", "5"))
        self.image_camera_no_label.setText(_translate("Form", "Camera #:"))
        self.detector_integration_time_input.setText(_translate("Form", "20"))
        self.detector_averages_input.setText(_translate("Form", "5"))
        self.tab_container.setTabText(self.tab_container.indexOf(self.tab_2), _translate("Form", "Page"))
        self.reference_button.setText(_translate("Form", "Reference spectrum"))
        self.sample_button.setText(_translate("Form", "Sample spectrum"))
        self.dark_button.setText(_translate("Form", "Dark spectrum"))
        self.detector_settings_label_3.setText(_translate("Form", "1."))
        self.detector_settings_label_4.setText(_translate("Form", "2."))
        self.detector_settings_label_5.setText(_translate("Form", "3."))
        self.transmission_label.setText(_translate("Form", "Transmission"))
        self.fluorescence_label.setText(_translate("Form", "Fluorescence"))
        self.experiment_button.setText(_translate("Form", "Experiment"))
        self.calibration_button.setText(_translate("Form", "Calibration"))
        self.acquisition_button.setText(_translate("Form", "Acquisition"))
        self.spec_mate_label.setText(_translate("Form", "spec-tool"))
        self.junkyard_photonics__label_2.setText(_translate("Form", "v1.0"))


from mplplot import MplPlot


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
