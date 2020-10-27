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
        Form.resize(1329, 849)
        Form.setStyleSheet("background-color: white")
        self.junkyard_photonics_label = QtWidgets.QLabel(Form)
        self.junkyard_photonics_label.setGeometry(QtCore.QRect(1189, -1, 141, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.junkyard_photonics_label.setFont(font)
        self.junkyard_photonics_label.setStyleSheet("background-color:white;\n"
"font-family: helvetica;\n"
"color:#14274e;")
        self.junkyard_photonics_label.setOpenExternalLinks(True)
        self.junkyard_photonics_label.setObjectName("junkyard_photonics_label")
        self.main_menu_tab = QtWidgets.QTabWidget(Form)
        self.main_menu_tab.setEnabled(True)
        self.main_menu_tab.setGeometry(QtCore.QRect(35, 66, 1291, 781))
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
        self.main_menu_tab.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.main_menu_tab.setFont(font)
        self.main_menu_tab.setAutoFillBackground(False)
        self.main_menu_tab.setStyleSheet("background-color: white;\n"
"margin: 0px;\n"
"padding:0px;\n"
"border: 0px;")
        self.main_menu_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_menu_tab.setTabBarAutoHide(True)
        self.main_menu_tab.setObjectName("main_menu_tab")
        self.acquisition_containerPage1 = QtWidgets.QWidget()
        self.acquisition_containerPage1.setObjectName("acquisition_containerPage1")
        self.detector_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.detector_frame.setGeometry(QtCore.QRect(43, 77, 241, 141))
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
        self.spectrometer_name_input.setGeometry(QtCore.QRect(326, 251, 181, 21))
        self.spectrometer_name_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrometer_name_input.setObjectName("spectrometer_name_input")
        self.load_acquisition_settings_button = QtWidgets.QPushButton(self.acquisition_containerPage1)
        self.load_acquisition_settings_button.setGeometry(QtCore.QRect(42, 20, 71, 25))
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
        self.image_frame.setGeometry(QtCore.QRect(300, 77, 231, 141))
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
        self.image_settings_label.setGeometry(QtCore.QRect(370, 69, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.image_settings_label.setFont(font)
        self.image_settings_label.setStyleSheet("color: #24262b;")
        self.image_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_settings_label.setObjectName("image_settings_label")
        self.spectrum_settings_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrum_settings_label.setGeometry(QtCore.QRect(100, 231, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrum_settings_label.setFont(font)
        self.spectrum_settings_label.setStyleSheet("color: #24262b;")
        self.spectrum_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spectrum_settings_label.setObjectName("spectrum_settings_label")
        self.spectrometer_name_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.spectrometer_name_label.setGeometry(QtCore.QRect(340, 230, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrometer_name_label.setFont(font)
        self.spectrometer_name_label.setStyleSheet("color: #24262b;")
        self.spectrometer_name_label.setObjectName("spectrometer_name_label")
        self.detector_settings_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.detector_settings_label.setGeometry(QtCore.QRect(119, 69, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label.setFont(font)
        self.detector_settings_label.setStyleSheet("color: #24262b;")
        self.detector_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label.setObjectName("detector_settings_label")
        self.save_acquisition_settings_button = QtWidgets.QPushButton(self.acquisition_containerPage1)
        self.save_acquisition_settings_button.setGeometry(QtCore.QRect(114, 20, 71, 25))
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
        self.spectrometer_name_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.spectrometer_name_frame.setGeometry(QtCore.QRect(300, 240, 231, 51))
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
        self.apply_acquisition_settings_button.setGeometry(QtCore.QRect(302, 317, 121, 41))
        self.apply_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.apply_acquisition_settings_button.setObjectName("apply_acquisition_settings_button")
        self.spectrum_frame = QtWidgets.QFrame(self.acquisition_containerPage1)
        self.spectrum_frame.setGeometry(QtCore.QRect(43, 240, 241, 171))
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
        self.live_button.setGeometry(QtCore.QRect(440, 318, 91, 91))
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
        self.image_label = QtWidgets.QLabel(self.acquisition_containerPage1)
        self.image_label.setGeometry(QtCore.QRect(700, 77, 541, 331))
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.acquisition_containerPage1)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(216, 253, 61, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spectrum_rotation_global_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_rotation_global_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_global_input.setObjectName("spectrum_rotation_global_input")
        self.verticalLayout_3.addWidget(self.spectrum_rotation_global_input)
        self.spectrum_rotation_spectrum_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_rotation_spectrum_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_spectrum_input.setObjectName("spectrum_rotation_spectrum_input")
        self.verticalLayout_3.addWidget(self.spectrum_rotation_spectrum_input)
        self.spectrum_start_x_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_start_x_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_start_x_input.setObjectName("spectrum_start_x_input")
        self.verticalLayout_3.addWidget(self.spectrum_start_x_input)
        self.spectrum_stop_x_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_stop_x_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_stop_x_input.setObjectName("spectrum_stop_x_input")
        self.verticalLayout_3.addWidget(self.spectrum_stop_x_input)
        self.spectrum_line_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_line_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_line_input.setObjectName("spectrum_line_input")
        self.verticalLayout_3.addWidget(self.spectrum_line_input)
        self.spectrum_lines_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_lines_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_lines_input.setObjectName("spectrum_lines_input")
        self.verticalLayout_3.addWidget(self.spectrum_lines_input)
        self.gridLayoutWidget = QtWidgets.QWidget(self.acquisition_containerPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(56, 90, 221, 112))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.detector_width_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_width_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_width_input.setObjectName("detector_width_input")
        self.gridLayout.addWidget(self.detector_width_input, 3, 1, 1, 1)
        self.detector_integration_time_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_integration_time_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_integration_time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_integration_time_label.setObjectName("detector_integration_time_label")
        self.gridLayout.addWidget(self.detector_integration_time_label, 0, 0, 1, 1)
        self.detector_gain_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_gain_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_gain_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_gain_label.setObjectName("detector_gain_label")
        self.gridLayout.addWidget(self.detector_gain_label, 2, 0, 1, 1)
        self.detector_averages_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_averages_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_averages_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_averages_label.setObjectName("detector_averages_label")
        self.gridLayout.addWidget(self.detector_averages_label, 1, 0, 1, 1)
        self.detector_gain_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_gain_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_gain_input.setObjectName("detector_gain_input")
        self.gridLayout.addWidget(self.detector_gain_input, 0, 1, 1, 1)
        self.detector_averages_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_averages_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_averages_input.setObjectName("detector_averages_input")
        self.gridLayout.addWidget(self.detector_averages_input, 1, 1, 1, 1)
        self.detector_height_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_height_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_height_input.setObjectName("detector_height_input")
        self.gridLayout.addWidget(self.detector_height_input, 3, 3, 1, 1)
        self.detector_resolution_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_resolution_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_resolution_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_resolution_label.setObjectName("detector_resolution_label")
        self.gridLayout.addWidget(self.detector_resolution_label, 3, 0, 1, 1)
        self.detector_integration_time_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_integration_time_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_integration_time_input.setObjectName("detector_integration_time_input")
        self.gridLayout.addWidget(self.detector_integration_time_input, 2, 1, 1, 1)
        self.detector_resolution_x_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_resolution_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_resolution_x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_resolution_x_label.setObjectName("detector_resolution_x_label")
        self.gridLayout.addWidget(self.detector_resolution_x_label, 3, 2, 1, 1)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.acquisition_containerPage1)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(92, 253, 121, 151))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.spectrum_rotation_global_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_rotation_global_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_rotation_global_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_rotation_global_label.setObjectName("spectrum_rotation_global_label")
        self.verticalLayout_4.addWidget(self.spectrum_rotation_global_label)
        self.spectrum_rotation_spectrum_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_rotation_spectrum_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_rotation_spectrum_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_rotation_spectrum_label.setObjectName("spectrum_rotation_spectrum_label")
        self.verticalLayout_4.addWidget(self.spectrum_rotation_spectrum_label)
        self.spectrum_start_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_start_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_start_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_start_x_label.setObjectName("spectrum_start_x_label")
        self.verticalLayout_4.addWidget(self.spectrum_start_x_label)
        self.spectrum_stop_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_stop_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_stop_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_stop_x_label.setObjectName("spectrum_stop_x_label")
        self.verticalLayout_4.addWidget(self.spectrum_stop_x_label)
        self.spectrum_line_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_line_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px;\n"
"\n"
"")
        self.spectrum_line_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_line_label.setObjectName("spectrum_line_label")
        self.verticalLayout_4.addWidget(self.spectrum_line_label)
        self.spectrum_lines_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_lines_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px;\n"
"")
        self.spectrum_lines_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_lines_label.setObjectName("spectrum_lines_label")
        self.verticalLayout_4.addWidget(self.spectrum_lines_label)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.acquisition_containerPage1)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(320, 90, 160, 101))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.image_scale_cropped_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_scale_cropped_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_scale_cropped_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_scale_cropped_label.setObjectName("image_scale_cropped_label")
        self.verticalLayout_8.addWidget(self.image_scale_cropped_label)
        self.image_crop_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_crop_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_crop_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_crop_label.setObjectName("image_crop_label")
        self.verticalLayout_8.addWidget(self.image_crop_label)
        self.image_scale_overview_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_scale_overview_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_scale_overview_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_scale_overview_label.setObjectName("image_scale_overview_label")
        self.verticalLayout_8.addWidget(self.image_scale_overview_label)
        self.image_camera_no_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.image_camera_no_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_camera_no_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_camera_no_label.setObjectName("image_camera_no_label")
        self.verticalLayout_8.addWidget(self.image_camera_no_label)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.acquisition_containerPage1)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(483, 90, 41, 101))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.image_scale_overview_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.image_scale_overview_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_scale_overview_input.setObjectName("image_scale_overview_input")
        self.verticalLayout_7.addWidget(self.image_scale_overview_input)
        self.image_scale_cropped_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.image_scale_cropped_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_scale_cropped_input.setObjectName("image_scale_cropped_input")
        self.verticalLayout_7.addWidget(self.image_scale_cropped_input)
        self.image_crop_box = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.image_crop_box.setEnabled(True)
        self.image_crop_box.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_crop_box.setText("")
        self.image_crop_box.setCheckable(True)
        self.image_crop_box.setChecked(False)
        self.image_crop_box.setObjectName("image_crop_box")
        self.verticalLayout_7.addWidget(self.image_crop_box, 0, QtCore.Qt.AlignHCenter)
        self.image_camera_no_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.image_camera_no_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_camera_no_input.setObjectName("image_camera_no_input")
        self.verticalLayout_7.addWidget(self.image_camera_no_input)
        self.detector_frame.raise_()
        self.spectrometer_name_frame.raise_()
        self.spectrum_frame.raise_()
        self.image_frame.raise_()
        self.spectrometer_name_input.raise_()
        self.load_acquisition_settings_button.raise_()
        self.image_settings_label.raise_()
        self.spectrum_settings_label.raise_()
        self.spectrometer_name_label.raise_()
        self.detector_settings_label.raise_()
        self.save_acquisition_settings_button.raise_()
        self.apply_acquisition_settings_button.raise_()
        self.live_button.raise_()
        self.image_label.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.gridLayoutWidget.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_8.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.main_menu_tab.addTab(self.acquisition_containerPage1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.main_menu_tab.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setGeometry(QtCore.QRect(43, 80, 481, 331))
        self.frame_5.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.clear_experiment_button = QtWidgets.QPushButton(self.frame_5)
        self.clear_experiment_button.setGeometry(QtCore.QRect(310, 290, 171, 41))
        self.clear_experiment_button.setStyleSheet("color: #24262b;")
        self.clear_experiment_button.setObjectName("clear_experiment_button")
        self.export_experiment_button = QtWidgets.QPushButton(self.frame_5)
        self.export_experiment_button.setGeometry(QtCore.QRect(0, 290, 311, 41))
        self.export_experiment_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.export_experiment_button.setObjectName("export_experiment_button")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(163, 60, 241, 31))
        self.frame.setStyleSheet("border-width: 0px;\n"
"border-style:solid;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.experiment_menu_fluorescence_button = QtWidgets.QPushButton(self.tab)
        self.experiment_menu_fluorescence_button.setGeometry(QtCore.QRect(290, 64, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_fluorescence_button.setFont(font)
        self.experiment_menu_fluorescence_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 0px;\n"
"border-color: #24262b;\n"
"border-style:solid;")
        self.experiment_menu_fluorescence_button.setObjectName("experiment_menu_fluorescence_button")
        self.experiment_menu_transmission_button = QtWidgets.QPushButton(self.tab)
        self.experiment_menu_transmission_button.setGeometry(QtCore.QRect(168, 64, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_transmission_button.setFont(font)
        self.experiment_menu_transmission_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 2px;\n"
"border-color: #24262b;\n"
"border-style:solid;\n"
"")
        self.experiment_menu_transmission_button.setObjectName("experiment_menu_transmission_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 110, 391, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.experiment_no_1_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_1_label.setFont(font)
        self.experiment_no_1_label.setStyleSheet("color:#14274e")
        self.experiment_no_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_1_label.setObjectName("experiment_no_1_label")
        self.verticalLayout_5.addWidget(self.experiment_no_1_label)
        self.experiment_no_2_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_2_label.setFont(font)
        self.experiment_no_2_label.setStyleSheet("color:#14274e")
        self.experiment_no_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_2_label.setObjectName("experiment_no_2_label")
        self.verticalLayout_5.addWidget(self.experiment_no_2_label)
        self.experiment_no_3_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_3_label.setFont(font)
        self.experiment_no_3_label.setStyleSheet("color:#14274e")
        self.experiment_no_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_3_label.setObjectName("experiment_no_3_label")
        self.verticalLayout_5.addWidget(self.experiment_no_3_label)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.acquire_dark_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_dark_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_dark_spectrum_button.setObjectName("acquire_dark_spectrum_button")
        self.verticalLayout_2.addWidget(self.acquire_dark_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.acquire_fluorescence_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_fluorescence_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_fluorescence_spectrum_button.setObjectName("acquire_fluorescence_spectrum_button")
        self.verticalLayout_2.addWidget(self.acquire_fluorescence_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.acquire_reference_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_reference_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_reference_spectrum_button.setObjectName("acquire_reference_spectrum_button")
        self.verticalLayout_2.addWidget(self.acquire_reference_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.acquire_transmission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.acquire_transmission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 15px;")
        self.acquire_transmission_spectrum_button.setObjectName("acquire_transmission_spectrum_button")
        self.verticalLayout_2.addWidget(self.acquire_transmission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.experiment_1_ok_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.experiment_1_ok_check.setEnabled(False)
        self.experiment_1_ok_check.setText("")
        self.experiment_1_ok_check.setCheckable(True)
        self.experiment_1_ok_check.setObjectName("experiment_1_ok_check")
        self.verticalLayout.addWidget(self.experiment_1_ok_check, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.experiment_2_ok_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.experiment_2_ok_check.setEnabled(False)
        self.experiment_2_ok_check.setText("")
        self.experiment_2_ok_check.setCheckable(True)
        self.experiment_2_ok_check.setObjectName("experiment_2_ok_check")
        self.verticalLayout.addWidget(self.experiment_2_ok_check, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.experiment_3_ok_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.experiment_3_ok_check.setEnabled(False)
        self.experiment_3_ok_check.setText("")
        self.experiment_3_ok_check.setCheckable(True)
        self.experiment_3_ok_check.setObjectName("experiment_3_ok_check")
        self.verticalLayout.addWidget(self.experiment_3_ok_check, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.calc_plot_frame = QtWidgets.QFrame(self.tab)
        self.calc_plot_frame.setGeometry(QtCore.QRect(640, 70, 631, 341))
        self.calc_plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_frame.setObjectName("calc_plot_frame")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.calc_plot_frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 611, 321))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calc_plot_2_i_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_i_label.setFont(font)
        self.calc_plot_2_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_i_label.setWordWrap(False)
        self.calc_plot_2_i_label.setObjectName("calc_plot_2_i_label")
        self.gridLayout_3.addWidget(self.calc_plot_2_i_label, 4, 0, 1, 1)
        self.calc_plot_2_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_label.setFont(font)
        self.calc_plot_2_label.setStyleSheet("color: #24262b;")
        self.calc_plot_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_label.setObjectName("calc_plot_2_label")
        self.gridLayout_3.addWidget(self.calc_plot_2_label, 3, 1, 1, 1)
        self.calc_plot_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_label.setFont(font)
        self.calc_plot_label.setStyleSheet("color: #24262b;")
        self.calc_plot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_label.setObjectName("calc_plot_label")
        self.gridLayout_3.addWidget(self.calc_plot_label, 0, 1, 1, 1)
        self.calc_plot_2_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_lambda_label.setFont(font)
        self.calc_plot_2_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_lambda_label.setWordWrap(False)
        self.calc_plot_2_lambda_label.setObjectName("calc_plot_2_lambda_label")
        self.gridLayout_3.addWidget(self.calc_plot_2_lambda_label, 5, 1, 1, 1)
        self.calc_plot_2 = PlotWidget(self.gridLayoutWidget_3)
        self.calc_plot_2.setEnabled(False)
        self.calc_plot_2.setObjectName("calc_plot_2")
        self.gridLayout_3.addWidget(self.calc_plot_2, 4, 1, 1, 1)
        self.calc_plot = PlotWidget(self.gridLayoutWidget_3)
        self.calc_plot.setEnabled(False)
        self.calc_plot.setObjectName("calc_plot")
        self.gridLayout_3.addWidget(self.calc_plot, 1, 1, 1, 1)
        self.calc_plot_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_lambda_label.setFont(font)
        self.calc_plot_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_lambda_label.setWordWrap(False)
        self.calc_plot_lambda_label.setObjectName("calc_plot_lambda_label")
        self.gridLayout_3.addWidget(self.calc_plot_lambda_label, 2, 1, 1, 1)
        self.calc_plot_i_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_i_label.setFont(font)
        self.calc_plot_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_i_label.setWordWrap(False)
        self.calc_plot_i_label.setObjectName("calc_plot_i_label")
        self.gridLayout_3.addWidget(self.calc_plot_i_label, 1, 0, 1, 1)
        self.calc_plot_3_frame = QtWidgets.QFrame(self.tab)
        self.calc_plot_3_frame.setGeometry(QtCore.QRect(640, 420, 631, 341))
        self.calc_plot_3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_3_frame.setObjectName("calc_plot_3_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.calc_plot_3_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.calc_plot_3_lambda_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_lambda_label.setFont(font)
        self.calc_plot_3_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_3_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_lambda_label.setWordWrap(False)
        self.calc_plot_3_lambda_label.setObjectName("calc_plot_3_lambda_label")
        self.gridLayout_4.addWidget(self.calc_plot_3_lambda_label, 8, 1, 1, 1)
        self.calc_plot_3_i_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_i_label.setFont(font)
        self.calc_plot_3_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_3_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_i_label.setWordWrap(False)
        self.calc_plot_3_i_label.setObjectName("calc_plot_3_i_label")
        self.gridLayout_4.addWidget(self.calc_plot_3_i_label, 7, 0, 1, 1)
        self.calc_plot_3_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_label.setFont(font)
        self.calc_plot_3_label.setStyleSheet("color: #24262b;")
        self.calc_plot_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_label.setObjectName("calc_plot_3_label")
        self.gridLayout_4.addWidget(self.calc_plot_3_label, 6, 1, 1, 1)
        self.calc_plot_3 = PlotWidget(self.verticalLayoutWidget)
        self.calc_plot_3.setEnabled(False)
        self.calc_plot_3.setObjectName("calc_plot_3")
        self.gridLayout_4.addWidget(self.calc_plot_3, 7, 1, 1, 1)
        self.main_menu_tab.addTab(self.tab, "")
        self.experiment_button = QtWidgets.QPushButton(Form)
        self.experiment_button.setGeometry(QtCore.QRect(739, 66, 140, 35))
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
        self.calibration_button.setGeometry(QtCore.QRect(582, 66, 140, 35))
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
        self.acquisition_button.setGeometry(QtCore.QRect(449, 66, 100, 35))
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
        self.spectrometer_name_frame_3.setGeometry(QtCore.QRect(-1, 19, 1331, 91))
        self.spectrometer_name_frame_3.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #9ba4b4;\n"
"background-color:#14274e")
        self.spectrometer_name_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrometer_name_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrometer_name_frame_3.setObjectName("spectrometer_name_frame_3")
        self.spec_mate_label = QtWidgets.QLabel(Form)
        self.spec_mate_label.setGeometry(QtCore.QRect(552, 21, 200, 31))
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
        self.junkyard_photonics__label_2.setGeometry(QtCore.QRect(714, 26, 31, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.junkyard_photonics__label_2.setFont(font)
        self.junkyard_photonics__label_2.setStyleSheet("background-color:#14274e;\n"
"font-family: helvetica;\n"
"color:#9ba4b4;")
        self.junkyard_photonics__label_2.setObjectName("junkyard_photonics__label_2")
        self.raw_plot_frame = QtWidgets.QFrame(Form)
        self.raw_plot_frame.setGeometry(QtCore.QRect(22, 509, 551, 341))
        self.raw_plot_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.raw_plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_plot_frame.setObjectName("raw_plot_frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.raw_plot_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(5, 19, 541, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.raw_spectrum_gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.raw_spectrum_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.raw_spectrum_gridLayout.setObjectName("raw_spectrum_gridLayout")
        self.raw_plot_lambda_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_lambda_label.setFont(font)
        self.raw_plot_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.raw_plot_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_lambda_label.setWordWrap(False)
        self.raw_plot_lambda_label.setObjectName("raw_plot_lambda_label")
        self.raw_spectrum_gridLayout.addWidget(self.raw_plot_lambda_label, 2, 1, 1, 1)
        self.raw_plot_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_label.setFont(font)
        self.raw_plot_label.setStyleSheet("color: #24262b;")
        self.raw_plot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_label.setWordWrap(False)
        self.raw_plot_label.setObjectName("raw_plot_label")
        self.raw_spectrum_gridLayout.addWidget(self.raw_plot_label, 0, 1, 1, 1)
        self.raw_plot = PlotWidget(self.verticalLayoutWidget_2)
        self.raw_plot.setObjectName("raw_plot")
        self.raw_spectrum_gridLayout.addWidget(self.raw_plot, 1, 1, 1, 1)
        self.raw_plot_i_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_i_label.setFont(font)
        self.raw_plot_i_label.setStyleSheet("color: #9ba4b4;")
        self.raw_plot_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_i_label.setWordWrap(False)
        self.raw_plot_i_label.setObjectName("raw_plot_i_label")
        self.raw_spectrum_gridLayout.addWidget(self.raw_plot_i_label, 1, 0, 1, 1)
        self.main_menu_tab.raise_()
        self.spectrometer_name_frame_3.raise_()
        self.junkyard_photonics_label.raise_()
        self.experiment_button.raise_()
        self.calibration_button.raise_()
        self.acquisition_button.raise_()
        self.spec_mate_label.raise_()
        self.junkyard_photonics__label_2.raise_()
        self.raw_plot_frame.raise_()

        self.retranslateUi(Form)
        self.main_menu_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.detector_gain_input, self.detector_averages_input)
        Form.setTabOrder(self.detector_averages_input, self.detector_integration_time_input)
        Form.setTabOrder(self.detector_integration_time_input, self.detector_width_input)
        Form.setTabOrder(self.detector_width_input, self.detector_height_input)
        Form.setTabOrder(self.detector_height_input, self.image_scale_overview_input)
        Form.setTabOrder(self.image_scale_overview_input, self.image_scale_cropped_input)
        Form.setTabOrder(self.image_scale_cropped_input, self.image_crop_box)
        Form.setTabOrder(self.image_crop_box, self.image_camera_no_input)
        Form.setTabOrder(self.image_camera_no_input, self.spectrum_rotation_global_input)
        Form.setTabOrder(self.spectrum_rotation_global_input, self.spectrum_rotation_spectrum_input)
        Form.setTabOrder(self.spectrum_rotation_spectrum_input, self.spectrum_start_x_input)
        Form.setTabOrder(self.spectrum_start_x_input, self.spectrum_stop_x_input)
        Form.setTabOrder(self.spectrum_stop_x_input, self.spectrum_line_input)
        Form.setTabOrder(self.spectrum_line_input, self.spectrum_lines_input)
        Form.setTabOrder(self.spectrum_lines_input, self.spectrometer_name_input)
        Form.setTabOrder(self.spectrometer_name_input, self.apply_acquisition_settings_button)
        Form.setTabOrder(self.apply_acquisition_settings_button, self.live_button)
        Form.setTabOrder(self.live_button, self.load_acquisition_settings_button)
        Form.setTabOrder(self.load_acquisition_settings_button, self.save_acquisition_settings_button)
        Form.setTabOrder(self.save_acquisition_settings_button, self.acquisition_button)
        Form.setTabOrder(self.acquisition_button, self.calibration_button)
        Form.setTabOrder(self.calibration_button, self.experiment_button)
        Form.setTabOrder(self.experiment_button, self.main_menu_tab)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "spec-tool // Open source spectral analysis"))
        self.junkyard_photonics_label.setText(_translate("Form", "by junkyard-photonics"))
        self.spectrometer_name_input.setText(_translate("Form", "ELP"))
        self.load_acquisition_settings_button.setText(_translate("Form", "Load"))
        self.image_settings_label.setText(_translate("Form", "Image"))
        self.spectrum_settings_label.setText(_translate("Form", "Spectrum config"))
        self.spectrometer_name_label.setText(_translate("Form", "Spectrometer name"))
        self.detector_settings_label.setText(_translate("Form", "Detector"))
        self.save_acquisition_settings_button.setText(_translate("Form", "Save"))
        self.apply_acquisition_settings_button.setText(_translate("Form", "Apply settings"))
        self.live_button.setText(_translate("Form", "Live"))
        self.spectrum_rotation_global_input.setText(_translate("Form", "0"))
        self.spectrum_rotation_spectrum_input.setText(_translate("Form", "0"))
        self.spectrum_start_x_input.setText(_translate("Form", "750"))
        self.spectrum_stop_x_input.setText(_translate("Form", "1230"))
        self.spectrum_line_input.setText(_translate("Form", "500"))
        self.spectrum_lines_input.setText(_translate("Form", "5"))
        self.detector_width_input.setText(_translate("Form", "1280"))
        self.detector_integration_time_label.setText(_translate("Form", "Integration time (ms):"))
        self.detector_gain_label.setText(_translate("Form", "Gain (0-100):"))
        self.detector_averages_label.setText(_translate("Form", "Averages:"))
        self.detector_gain_input.setText(_translate("Form", "20"))
        self.detector_averages_input.setText(_translate("Form", "5"))
        self.detector_height_input.setText(_translate("Form", "1024"))
        self.detector_resolution_label.setText(_translate("Form", "Resolution (WxH):"))
        self.detector_integration_time_input.setText(_translate("Form", "20"))
        self.detector_resolution_x_label.setText(_translate("Form", "x"))
        self.spectrum_rotation_global_label.setText(_translate("Form", "Rotation global:"))
        self.spectrum_rotation_spectrum_label.setText(_translate("Form", "Rotation spectrum:"))
        self.spectrum_start_x_label.setText(_translate("Form", "Start (x-val):"))
        self.spectrum_stop_x_label.setText(_translate("Form", "Stop (x-val):"))
        self.spectrum_line_label.setText(_translate("Form", "Line (y-val):"))
        self.spectrum_lines_label.setText(_translate("Form", "No of lines:"))
        self.image_scale_cropped_label.setText(_translate("Form", "Scale cropped (%):"))
        self.image_crop_label.setText(_translate("Form", "Crop to spectrum:"))
        self.image_scale_overview_label.setText(_translate("Form", "Scale overview (%):"))
        self.image_camera_no_label.setText(_translate("Form", "Camera #:"))
        self.image_scale_overview_input.setText(_translate("Form", "40"))
        self.image_scale_cropped_input.setText(_translate("Form", "150"))
        self.image_camera_no_input.setText(_translate("Form", "0"))
        self.main_menu_tab.setTabText(self.main_menu_tab.indexOf(self.tab_2), _translate("Form", "Page"))
        self.clear_experiment_button.setText(_translate("Form", "Clear"))
        self.export_experiment_button.setText(_translate("Form", "Export data"))
        self.experiment_menu_fluorescence_button.setText(_translate("Form", "Fluorescence"))
        self.experiment_menu_transmission_button.setText(_translate("Form", "Transmission"))
        self.experiment_no_1_label.setText(_translate("Form", "1."))
        self.experiment_no_2_label.setText(_translate("Form", "2."))
        self.experiment_no_3_label.setText(_translate("Form", "3."))
        self.acquire_dark_spectrum_button.setText(_translate("Form", "Dark spectrum"))
        self.acquire_fluorescence_spectrum_button.setText(_translate("Form", "Fluorescence spectrum"))
        self.acquire_reference_spectrum_button.setText(_translate("Form", "Reference spectrum"))
        self.acquire_transmission_spectrum_button.setText(_translate("Form", "Transmission spectrum"))
        self.calc_plot_2_i_label.setText(_translate("Form", "I"))
        self.calc_plot_2_label.setText(_translate("Form", "Reference"))
        self.calc_plot_label.setText(_translate("Form", "Dark"))
        self.calc_plot_2_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_i_label.setText(_translate("Form", "I"))
        self.calc_plot_3_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_3_i_label.setText(_translate("Form", "I"))
        self.calc_plot_3_label.setText(_translate("Form", "Transmission"))
        self.experiment_button.setText(_translate("Form", "Experiment"))
        self.calibration_button.setText(_translate("Form", "Calibration"))
        self.acquisition_button.setText(_translate("Form", "Acquisition"))
        self.spec_mate_label.setText(_translate("Form", "spec-tool"))
        self.junkyard_photonics__label_2.setText(_translate("Form", "v1.0"))
        self.raw_plot_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.raw_plot_label.setText(_translate("Form", "Raw spectrum"))
        self.raw_plot_i_label.setText(_translate("Form", "I"))


from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
