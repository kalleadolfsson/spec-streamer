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
        Form.resize(1229, 754)
        Form.setStyleSheet("background-color: white")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1330, 840))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(1330, 840))
        self.scrollArea.setMaximumSize(QtCore.QSize(1330, 840))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.container_widget = QtWidgets.QWidget()
        self.container_widget.setGeometry(QtCore.QRect(0, 0, 1330, 840))
        self.container_widget.setObjectName("container_widget")
        self.main_menu_tab = QtWidgets.QTabWidget(self.container_widget)
        self.main_menu_tab.setEnabled(True)
        self.main_menu_tab.setGeometry(QtCore.QRect(-4, 49, 1291, 701))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu_tab.sizePolicy().hasHeightForWidth())
        self.main_menu_tab.setSizePolicy(sizePolicy)
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
        self.main_menu_tab.setMouseTracking(True)
        self.main_menu_tab.setAutoFillBackground(False)
        self.main_menu_tab.setStyleSheet("background-color: white;\n"
"margin: 0px;\n"
"padding:0px;\n"
"border: 0px;")
        self.main_menu_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_menu_tab.setTabBarAutoHide(True)
        self.main_menu_tab.setObjectName("main_menu_tab")
        self.main_menu_acquisition_tab = QtWidgets.QWidget()
        self.main_menu_acquisition_tab.setObjectName("main_menu_acquisition_tab")
        self.load_acquisition_settings_button = QtWidgets.QPushButton(self.main_menu_acquisition_tab)
        self.load_acquisition_settings_button.setGeometry(QtCore.QRect(94, 8, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.load_acquisition_settings_button.setFont(font)
        self.load_acquisition_settings_button.setMouseTracking(True)
        self.load_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.load_acquisition_settings_button.setObjectName("load_acquisition_settings_button")
        self.save_acquisition_settings_button = QtWidgets.QPushButton(self.main_menu_acquisition_tab)
        self.save_acquisition_settings_button.setGeometry(QtCore.QRect(166, 8, 71, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_acquisition_settings_button.setFont(font)
        self.save_acquisition_settings_button.setMouseTracking(True)
        self.save_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_acquisition_settings_button.setObjectName("save_acquisition_settings_button")
        self.acquisition_frame = QtWidgets.QFrame(self.main_menu_acquisition_tab)
        self.acquisition_frame.setGeometry(QtCore.QRect(51, 45, 541, 351))
        self.acquisition_frame.setMouseTracking(True)
        self.acquisition_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.acquisition_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.acquisition_frame.setObjectName("acquisition_frame")
        self.spectrometer_name_label = QtWidgets.QLabel(self.acquisition_frame)
        self.spectrometer_name_label.setGeometry(QtCore.QRect(340, 150, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrometer_name_label.setFont(font)
        self.spectrometer_name_label.setMouseTracking(True)
        self.spectrometer_name_label.setStyleSheet("color: #24262b;")
        self.spectrometer_name_label.setObjectName("spectrometer_name_label")
        self.spectrometer_name_input = QtWidgets.QLineEdit(self.acquisition_frame)
        self.spectrometer_name_input.setGeometry(QtCore.QRect(312, 171, 211, 21))
        self.spectrometer_name_input.setMouseTracking(True)
        self.spectrometer_name_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrometer_name_input.setObjectName("spectrometer_name_input")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.acquisition_frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(216, 173, 61, 151))
        self.verticalLayoutWidget_3.setMouseTracking(True)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.spectrum_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.spectrum_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.spectrum_vertical_layout.setSpacing(0)
        self.spectrum_vertical_layout.setObjectName("spectrum_vertical_layout")
        self.spectrum_rotation_global_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_rotation_global_input.setMouseTracking(True)
        self.spectrum_rotation_global_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_global_input.setObjectName("spectrum_rotation_global_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_rotation_global_input)
        self.spectrum_rotation_spectrum_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_rotation_spectrum_input.setMouseTracking(True)
        self.spectrum_rotation_spectrum_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_rotation_spectrum_input.setObjectName("spectrum_rotation_spectrum_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_rotation_spectrum_input)
        self.spectrum_start_x_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_start_x_input.setMouseTracking(True)
        self.spectrum_start_x_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_start_x_input.setObjectName("spectrum_start_x_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_start_x_input)
        self.spectrum_stop_x_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_stop_x_input.setMouseTracking(True)
        self.spectrum_stop_x_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_stop_x_input.setObjectName("spectrum_stop_x_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_stop_x_input)
        self.spectrum_line_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_line_input.setMouseTracking(True)
        self.spectrum_line_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_line_input.setObjectName("spectrum_line_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_line_input)
        self.spectrum_lines_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.spectrum_lines_input.setMouseTracking(True)
        self.spectrum_lines_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.spectrum_lines_input.setObjectName("spectrum_lines_input")
        self.spectrum_vertical_layout.addWidget(self.spectrum_lines_input)
        self.apply_acquisition_settings_button = QtWidgets.QPushButton(self.acquisition_frame)
        self.apply_acquisition_settings_button.setGeometry(QtCore.QRect(302, 237, 121, 41))
        self.apply_acquisition_settings_button.setMouseTracking(True)
        self.apply_acquisition_settings_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.apply_acquisition_settings_button.setObjectName("apply_acquisition_settings_button")
        self.image_settings_label = QtWidgets.QLabel(self.acquisition_frame)
        self.image_settings_label.setGeometry(QtCore.QRect(370, -2, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.image_settings_label.setFont(font)
        self.image_settings_label.setMouseTracking(True)
        self.image_settings_label.setStyleSheet("color: #24262b;")
        self.image_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_settings_label.setObjectName("image_settings_label")
        self.detector_settings_label = QtWidgets.QLabel(self.acquisition_frame)
        self.detector_settings_label.setGeometry(QtCore.QRect(119, -1, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.detector_settings_label.setFont(font)
        self.detector_settings_label.setMouseTracking(True)
        self.detector_settings_label.setStyleSheet("color: #24262b;")
        self.detector_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_settings_label.setObjectName("detector_settings_label")
        self.spectrometer_name_frame = QtWidgets.QFrame(self.acquisition_frame)
        self.spectrometer_name_frame.setGeometry(QtCore.QRect(300, 160, 231, 51))
        self.spectrometer_name_frame.setMouseTracking(True)
        self.spectrometer_name_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.spectrometer_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrometer_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrometer_name_frame.setObjectName("spectrometer_name_frame")
        self.detector_frame = QtWidgets.QFrame(self.acquisition_frame)
        self.detector_frame.setGeometry(QtCore.QRect(43, 7, 241, 141))
        self.detector_frame.setMouseTracking(True)
        self.detector_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.detector_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detector_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detector_frame.setObjectName("detector_frame")
        self.spectrum_settings_label = QtWidgets.QLabel(self.acquisition_frame)
        self.spectrum_settings_label.setGeometry(QtCore.QRect(100, 151, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spectrum_settings_label.setFont(font)
        self.spectrum_settings_label.setMouseTracking(True)
        self.spectrum_settings_label.setStyleSheet("color: #24262b;")
        self.spectrum_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spectrum_settings_label.setObjectName("spectrum_settings_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.acquisition_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(56, 20, 221, 112))
        self.gridLayoutWidget.setMouseTracking(True)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.detector_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.detector_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.detector_grid_layout.setSpacing(0)
        self.detector_grid_layout.setObjectName("detector_grid_layout")
        self.detector_width_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_width_input.setMouseTracking(True)
        self.detector_width_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_width_input.setObjectName("detector_width_input")
        self.detector_grid_layout.addWidget(self.detector_width_input, 3, 1, 1, 1)
        self.detector_integration_time_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_integration_time_label.setMouseTracking(True)
        self.detector_integration_time_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_integration_time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_integration_time_label.setObjectName("detector_integration_time_label")
        self.detector_grid_layout.addWidget(self.detector_integration_time_label, 0, 0, 1, 1)
        self.detector_gain_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_gain_label.setMouseTracking(True)
        self.detector_gain_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_gain_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_gain_label.setObjectName("detector_gain_label")
        self.detector_grid_layout.addWidget(self.detector_gain_label, 2, 0, 1, 1)
        self.detector_averages_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_averages_label.setMouseTracking(True)
        self.detector_averages_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_averages_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_averages_label.setObjectName("detector_averages_label")
        self.detector_grid_layout.addWidget(self.detector_averages_label, 1, 0, 1, 1)
        self.detector_gain_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_gain_input.setMouseTracking(True)
        self.detector_gain_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_gain_input.setObjectName("detector_gain_input")
        self.detector_grid_layout.addWidget(self.detector_gain_input, 0, 1, 1, 1)
        self.detector_averages_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_averages_input.setMouseTracking(True)
        self.detector_averages_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_averages_input.setObjectName("detector_averages_input")
        self.detector_grid_layout.addWidget(self.detector_averages_input, 1, 1, 1, 1)
        self.detector_height_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_height_input.setMouseTracking(True)
        self.detector_height_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_height_input.setObjectName("detector_height_input")
        self.detector_grid_layout.addWidget(self.detector_height_input, 3, 3, 1, 1)
        self.detector_resolution_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_resolution_label.setMouseTracking(True)
        self.detector_resolution_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_resolution_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.detector_resolution_label.setObjectName("detector_resolution_label")
        self.detector_grid_layout.addWidget(self.detector_resolution_label, 3, 0, 1, 1)
        self.detector_integration_time_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.detector_integration_time_input.setMouseTracking(True)
        self.detector_integration_time_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.detector_integration_time_input.setObjectName("detector_integration_time_input")
        self.detector_grid_layout.addWidget(self.detector_integration_time_input, 2, 1, 1, 1)
        self.detector_resolution_x_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detector_resolution_x_label.setMouseTracking(True)
        self.detector_resolution_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.detector_resolution_x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detector_resolution_x_label.setObjectName("detector_resolution_x_label")
        self.detector_grid_layout.addWidget(self.detector_resolution_x_label, 3, 2, 1, 1)
        self.live_button = QtWidgets.QPushButton(self.acquisition_frame)
        self.live_button.setGeometry(QtCore.QRect(440, 238, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.live_button.setFont(font)
        self.live_button.setMouseTracking(True)
        self.live_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.live_button.setObjectName("live_button")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.acquisition_frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(92, 173, 121, 151))
        self.verticalLayoutWidget_4.setMouseTracking(True)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.spectrum_vertical_layout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.spectrum_vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.spectrum_vertical_layout_2.setSpacing(0)
        self.spectrum_vertical_layout_2.setObjectName("spectrum_vertical_layout_2")
        self.spectrum_rotation_global_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_rotation_global_label.setMouseTracking(True)
        self.spectrum_rotation_global_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_rotation_global_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_rotation_global_label.setObjectName("spectrum_rotation_global_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_rotation_global_label)
        self.spectrum_rotation_spectrum_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_rotation_spectrum_label.setMouseTracking(True)
        self.spectrum_rotation_spectrum_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_rotation_spectrum_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_rotation_spectrum_label.setObjectName("spectrum_rotation_spectrum_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_rotation_spectrum_label)
        self.spectrum_start_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_start_x_label.setMouseTracking(True)
        self.spectrum_start_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_start_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_start_x_label.setObjectName("spectrum_start_x_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_start_x_label)
        self.spectrum_stop_x_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_stop_x_label.setMouseTracking(True)
        self.spectrum_stop_x_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.spectrum_stop_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_stop_x_label.setObjectName("spectrum_stop_x_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_stop_x_label)
        self.spectrum_line_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_line_label.setMouseTracking(True)
        self.spectrum_line_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px;\n"
"\n"
"")
        self.spectrum_line_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_line_label.setObjectName("spectrum_line_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_line_label)
        self.spectrum_lines_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.spectrum_lines_label.setMouseTracking(True)
        self.spectrum_lines_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px;\n"
"")
        self.spectrum_lines_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spectrum_lines_label.setObjectName("spectrum_lines_label")
        self.spectrum_vertical_layout_2.addWidget(self.spectrum_lines_label)
        self.image_frame = QtWidgets.QFrame(self.acquisition_frame)
        self.image_frame.setGeometry(QtCore.QRect(300, 7, 231, 141))
        self.image_frame.setMouseTracking(True)
        self.image_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.spectrum_frame = QtWidgets.QFrame(self.acquisition_frame)
        self.spectrum_frame.setGeometry(QtCore.QRect(43, 160, 241, 171))
        self.spectrum_frame.setMouseTracking(True)
        self.spectrum_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.spectrum_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spectrum_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spectrum_frame.setObjectName("spectrum_frame")
        self.detector_frame.raise_()
        self.spectrum_frame.raise_()
        self.image_frame.raise_()
        self.spectrometer_name_frame.raise_()
        self.spectrometer_name_label.raise_()
        self.spectrometer_name_input.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.apply_acquisition_settings_button.raise_()
        self.detector_settings_label.raise_()
        self.spectrum_settings_label.raise_()
        self.gridLayoutWidget.raise_()
        self.live_button.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.image_settings_label.raise_()
        self.cursor_overview_label = QtWidgets.QLabel(self.main_menu_acquisition_tab)
        self.cursor_overview_label.setGeometry(QtCore.QRect(680, 52, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cursor_overview_label.setFont(font)
        self.cursor_overview_label.setMouseTracking(True)
        self.cursor_overview_label.setObjectName("cursor_overview_label")
        self.image_overview_view = GraphicsLayoutWidget(self.main_menu_acquisition_tab)
        self.image_overview_view.setGeometry(QtCore.QRect(680, 67, 540, 340))
        self.image_overview_view.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 0ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;\n"
"background-color: #f1f6f9;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.image_overview_view.setLineWidth(0)
        self.image_overview_view.setObjectName("image_overview_view")
        self.image_cropped_view = GraphicsLayoutWidget(self.main_menu_acquisition_tab)
        self.image_cropped_view.setGeometry(QtCore.QRect(679, 430, 541, 191))
        self.image_cropped_view.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 0ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;\n"
"background-color: #f1f6f9;")
        self.image_cropped_view.setObjectName("image_cropped_view")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.main_menu_acquisition_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(404, 63, 171, 61))
        self.gridLayoutWidget_2.setMouseTracking(True)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.image_camera_no_input = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.image_camera_no_input.setMouseTracking(True)
        self.image_camera_no_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_camera_no_input.setObjectName("image_camera_no_input")
        self.gridLayout.addWidget(self.image_camera_no_input, 2, 1, 1, 1)
        self.image_camera_no_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.image_camera_no_label.setMouseTracking(True)
        self.image_camera_no_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_camera_no_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_camera_no_label.setObjectName("image_camera_no_label")
        self.gridLayout.addWidget(self.image_camera_no_label, 2, 0, 1, 1)
        self.image_downsampling_overview_input = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.image_downsampling_overview_input.setMouseTracking(True)
        self.image_downsampling_overview_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.image_downsampling_overview_input.setObjectName("image_downsampling_overview_input")
        self.gridLayout.addWidget(self.image_downsampling_overview_input, 1, 1, 1, 1)
        self.image_downsampling_overview_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.image_downsampling_overview_label.setMouseTracking(True)
        self.image_downsampling_overview_label.setStyleSheet("color: #24262b;\n"
"outline:0px;\n"
"border-width:0px,")
        self.image_downsampling_overview_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.image_downsampling_overview_label.setObjectName("image_downsampling_overview_label")
        self.gridLayout.addWidget(self.image_downsampling_overview_label, 1, 0, 1, 1)
        self.main_menu_tab.addTab(self.main_menu_acquisition_tab, "")
        self.main_menu_calibration_tab = QtWidgets.QWidget()
        self.main_menu_calibration_tab.setObjectName("main_menu_calibration_tab")
        self.calibration_flow_frame = QtWidgets.QFrame(self.main_menu_calibration_tab)
        self.calibration_flow_frame.setGeometry(QtCore.QRect(93, 56, 491, 331))
        self.calibration_flow_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.calibration_flow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_flow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_flow_frame.setObjectName("calibration_flow_frame")
        self.clear_calibration_button = QtWidgets.QPushButton(self.calibration_flow_frame)
        self.clear_calibration_button.setGeometry(QtCore.QRect(310, 290, 181, 41))
        self.clear_calibration_button.setStyleSheet("color: #24262b;")
        self.clear_calibration_button.setObjectName("clear_calibration_button")
        self.save_calibration_button = QtWidgets.QPushButton(self.calibration_flow_frame)
        self.save_calibration_button.setGeometry(QtCore.QRect(0, 290, 156, 41))
        self.save_calibration_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calibration_button.setObjectName("save_calibration_button")
        self.load_calibration_button = QtWidgets.QPushButton(self.calibration_flow_frame)
        self.load_calibration_button.setGeometry(QtCore.QRect(155, 290, 156, 41))
        self.load_calibration_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.load_calibration_button.setObjectName("load_calibration_button")
        self.calibration_next_button = QtWidgets.QPushButton(self.calibration_flow_frame)
        self.calibration_next_button.setGeometry(QtCore.QRect(440, 140, 51, 41))
        self.calibration_next_button.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"background-color:#14274e;\n"
"color: white;")
        self.calibration_next_button.setObjectName("calibration_next_button")
        self.calibration_step_1_label = QtWidgets.QLabel(self.calibration_flow_frame)
        self.calibration_step_1_label.setGeometry(QtCore.QRect(20, 13, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.calibration_step_1_label.setFont(font)
        self.calibration_step_1_label.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.calibration_step_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calibration_step_1_label.setObjectName("calibration_step_1_label")
        self.calibration_step_2_label = QtWidgets.QLabel(self.calibration_flow_frame)
        self.calibration_step_2_label.setGeometry(QtCore.QRect(180, 13, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.calibration_step_2_label.setFont(font)
        self.calibration_step_2_label.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"color:#9ba4b4;")
        self.calibration_step_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calibration_step_2_label.setObjectName("calibration_step_2_label")
        self.calibration_step_3_label = QtWidgets.QLabel(self.calibration_flow_frame)
        self.calibration_step_3_label.setGeometry(QtCore.QRect(330, 13, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.calibration_step_3_label.setFont(font)
        self.calibration_step_3_label.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"color:#9ba4b4;")
        self.calibration_step_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calibration_step_3_label.setObjectName("calibration_step_3_label")
        self.calibration_plot_acquisition_flow_frame = QtWidgets.QFrame(self.calibration_flow_frame)
        self.calibration_plot_acquisition_flow_frame.setGeometry(QtCore.QRect(50, 40, 391, 241))
        self.calibration_plot_acquisition_flow_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.calibration_plot_acquisition_flow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_plot_acquisition_flow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_plot_acquisition_flow_frame.setObjectName("calibration_plot_acquisition_flow_frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.calibration_plot_acquisition_flow_frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 3, 391, 231))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.calibration_flow_horizontal_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.calibration_flow_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.calibration_flow_horizontal_layout.setObjectName("calibration_flow_horizontal_layout")
        self.calibration_flow_vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.calibration_flow_vertical_layout_1.setObjectName("calibration_flow_vertical_layout_1")
        self.calibration_no_1_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.calibration_no_1_label.setFont(font)
        self.calibration_no_1_label.setStyleSheet("color:#14274e;\n"
"opacity: 0.5;")
        self.calibration_no_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calibration_no_1_label.setObjectName("calibration_no_1_label")
        self.calibration_flow_vertical_layout_1.addWidget(self.calibration_no_1_label)
        self.calibration_no_2_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.calibration_no_2_label.setFont(font)
        self.calibration_no_2_label.setStyleSheet("color:#14274e")
        self.calibration_no_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calibration_no_2_label.setObjectName("calibration_no_2_label")
        self.calibration_flow_vertical_layout_1.addWidget(self.calibration_no_2_label)
        self.calibration_no_3_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.calibration_no_3_label.setFont(font)
        self.calibration_no_3_label.setStyleSheet("color:#14274e")
        self.calibration_no_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calibration_no_3_label.setObjectName("calibration_no_3_label")
        self.calibration_flow_vertical_layout_1.addWidget(self.calibration_no_3_label)
        self.calibration_flow_horizontal_layout.addLayout(self.calibration_flow_vertical_layout_1)
        self.calibration_flow_vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.calibration_flow_vertical_layout_2.setObjectName("calibration_flow_vertical_layout_2")
        self.calibration_acquire_dark_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calibration_acquire_dark_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.calibration_acquire_dark_spectrum_button.setObjectName("calibration_acquire_dark_spectrum_button")
        self.calibration_flow_vertical_layout_2.addWidget(self.calibration_acquire_dark_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.calibration_acquire_emission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calibration_acquire_emission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.calibration_acquire_emission_spectrum_button.setObjectName("calibration_acquire_emission_spectrum_button")
        self.calibration_flow_vertical_layout_2.addWidget(self.calibration_acquire_emission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.calibration_acquire_reference_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calibration_acquire_reference_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.calibration_acquire_reference_spectrum_button.setObjectName("calibration_acquire_reference_spectrum_button")
        self.calibration_flow_vertical_layout_2.addWidget(self.calibration_acquire_reference_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.calibration_acquire_transmission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.calibration_acquire_transmission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.calibration_acquire_transmission_spectrum_button.setObjectName("calibration_acquire_transmission_spectrum_button")
        self.calibration_flow_vertical_layout_2.addWidget(self.calibration_acquire_transmission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.calibration_flow_horizontal_layout.addLayout(self.calibration_flow_vertical_layout_2)
        self.calibration_flow_vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.calibration_flow_vertical_layout_3.setObjectName("calibration_flow_vertical_layout_3")
        self.calibration_check_label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.calibration_check_label_1.setText("")
        self.calibration_check_label_1.setObjectName("calibration_check_label_1")
        self.calibration_flow_vertical_layout_3.addWidget(self.calibration_check_label_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.calibration_check_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.calibration_check_label_2.setText("")
        self.calibration_check_label_2.setObjectName("calibration_check_label_2")
        self.calibration_flow_vertical_layout_3.addWidget(self.calibration_check_label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.calibration_check_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.calibration_check_label_3.setText("")
        self.calibration_check_label_3.setObjectName("calibration_check_label_3")
        self.calibration_flow_vertical_layout_3.addWidget(self.calibration_check_label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.calibration_flow_horizontal_layout.addLayout(self.calibration_flow_vertical_layout_3)
        self.calibration_identify_peaks_frame = QtWidgets.QFrame(self.calibration_flow_frame)
        self.calibration_identify_peaks_frame.setGeometry(QtCore.QRect(7, 40, 431, 231))
        self.calibration_identify_peaks_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.calibration_identify_peaks_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_identify_peaks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_identify_peaks_frame.setObjectName("calibration_identify_peaks_frame")
        self.pixel_wavelength_list = QtWidgets.QListWidget(self.calibration_identify_peaks_frame)
        self.pixel_wavelength_list.setGeometry(QtCore.QRect(227, 48, 171, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pixel_wavelength_list.setFont(font)
        self.pixel_wavelength_list.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.pixel_wavelength_list.setObjectName("pixel_wavelength_list")
        self.pixel_input = QtWidgets.QLineEdit(self.calibration_identify_peaks_frame)
        self.pixel_input.setGeometry(QtCore.QRect(144, 49, 51, 21))
        self.pixel_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.pixel_input.setText("")
        self.pixel_input.setObjectName("pixel_input")
        self.wavelength_input = QtWidgets.QLineEdit(self.calibration_identify_peaks_frame)
        self.wavelength_input.setGeometry(QtCore.QRect(144, 79, 51, 21))
        self.wavelength_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.wavelength_input.setObjectName("wavelength_input")
        self.pixel_input_label = QtWidgets.QLabel(self.calibration_identify_peaks_frame)
        self.pixel_input_label.setGeometry(QtCore.QRect(93, 50, 51, 16))
        self.pixel_input_label.setObjectName("pixel_input_label")
        self.wavelength_input_label = QtWidgets.QLabel(self.calibration_identify_peaks_frame)
        self.wavelength_input_label.setGeometry(QtCore.QRect(29, 79, 111, 20))
        self.wavelength_input_label.setObjectName("wavelength_input_label")
        self.add_pixel_wavelength_point_button = QtWidgets.QPushButton(self.calibration_identify_peaks_frame)
        self.add_pixel_wavelength_point_button.setGeometry(QtCore.QRect(94, 110, 101, 31))
        self.add_pixel_wavelength_point_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.add_pixel_wavelength_point_button.setObjectName("add_pixel_wavelength_point_button")
        self.pixel_input_label_2 = QtWidgets.QLabel(self.calibration_identify_peaks_frame)
        self.pixel_input_label_2.setGeometry(QtCore.QRect(229, 29, 51, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.pixel_input_label_2.setFont(font)
        self.pixel_input_label_2.setStyleSheet("color:#9ba4b4;")
        self.pixel_input_label_2.setObjectName("pixel_input_label_2")
        self.wavelength_input_label_2 = QtWidgets.QLabel(self.calibration_identify_peaks_frame)
        self.wavelength_input_label_2.setGeometry(QtCore.QRect(321, 29, 81, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.wavelength_input_label_2.setFont(font)
        self.wavelength_input_label_2.setStyleSheet("color:#9ba4b4;")
        self.wavelength_input_label_2.setObjectName("wavelength_input_label_2")
        self.calibration_back_button = QtWidgets.QPushButton(self.calibration_flow_frame)
        self.calibration_back_button.setGeometry(QtCore.QRect(0, 140, 51, 41))
        self.calibration_back_button.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"background-color:#14274e;\n"
"color: white;")
        self.calibration_back_button.setObjectName("calibration_back_button")
        self.calibration_pixel_wavelength_polynomial_frame = QtWidgets.QFrame(self.calibration_flow_frame)
        self.calibration_pixel_wavelength_polynomial_frame.setGeometry(QtCore.QRect(50, 40, 391, 241))
        self.calibration_pixel_wavelength_polynomial_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.calibration_pixel_wavelength_polynomial_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_pixel_wavelength_polynomial_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_pixel_wavelength_polynomial_frame.setObjectName("calibration_pixel_wavelength_polynomial_frame")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.calibration_pixel_wavelength_polynomial_frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(90, 50, 231, 121))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pixel_wavelength_polynomial_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.pixel_wavelength_polynomial_label.setObjectName("pixel_wavelength_polynomial_label")
        self.verticalLayout.addWidget(self.pixel_wavelength_polynomial_label)
        self.pixel_wavelength_polynomial_coeffs_a_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.pixel_wavelength_polynomial_coeffs_a_label.setObjectName("pixel_wavelength_polynomial_coeffs_a_label")
        self.verticalLayout.addWidget(self.pixel_wavelength_polynomial_coeffs_a_label)
        self.pixel_wavelength_polynomial_coeffs_b_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.pixel_wavelength_polynomial_coeffs_b_label.setObjectName("pixel_wavelength_polynomial_coeffs_b_label")
        self.verticalLayout.addWidget(self.pixel_wavelength_polynomial_coeffs_b_label)
        self.pixel_wavelength_polynomial_coeffs_c_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.pixel_wavelength_polynomial_coeffs_c_label.setObjectName("pixel_wavelength_polynomial_coeffs_c_label")
        self.verticalLayout.addWidget(self.pixel_wavelength_polynomial_coeffs_c_label)
        self.pixel_wavelength_polynomial_coeffs_d_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.pixel_wavelength_polynomial_coeffs_d_label.setObjectName("pixel_wavelength_polynomial_coeffs_d_label")
        self.verticalLayout.addWidget(self.pixel_wavelength_polynomial_coeffs_d_label)
        self.calibration_set_black_body_frame = QtWidgets.QFrame(self.calibration_flow_frame)
        self.calibration_set_black_body_frame.setGeometry(QtCore.QRect(60, 40, 381, 231))
        self.calibration_set_black_body_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.calibration_set_black_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_set_black_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_set_black_body_frame.setObjectName("calibration_set_black_body_frame")
        self.black_body_temperature_input = QtWidgets.QLineEdit(self.calibration_set_black_body_frame)
        self.black_body_temperature_input.setGeometry(QtCore.QRect(247, 41, 51, 21))
        self.black_body_temperature_input.setStyleSheet("background-color: white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: #d6e0f0;\n"
"color: #24262b;")
        self.black_body_temperature_input.setText("")
        self.black_body_temperature_input.setObjectName("black_body_temperature_input")
        self.black_body_temperature_input_label = QtWidgets.QLabel(self.calibration_set_black_body_frame)
        self.black_body_temperature_input_label.setGeometry(QtCore.QRect(70, 40, 181, 20))
        self.black_body_temperature_input_label.setObjectName("black_body_temperature_input_label")
        self.black_body_temperature_input_label.raise_()
        self.black_body_temperature_input.raise_()
        self.calibration_get_spectral_sensitivity_frame = QtWidgets.QFrame(self.calibration_flow_frame)
        self.calibration_get_spectral_sensitivity_frame.setGeometry(QtCore.QRect(10, 40, 431, 231))
        self.calibration_get_spectral_sensitivity_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.calibration_get_spectral_sensitivity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_get_spectral_sensitivity_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_get_spectral_sensitivity_frame.setObjectName("calibration_get_spectral_sensitivity_frame")
        self.black_body_stats_label = QtWidgets.QLabel(self.calibration_get_spectral_sensitivity_frame)
        self.black_body_stats_label.setGeometry(QtCore.QRect(160, 70, 101, 20))
        self.black_body_stats_label.setObjectName("black_body_stats_label")
        self.calibration_get_spectral_sensitivity_frame.raise_()
        self.clear_calibration_button.raise_()
        self.save_calibration_button.raise_()
        self.load_calibration_button.raise_()
        self.calibration_step_1_label.raise_()
        self.calibration_step_2_label.raise_()
        self.calibration_step_3_label.raise_()
        self.calibration_pixel_wavelength_polynomial_frame.raise_()
        self.calibration_next_button.raise_()
        self.calibration_set_black_body_frame.raise_()
        self.calibration_identify_peaks_frame.raise_()
        self.calibration_plot_acquisition_flow_frame.raise_()
        self.calibration_back_button.raise_()
        self.calibration_menu_pixel_wavelength_button = QtWidgets.QPushButton(self.main_menu_calibration_tab)
        self.calibration_menu_pixel_wavelength_button.setGeometry(QtCore.QRect(190, 40, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_menu_pixel_wavelength_button.setFont(font)
        self.calibration_menu_pixel_wavelength_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 2px;\n"
"border-color: #24262b;\n"
"border-style:solid;\n"
"")
        self.calibration_menu_pixel_wavelength_button.setObjectName("calibration_menu_pixel_wavelength_button")
        self.calibration_menu_spectral_sensitivity_button = QtWidgets.QPushButton(self.main_menu_calibration_tab)
        self.calibration_menu_spectral_sensitivity_button.setEnabled(True)
        self.calibration_menu_spectral_sensitivity_button.setGeometry(QtCore.QRect(340, 40, 141, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_menu_spectral_sensitivity_button.setFont(font)
        self.calibration_menu_spectral_sensitivity_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 0px;\n"
"border-color: #24262b;\n"
"border-style:solid;")
        self.calibration_menu_spectral_sensitivity_button.setObjectName("calibration_menu_spectral_sensitivity_button")
        self.calibration_menu_frame = QtWidgets.QFrame(self.main_menu_calibration_tab)
        self.calibration_menu_frame.setGeometry(QtCore.QRect(210, 42, 241, 31))
        self.calibration_menu_frame.setStyleSheet("border-width: 0px;\n"
"border-style:solid;\n"
"")
        self.calibration_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calibration_menu_frame.setObjectName("calibration_menu_frame")
        self.calibration_flow_frame.raise_()
        self.calibration_menu_frame.raise_()
        self.calibration_menu_pixel_wavelength_button.raise_()
        self.calibration_menu_spectral_sensitivity_button.raise_()
        self.main_menu_tab.addTab(self.main_menu_calibration_tab, "")
        self.main_menu_experiment_tab = QtWidgets.QWidget()
        self.main_menu_experiment_tab.setObjectName("main_menu_experiment_tab")
        self.experiment_flow_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.experiment_flow_frame.setGeometry(QtCore.QRect(93, 56, 491, 331))
        self.experiment_flow_frame.setStyleSheet("outline-color: #8d93ab;\n"
"outline-width: 4ps;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #8d93ab;")
        self.experiment_flow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_flow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_flow_frame.setObjectName("experiment_flow_frame")
        self.clear_experiment_button = QtWidgets.QPushButton(self.experiment_flow_frame)
        self.clear_experiment_button.setGeometry(QtCore.QRect(310, 290, 181, 41))
        self.clear_experiment_button.setStyleSheet("color: #24262b;")
        self.clear_experiment_button.setObjectName("clear_experiment_button")
        self.export_experiment_button = QtWidgets.QPushButton(self.experiment_flow_frame)
        self.export_experiment_button.setGeometry(QtCore.QRect(0, 290, 311, 41))
        self.export_experiment_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.export_experiment_button.setObjectName("export_experiment_button")
        self.experiment_plot_acquisition_flow_frame = QtWidgets.QFrame(self.experiment_flow_frame)
        self.experiment_plot_acquisition_flow_frame.setGeometry(QtCore.QRect(50, 40, 391, 241))
        self.experiment_plot_acquisition_flow_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.experiment_plot_acquisition_flow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_plot_acquisition_flow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_plot_acquisition_flow_frame.setObjectName("experiment_plot_acquisition_flow_frame")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.experiment_plot_acquisition_flow_frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 3, 391, 231))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.experiment_flow_horizontal_layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.experiment_flow_horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.experiment_flow_horizontal_layout_2.setObjectName("experiment_flow_horizontal_layout_2")
        self.experiment_flow_vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.experiment_flow_vertical_layout_1.setObjectName("experiment_flow_vertical_layout_1")
        self.experiment_no_1_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_1_label.setFont(font)
        self.experiment_no_1_label.setStyleSheet("color:#14274e")
        self.experiment_no_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_1_label.setObjectName("experiment_no_1_label")
        self.experiment_flow_vertical_layout_1.addWidget(self.experiment_no_1_label)
        self.experiment_no_2_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_2_label.setFont(font)
        self.experiment_no_2_label.setStyleSheet("color:#14274e")
        self.experiment_no_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_2_label.setObjectName("experiment_no_2_label")
        self.experiment_flow_vertical_layout_1.addWidget(self.experiment_no_2_label)
        self.experiment_no_3_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.experiment_no_3_label.setFont(font)
        self.experiment_no_3_label.setStyleSheet("color:#14274e")
        self.experiment_no_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.experiment_no_3_label.setObjectName("experiment_no_3_label")
        self.experiment_flow_vertical_layout_1.addWidget(self.experiment_no_3_label)
        self.experiment_flow_horizontal_layout_2.addLayout(self.experiment_flow_vertical_layout_1)
        self.experiment_flow_vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.experiment_flow_vertical_layout_2.setObjectName("experiment_flow_vertical_layout_2")
        self.experiment_acquire_dark_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.experiment_acquire_dark_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.experiment_acquire_dark_spectrum_button.setObjectName("experiment_acquire_dark_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.experiment_acquire_dark_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.experiment_acquire_emission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.experiment_acquire_emission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.experiment_acquire_emission_spectrum_button.setObjectName("experiment_acquire_emission_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.experiment_acquire_emission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.experiment_acquire_reference_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.experiment_acquire_reference_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.experiment_acquire_reference_spectrum_button.setObjectName("experiment_acquire_reference_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.experiment_acquire_reference_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.experiment_acquire_transmission_spectrum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.experiment_acquire_transmission_spectrum_button.setStyleSheet("background-color:#14274e;\n"
"color:white;\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;\n"
"padding: 10px;")
        self.experiment_acquire_transmission_spectrum_button.setObjectName("experiment_acquire_transmission_spectrum_button")
        self.experiment_flow_vertical_layout_2.addWidget(self.experiment_acquire_transmission_spectrum_button, 0, QtCore.Qt.AlignVCenter)
        self.experiment_flow_horizontal_layout_2.addLayout(self.experiment_flow_vertical_layout_2)
        self.experiment_flow_vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.experiment_flow_vertical_layout_3.setObjectName("experiment_flow_vertical_layout_3")
        self.experiment_check_label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.experiment_check_label_1.setText("")
        self.experiment_check_label_1.setObjectName("experiment_check_label_1")
        self.experiment_flow_vertical_layout_3.addWidget(self.experiment_check_label_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.experiment_check_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.experiment_check_label_2.setText("")
        self.experiment_check_label_2.setObjectName("experiment_check_label_2")
        self.experiment_flow_vertical_layout_3.addWidget(self.experiment_check_label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.experiment_check_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.experiment_check_label_3.setText("")
        self.experiment_check_label_3.setObjectName("experiment_check_label_3")
        self.experiment_flow_vertical_layout_3.addWidget(self.experiment_check_label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.experiment_flow_horizontal_layout_2.addLayout(self.experiment_flow_vertical_layout_3)
        self.experiment_menu_frame = QtWidgets.QFrame(self.main_menu_experiment_tab)
        self.experiment_menu_frame.setGeometry(QtCore.QRect(213, 36, 241, 31))
        self.experiment_menu_frame.setStyleSheet("border-width: 0px;\n"
"border-style:solid;\n"
"")
        self.experiment_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.experiment_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.experiment_menu_frame.setObjectName("experiment_menu_frame")
        self.experiment_menu_emission_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.experiment_menu_emission_button.setGeometry(QtCore.QRect(340, 40, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_menu_emission_button.setFont(font)
        self.experiment_menu_emission_button.setStyleSheet("color: #24262b;\n"
"border-bottom-width: 0px;\n"
"border-color: #24262b;\n"
"border-style:solid;")
        self.experiment_menu_emission_button.setObjectName("experiment_menu_emission_button")
        self.experiment_menu_transmission_button = QtWidgets.QPushButton(self.main_menu_experiment_tab)
        self.experiment_menu_transmission_button.setGeometry(QtCore.QRect(218, 40, 113, 32))
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
        self.main_menu_tab.addTab(self.main_menu_experiment_tab, "")
        self.main_header_frame = QtWidgets.QFrame(self.container_widget)
        self.main_header_frame.setGeometry(QtCore.QRect(-1, -1, 1271, 81))
        self.main_header_frame.setMouseTracking(True)
        self.main_header_frame.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #9ba4b4;\n"
"background-color:#14274e")
        self.main_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header_frame.setObjectName("main_header_frame")
        self.calibration_button = QtWidgets.QPushButton(self.container_widget)
        self.calibration_button.setGeometry(QtCore.QRect(511, 38, 161, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_button.setFont(font)
        self.calibration_button.setMouseTracking(True)
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
        self.spec_streamer_label = QtWidgets.QLabel(self.container_widget)
        self.spec_streamer_label.setGeometry(QtCore.QRect(451, 1, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.spec_streamer_label.setFont(font)
        self.spec_streamer_label.setMouseTracking(True)
        self.spec_streamer_label.setAutoFillBackground(False)
        self.spec_streamer_label.setStyleSheet("color:#f1f6f9;\n"
"border-width:0px;\n"
"background-color: #14274e;\n"
"padding:0px;")
        self.spec_streamer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spec_streamer_label.setObjectName("spec_streamer_label")
        self.acquisition_button = QtWidgets.QPushButton(self.container_widget)
        self.acquisition_button.setGeometry(QtCore.QRect(388, 38, 111, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.acquisition_button.setFont(font)
        self.acquisition_button.setMouseTracking(True)
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
        self.raw_plot_frame = QtWidgets.QFrame(self.container_widget)
        self.raw_plot_frame.setGeometry(QtCore.QRect(36, 465, 561, 281))
        self.raw_plot_frame.setMouseTracking(True)
        self.raw_plot_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.raw_plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_plot_frame.setObjectName("raw_plot_frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.raw_plot_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(5, 10, 541, 261))
        self.verticalLayoutWidget_2.setMouseTracking(True)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.raw_spectrum_grid_layout = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.raw_spectrum_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.raw_spectrum_grid_layout.setObjectName("raw_spectrum_grid_layout")
        self.raw_plot_i_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_i_label.setFont(font)
        self.raw_plot_i_label.setMouseTracking(True)
        self.raw_plot_i_label.setStyleSheet("color: #9ba4b4;")
        self.raw_plot_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_i_label.setWordWrap(False)
        self.raw_plot_i_label.setObjectName("raw_plot_i_label")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot_i_label, 1, 0, 1, 1)
        self.raw_plot_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_label.setFont(font)
        self.raw_plot_label.setMouseTracking(True)
        self.raw_plot_label.setStyleSheet("color: #24262b;")
        self.raw_plot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_label.setWordWrap(False)
        self.raw_plot_label.setObjectName("raw_plot_label")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot_label, 0, 1, 1, 1)
        self.raw_plot_lambda_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.raw_plot_lambda_label.setFont(font)
        self.raw_plot_lambda_label.setMouseTracking(True)
        self.raw_plot_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.raw_plot_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_plot_lambda_label.setWordWrap(False)
        self.raw_plot_lambda_label.setObjectName("raw_plot_lambda_label")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot_lambda_label, 2, 1, 1, 1)
        self.raw_plot = PlotWidget(self.verticalLayoutWidget_2)
        self.raw_plot.setMouseTracking(True)
        self.raw_plot.setObjectName("raw_plot")
        self.raw_spectrum_grid_layout.addWidget(self.raw_plot, 1, 1, 1, 1)
        self.cursor_raw_label = QtWidgets.QLabel(self.raw_plot_frame)
        self.cursor_raw_label.setGeometry(QtCore.QRect(60, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cursor_raw_label.setFont(font)
        self.cursor_raw_label.setMouseTracking(True)
        self.cursor_raw_label.setObjectName("cursor_raw_label")
        self.spec_streamer_v_label = QtWidgets.QLabel(self.container_widget)
        self.spec_streamer_v_label.setGeometry(QtCore.QRect(696, 6, 31, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.spec_streamer_v_label.setFont(font)
        self.spec_streamer_v_label.setMouseTracking(True)
        self.spec_streamer_v_label.setStyleSheet("background-color:#14274e;\n"
"font-family: helvetica;\n"
"color:#9ba4b4;")
        self.spec_streamer_v_label.setObjectName("spec_streamer_v_label")
        self.spec_it_label = QtWidgets.QLabel(self.container_widget)
        self.spec_it_label.setGeometry(QtCore.QRect(1150, 9, 141, 20))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        self.spec_it_label.setFont(font)
        self.spec_it_label.setMouseTracking(True)
        self.spec_it_label.setStyleSheet("background-color:white;\n"
"font-family: helvetica;\n"
"color:#fff;\n"
"background-color:#14274e")
        self.spec_it_label.setOpenExternalLinks(True)
        self.spec_it_label.setObjectName("spec_it_label")
        self.experiment_button = QtWidgets.QPushButton(self.container_widget)
        self.experiment_button.setGeometry(QtCore.QRect(669, 38, 161, 35))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.experiment_button.setFont(font)
        self.experiment_button.setMouseTracking(True)
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
        self.save_raw_plot_txt_button = QtWidgets.QPushButton(self.container_widget)
        self.save_raw_plot_txt_button.setGeometry(QtCore.QRect(540, 475, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_raw_plot_txt_button.setFont(font)
        self.save_raw_plot_txt_button.setMouseTracking(True)
        self.save_raw_plot_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_raw_plot_txt_button.setObjectName("save_raw_plot_txt_button")
        self.save_raw_plot_png_button = QtWidgets.QPushButton(self.container_widget)
        self.save_raw_plot_png_button.setGeometry(QtCore.QRect(497, 475, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_raw_plot_png_button.setFont(font)
        self.save_raw_plot_png_button.setMouseTracking(True)
        self.save_raw_plot_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_raw_plot_png_button.setObjectName("save_raw_plot_png_button")
        self.side_plots_frame = QtWidgets.QFrame(self.container_widget)
        self.side_plots_frame.setGeometry(QtCore.QRect(586, 89, 641, 661))
        self.side_plots_frame.setMouseTracking(True)
        self.side_plots_frame.setStyleSheet("outline-width: 0ps;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 0px;")
        self.side_plots_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_plots_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_plots_frame.setObjectName("side_plots_frame")
        self.calc_plot_2_frame = QtWidgets.QFrame(self.side_plots_frame)
        self.calc_plot_2_frame.setGeometry(QtCore.QRect(3, -8, 631, 351))
        self.calc_plot_2_frame.setMouseTracking(True)
        self.calc_plot_2_frame.setStyleSheet("")
        self.calc_plot_2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_2_frame.setObjectName("calc_plot_2_frame")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.calc_plot_2_frame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 0, 611, 341))
        self.gridLayoutWidget_5.setMouseTracking(True)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.calc_plot_2_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.calc_plot_2_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calc_plot_2_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_2_grid_layout.setObjectName("calc_plot_2_grid_layout")
        self.calc_plot_2_i_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_i_label.setFont(font)
        self.calc_plot_2_i_label.setMouseTracking(True)
        self.calc_plot_2_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_i_label.setWordWrap(False)
        self.calc_plot_2_i_label.setObjectName("calc_plot_2_i_label")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2_i_label, 3, 0, 1, 1)
        self.calc_plot_2_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_label.setFont(font)
        self.calc_plot_2_label.setMouseTracking(True)
        self.calc_plot_2_label.setStyleSheet("color: #24262b;")
        self.calc_plot_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_label.setObjectName("calc_plot_2_label")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2_label, 2, 1, 1, 1)
        self.calc_plot_2_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_lambda_label.setFont(font)
        self.calc_plot_2_lambda_label.setMouseTracking(True)
        self.calc_plot_2_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_lambda_label.setWordWrap(False)
        self.calc_plot_2_lambda_label.setObjectName("calc_plot_2_lambda_label")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2_lambda_label, 4, 1, 1, 1)
        self.calc_plot_2 = PlotWidget(self.gridLayoutWidget_5)
        self.calc_plot_2.setEnabled(False)
        self.calc_plot_2.setMouseTracking(True)
        self.calc_plot_2.setObjectName("calc_plot_2")
        self.calc_plot_2_grid_layout.addWidget(self.calc_plot_2, 3, 1, 1, 1)
        self.save_calc_plot_1_txt_button = QtWidgets.QPushButton(self.side_plots_frame)
        self.save_calc_plot_1_txt_button.setGeometry(QtCore.QRect(583, 4, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_1_txt_button.setFont(font)
        self.save_calc_plot_1_txt_button.setMouseTracking(True)
        self.save_calc_plot_1_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_1_txt_button.setObjectName("save_calc_plot_1_txt_button")
        self.save_calc_plot_2_png_button = QtWidgets.QPushButton(self.side_plots_frame)
        self.save_calc_plot_2_png_button.setGeometry(QtCore.QRect(540, 180, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_2_png_button.setFont(font)
        self.save_calc_plot_2_png_button.setMouseTracking(True)
        self.save_calc_plot_2_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_2_png_button.setObjectName("save_calc_plot_2_png_button")
        self.calc_plot_1_frame = QtWidgets.QFrame(self.side_plots_frame)
        self.calc_plot_1_frame.setGeometry(QtCore.QRect(3, 2, 631, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_plot_1_frame.sizePolicy().hasHeightForWidth())
        self.calc_plot_1_frame.setSizePolicy(sizePolicy)
        self.calc_plot_1_frame.setMouseTracking(True)
        self.calc_plot_1_frame.setStyleSheet("")
        self.calc_plot_1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_1_frame.setObjectName("calc_plot_1_frame")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.calc_plot_1_frame)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 0, 611, 341))
        self.gridLayoutWidget_6.setMouseTracking(True)
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.calc_plot_1_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.calc_plot_1_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calc_plot_1_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_1_grid_layout.setObjectName("calc_plot_1_grid_layout")
        self.calc_plot_1_i_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_i_label.setFont(font)
        self.calc_plot_1_i_label.setMouseTracking(True)
        self.calc_plot_1_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_i_label.setWordWrap(False)
        self.calc_plot_1_i_label.setObjectName("calc_plot_1_i_label")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1_i_label, 1, 0, 1, 1)
        self.calc_plot_1_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_label.setFont(font)
        self.calc_plot_1_label.setMouseTracking(True)
        self.calc_plot_1_label.setStyleSheet("color: #24262b;")
        self.calc_plot_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_label.setObjectName("calc_plot_1_label")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1_label, 0, 1, 1, 1)
        self.calc_plot_1_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.calc_plot_1_lambda_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_lambda_label.setFont(font)
        self.calc_plot_1_lambda_label.setMouseTracking(True)
        self.calc_plot_1_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_lambda_label.setWordWrap(False)
        self.calc_plot_1_lambda_label.setObjectName("calc_plot_1_lambda_label")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1_lambda_label, 2, 1, 1, 1)
        self.calc_plot_1 = PlotWidget(self.gridLayoutWidget_6)
        self.calc_plot_1.setEnabled(False)
        self.calc_plot_1.setMouseTracking(True)
        self.calc_plot_1.setObjectName("calc_plot_1")
        self.calc_plot_1_grid_layout.addWidget(self.calc_plot_1, 1, 1, 1, 1)
        self.calc_plot_3_frame = QtWidgets.QFrame(self.side_plots_frame)
        self.calc_plot_3_frame.setGeometry(QtCore.QRect(3, 365, 631, 291))
        self.calc_plot_3_frame.setMouseTracking(True)
        self.calc_plot_3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_3_frame.setObjectName("calc_plot_3_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.calc_plot_3_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 591, 261))
        self.verticalLayoutWidget.setMouseTracking(True)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.calc_plot_3_grid_layout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.calc_plot_3_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_3_grid_layout.setObjectName("calc_plot_3_grid_layout")
        self.calc_plot_3_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_label.setFont(font)
        self.calc_plot_3_label.setMouseTracking(True)
        self.calc_plot_3_label.setStyleSheet("color: #24262b;")
        self.calc_plot_3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_label.setObjectName("calc_plot_3_label")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3_label, 6, 1, 1, 1)
        self.calc_plot_3_lambda_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_lambda_label.setFont(font)
        self.calc_plot_3_lambda_label.setMouseTracking(True)
        self.calc_plot_3_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_3_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_lambda_label.setWordWrap(False)
        self.calc_plot_3_lambda_label.setObjectName("calc_plot_3_lambda_label")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3_lambda_label, 8, 1, 1, 1)
        self.calc_plot_3_i_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_3_i_label.setFont(font)
        self.calc_plot_3_i_label.setMouseTracking(True)
        self.calc_plot_3_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_3_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_3_i_label.setWordWrap(False)
        self.calc_plot_3_i_label.setObjectName("calc_plot_3_i_label")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3_i_label, 7, 0, 1, 1)
        self.calc_plot_3 = PlotWidget(self.verticalLayoutWidget)
        self.calc_plot_3.setEnabled(True)
        self.calc_plot_3.setMouseTracking(True)
        self.calc_plot_3.setObjectName("calc_plot_3")
        self.calc_plot_3_grid_layout.addWidget(self.calc_plot_3, 7, 1, 1, 1)
        self.cursor_calc_3_label = QtWidgets.QLabel(self.calc_plot_3_frame)
        self.cursor_calc_3_label.setGeometry(QtCore.QRect(90, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cursor_calc_3_label.setFont(font)
        self.cursor_calc_3_label.setMouseTracking(True)
        self.cursor_calc_3_label.setObjectName("cursor_calc_3_label")
        self.calc_plot_1_2_combo_frame = QtWidgets.QFrame(self.side_plots_frame)
        self.calc_plot_1_2_combo_frame.setGeometry(QtCore.QRect(3, -8, 631, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_plot_1_2_combo_frame.sizePolicy().hasHeightForWidth())
        self.calc_plot_1_2_combo_frame.setSizePolicy(sizePolicy)
        self.calc_plot_1_2_combo_frame.setMouseTracking(True)
        self.calc_plot_1_2_combo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calc_plot_1_2_combo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calc_plot_1_2_combo_frame.setObjectName("calc_plot_1_2_combo_frame")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.calc_plot_1_2_combo_frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(29, 10, 591, 341))
        self.gridLayoutWidget_4.setMouseTracking(True)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.calc_plot_1_2_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.calc_plot_1_2_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.calc_plot_1_2_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.calc_plot_1_2_grid_layout.setObjectName("calc_plot_1_2_grid_layout")
        self.calc_plot_2_combo_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_combo_label.setFont(font)
        self.calc_plot_2_combo_label.setMouseTracking(True)
        self.calc_plot_2_combo_label.setStyleSheet("color: #24262b;")
        self.calc_plot_2_combo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_combo_label.setObjectName("calc_plot_2_combo_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo_label, 5, 1, 1, 1)
        self.calc_plot_2_combo_i_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_combo_i_label.setFont(font)
        self.calc_plot_2_combo_i_label.setMouseTracking(True)
        self.calc_plot_2_combo_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_combo_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_combo_i_label.setWordWrap(False)
        self.calc_plot_2_combo_i_label.setObjectName("calc_plot_2_combo_i_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo_i_label, 6, 0, 1, 1)
        self.calc_plot_1_combo_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_combo_label.setFont(font)
        self.calc_plot_1_combo_label.setMouseTracking(True)
        self.calc_plot_1_combo_label.setStyleSheet("color: #24262b;")
        self.calc_plot_1_combo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_combo_label.setObjectName("calc_plot_1_combo_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo_label, 0, 1, 1, 1)
        self.calc_plot_1_combo_i_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_combo_i_label.setFont(font)
        self.calc_plot_1_combo_i_label.setMouseTracking(True)
        self.calc_plot_1_combo_i_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_combo_i_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_combo_i_label.setWordWrap(False)
        self.calc_plot_1_combo_i_label.setObjectName("calc_plot_1_combo_i_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo_i_label, 1, 0, 1, 1)
        self.calc_plot_1_combo_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.calc_plot_1_combo_lambda_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_1_combo_lambda_label.setFont(font)
        self.calc_plot_1_combo_lambda_label.setMouseTracking(True)
        self.calc_plot_1_combo_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_1_combo_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_1_combo_lambda_label.setWordWrap(False)
        self.calc_plot_1_combo_lambda_label.setObjectName("calc_plot_1_combo_lambda_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo_lambda_label, 2, 1, 1, 1)
        self.calc_plot_2_combo_lambda_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calc_plot_2_combo_lambda_label.setFont(font)
        self.calc_plot_2_combo_lambda_label.setMouseTracking(True)
        self.calc_plot_2_combo_lambda_label.setStyleSheet("color: #9ba4b4;")
        self.calc_plot_2_combo_lambda_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_plot_2_combo_lambda_label.setWordWrap(False)
        self.calc_plot_2_combo_lambda_label.setObjectName("calc_plot_2_combo_lambda_label")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo_lambda_label, 7, 1, 1, 1)
        self.calc_plot_1_combo = PlotWidget(self.gridLayoutWidget_4)
        self.calc_plot_1_combo.setEnabled(False)
        self.calc_plot_1_combo.setMouseTracking(True)
        self.calc_plot_1_combo.setObjectName("calc_plot_1_combo")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_1_combo, 1, 1, 1, 1)
        self.calc_plot_2_combo = PlotWidget(self.gridLayoutWidget_4)
        self.calc_plot_2_combo.setEnabled(False)
        self.calc_plot_2_combo.setMouseTracking(True)
        self.calc_plot_2_combo.setObjectName("calc_plot_2_combo")
        self.calc_plot_1_2_grid_layout.addWidget(self.calc_plot_2_combo, 6, 1, 1, 1)
        self.save_calc_plot_3_txt_button = QtWidgets.QPushButton(self.side_plots_frame)
        self.save_calc_plot_3_txt_button.setGeometry(QtCore.QRect(583, 386, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_3_txt_button.setFont(font)
        self.save_calc_plot_3_txt_button.setMouseTracking(True)
        self.save_calc_plot_3_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_3_txt_button.setObjectName("save_calc_plot_3_txt_button")
        self.save_calc_plot_3_png_button = QtWidgets.QPushButton(self.side_plots_frame)
        self.save_calc_plot_3_png_button.setGeometry(QtCore.QRect(540, 386, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_3_png_button.setFont(font)
        self.save_calc_plot_3_png_button.setMouseTracking(True)
        self.save_calc_plot_3_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_3_png_button.setObjectName("save_calc_plot_3_png_button")
        self.save_calc_plot_1_png_button = QtWidgets.QPushButton(self.side_plots_frame)
        self.save_calc_plot_1_png_button.setGeometry(QtCore.QRect(540, 4, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_1_png_button.setFont(font)
        self.save_calc_plot_1_png_button.setMouseTracking(True)
        self.save_calc_plot_1_png_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_1_png_button.setObjectName("save_calc_plot_1_png_button")
        self.save_calc_plot_2_txt_button = QtWidgets.QPushButton(self.side_plots_frame)
        self.save_calc_plot_2_txt_button.setGeometry(QtCore.QRect(583, 180, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_calc_plot_2_txt_button.setFont(font)
        self.save_calc_plot_2_txt_button.setMouseTracking(True)
        self.save_calc_plot_2_txt_button.setStyleSheet("background-color:#9ba4b4;\n"
"color:white;\n"
"border-radius: 1px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #626470;")
        self.save_calc_plot_2_txt_button.setObjectName("save_calc_plot_2_txt_button")
        self.calc_plot_2_frame.raise_()
        self.calc_plot_1_frame.raise_()
        self.calc_plot_3_frame.raise_()
        self.calc_plot_1_2_combo_frame.raise_()
        self.save_calc_plot_3_txt_button.raise_()
        self.save_calc_plot_3_png_button.raise_()
        self.save_calc_plot_1_png_button.raise_()
        self.save_calc_plot_2_txt_button.raise_()
        self.save_calc_plot_1_txt_button.raise_()
        self.save_calc_plot_2_png_button.raise_()
        self.scrollArea.setWidget(self.container_widget)

        self.retranslateUi(Form)
        self.main_menu_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.detector_gain_input, self.detector_averages_input)
        Form.setTabOrder(self.detector_averages_input, self.detector_integration_time_input)
        Form.setTabOrder(self.detector_integration_time_input, self.detector_width_input)
        Form.setTabOrder(self.detector_width_input, self.detector_height_input)
        Form.setTabOrder(self.detector_height_input, self.spectrum_rotation_global_input)
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
        self.load_acquisition_settings_button.setText(_translate("Form", "Load"))
        self.save_acquisition_settings_button.setText(_translate("Form", "Save"))
        self.spectrometer_name_label.setText(_translate("Form", "Spectrometer name"))
        self.spectrometer_name_input.setText(_translate("Form", "ELP"))
        self.spectrum_rotation_global_input.setText(_translate("Form", "0"))
        self.spectrum_rotation_spectrum_input.setText(_translate("Form", "0"))
        self.spectrum_start_x_input.setText(_translate("Form", "750"))
        self.spectrum_stop_x_input.setText(_translate("Form", "1230"))
        self.spectrum_line_input.setText(_translate("Form", "500"))
        self.spectrum_lines_input.setText(_translate("Form", "5"))
        self.apply_acquisition_settings_button.setText(_translate("Form", "Apply settings"))
        self.image_settings_label.setText(_translate("Form", "Image"))
        self.detector_settings_label.setText(_translate("Form", "Detector"))
        self.spectrum_settings_label.setText(_translate("Form", "Spectrum config"))
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
        self.live_button.setText(_translate("Form", "Live"))
        self.spectrum_rotation_global_label.setText(_translate("Form", "Rotation global:"))
        self.spectrum_rotation_spectrum_label.setText(_translate("Form", "Rotation spectrum:"))
        self.spectrum_start_x_label.setText(_translate("Form", "Start (x-val):"))
        self.spectrum_stop_x_label.setText(_translate("Form", "Stop (x-val):"))
        self.spectrum_line_label.setText(_translate("Form", "Line (y-val):"))
        self.spectrum_lines_label.setText(_translate("Form", "No of lines:"))
        self.cursor_overview_label.setText(_translate("Form", "Cursor position"))
        self.image_camera_no_input.setText(_translate("Form", "0"))
        self.image_camera_no_label.setText(_translate("Form", "Camera #:"))
        self.image_downsampling_overview_input.setText(_translate("Form", "0.5"))
        self.image_downsampling_overview_label.setText(_translate("Form", "Downsampling"))
        self.clear_calibration_button.setText(_translate("Form", "Clear"))
        self.save_calibration_button.setText(_translate("Form", "Save"))
        self.load_calibration_button.setText(_translate("Form", "Load"))
        self.calibration_next_button.setText(_translate("Form", ">"))
        self.calibration_step_1_label.setText(_translate("Form", "Acquire spectra"))
        self.calibration_step_2_label.setText(_translate("Form", "Identify peaks "))
        self.calibration_step_3_label.setText(_translate("Form", "Get projection"))
        self.calibration_no_1_label.setText(_translate("Form", "1."))
        self.calibration_no_2_label.setText(_translate("Form", "2."))
        self.calibration_no_3_label.setText(_translate("Form", "3."))
        self.calibration_acquire_dark_spectrum_button.setText(_translate("Form", "Dark spectrum"))
        self.calibration_acquire_emission_spectrum_button.setText(_translate("Form", "Emission spectrum"))
        self.calibration_acquire_reference_spectrum_button.setText(_translate("Form", "Reference spectrum"))
        self.calibration_acquire_transmission_spectrum_button.setText(_translate("Form", "Transmission spectrum"))
        self.pixel_input_label.setText(_translate("Form", "Pixel #:"))
        self.wavelength_input_label.setText(_translate("Form", "Wavelength (nm):"))
        self.add_pixel_wavelength_point_button.setText(_translate("Form", "Add"))
        self.pixel_input_label_2.setText(_translate("Form", "Pixel"))
        self.wavelength_input_label_2.setText(_translate("Form", "Wavelength"))
        self.calibration_back_button.setText(_translate("Form", "<"))
        self.pixel_wavelength_polynomial_label.setText(_translate("Form", "λ(p) = A+B*p+C*p^2+D*p^3"))
        self.pixel_wavelength_polynomial_coeffs_a_label.setText(_translate("Form", "Coefficient A"))
        self.pixel_wavelength_polynomial_coeffs_b_label.setText(_translate("Form", "Coefficient B"))
        self.pixel_wavelength_polynomial_coeffs_c_label.setText(_translate("Form", "Coefficient C"))
        self.pixel_wavelength_polynomial_coeffs_d_label.setText(_translate("Form", "Coefficient D"))
        self.black_body_temperature_input_label.setText(_translate("Form", "Black-body temperature (K):"))
        self.black_body_stats_label.setText(_translate("Form", "Fit statistics"))
        self.calibration_menu_pixel_wavelength_button.setText(_translate("Form", "Pixel-Wavelength"))
        self.calibration_menu_spectral_sensitivity_button.setText(_translate("Form", "Spectral sensitivity"))
        self.main_menu_tab.setTabText(self.main_menu_tab.indexOf(self.main_menu_calibration_tab), _translate("Form", "Page"))
        self.clear_experiment_button.setText(_translate("Form", "Clear"))
        self.export_experiment_button.setText(_translate("Form", "Export experiment"))
        self.experiment_no_1_label.setText(_translate("Form", "1."))
        self.experiment_no_2_label.setText(_translate("Form", "2."))
        self.experiment_no_3_label.setText(_translate("Form", "3."))
        self.experiment_acquire_dark_spectrum_button.setText(_translate("Form", "Dark spectrum"))
        self.experiment_acquire_emission_spectrum_button.setText(_translate("Form", "Emission spectrum"))
        self.experiment_acquire_reference_spectrum_button.setText(_translate("Form", "Reference spectrum"))
        self.experiment_acquire_transmission_spectrum_button.setText(_translate("Form", "Transmission spectrum"))
        self.experiment_menu_emission_button.setText(_translate("Form", "Emission"))
        self.experiment_menu_transmission_button.setText(_translate("Form", "Transmission"))
        self.calibration_button.setText(_translate("Form", "Calibration"))
        self.spec_streamer_label.setText(_translate("Form", "spec-streamer"))
        self.acquisition_button.setText(_translate("Form", "Acquisition"))
        self.raw_plot_i_label.setText(_translate("Form", "I"))
        self.raw_plot_label.setText(_translate("Form", "Raw spectrum"))
        self.raw_plot_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.cursor_raw_label.setText(_translate("Form", "Cursor position"))
        self.spec_streamer_v_label.setText(_translate("Form", "v1.0"))
        self.spec_it_label.setText(_translate("Form", "spec-it.org"))
        self.experiment_button.setText(_translate("Form", "Experiment"))
        self.save_raw_plot_txt_button.setText(_translate("Form", ".txt"))
        self.save_raw_plot_png_button.setText(_translate("Form", ".png"))
        self.calc_plot_2_i_label.setText(_translate("Form", "I"))
        self.calc_plot_2_label.setText(_translate("Form", "Reference"))
        self.calc_plot_2_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.save_calc_plot_1_txt_button.setText(_translate("Form", ".txt"))
        self.save_calc_plot_2_png_button.setText(_translate("Form", ".png"))
        self.calc_plot_1_i_label.setText(_translate("Form", "I"))
        self.calc_plot_1_label.setText(_translate("Form", "Dark"))
        self.calc_plot_1_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_3_label.setText(_translate("Form", "Transmission"))
        self.calc_plot_3_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_3_i_label.setText(_translate("Form", "I"))
        self.cursor_calc_3_label.setText(_translate("Form", "Cursor position"))
        self.calc_plot_2_combo_label.setText(_translate("Form", "Reference"))
        self.calc_plot_2_combo_i_label.setText(_translate("Form", "I"))
        self.calc_plot_1_combo_label.setText(_translate("Form", "Dark"))
        self.calc_plot_1_combo_i_label.setText(_translate("Form", "I"))
        self.calc_plot_1_combo_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.calc_plot_2_combo_lambda_label.setText(_translate("Form", "λ (nm)"))
        self.save_calc_plot_3_txt_button.setText(_translate("Form", ".txt"))
        self.save_calc_plot_3_png_button.setText(_translate("Form", ".png"))
        self.save_calc_plot_1_png_button.setText(_translate("Form", ".png"))
        self.save_calc_plot_2_txt_button.setText(_translate("Form", ".txt"))


from pyqtgraph import GraphicsLayoutWidget, PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
