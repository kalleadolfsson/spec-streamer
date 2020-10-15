# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 846)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(540, 10, 520, 400))
        self.image_label.setMaximumSize(QtCore.QSize(642, 16777215))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(170, 70, 181, 32))
        self.control_bt.setObjectName("control_bt")
        self.spec_plot = MplPlot(Form)
        self.spec_plot.setGeometry(QtCore.QRect(10, 420, 520, 400))
        self.spec_plot.setObjectName("spec_plot")
        self.set_averages_button = QtWidgets.QPushButton(Form)
        self.set_averages_button.setGeometry(QtCore.QRect(160, 164, 91, 32))
        self.set_averages_button.setObjectName("set_averages_button")
        self.averages_input = QtWidgets.QLineEdit(Form)
        self.averages_input.setGeometry(QtCore.QRect(87, 168, 51, 21))
        self.averages_input.setObjectName("averages_input")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 170, 60, 16))
        self.label.setObjectName("label")
        self.calc_plot = MplPlot(Form)
        self.calc_plot.setGeometry(QtCore.QRect(540, 420, 520, 400))
        self.calc_plot.setObjectName("calc_plot")
        self.dark_button = QtWidgets.QPushButton(Form)
        self.dark_button.setGeometry(QtCore.QRect(70, 250, 171, 41))
        self.dark_button.setObjectName("dark_button")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 143, 81, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 228, 91, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.reference_button = QtWidgets.QPushButton(Form)
        self.reference_button.setGeometry(QtCore.QRect(70, 290, 171, 41))
        self.reference_button.setObjectName("reference_button")
        self.sample_button = QtWidgets.QPushButton(Form)
        self.sample_button.setGeometry(QtCore.QRect(70, 330, 171, 41))
        self.sample_button.setObjectName("sample_button")
        self.dark_ok = QtWidgets.QCheckBox(Form)
        self.dark_ok.setEnabled(False)
        self.dark_ok.setGeometry(QtCore.QRect(250, 258, 31, 20))
        self.dark_ok.setText("")
        self.dark_ok.setCheckable(True)
        self.dark_ok.setObjectName("dark_ok")
        self.reference_ok = QtWidgets.QCheckBox(Form)
        self.reference_ok.setEnabled(False)
        self.reference_ok.setGeometry(QtCore.QRect(250, 299, 31, 20))
        self.reference_ok.setText("")
        self.reference_ok.setCheckable(True)
        self.reference_ok.setObjectName("reference_ok")
        self.sample_ok = QtWidgets.QCheckBox(Form)
        self.sample_ok.setEnabled(False)
        self.sample_ok.setGeometry(QtCore.QRect(250, 340, 31, 20))
        self.sample_ok.setText("")
        self.sample_ok.setCheckable(True)
        self.sample_ok.setObjectName("sample_ok")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 50, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt.setText(_translate("Form", "Live"))
        self.set_averages_button.setText(_translate("Form", "Set"))
        self.averages_input.setText(_translate("Form", "5"))
        self.label.setText(_translate("Form", "Averages:"))
        self.dark_button.setText(_translate("Form", "Dark spectrum"))
        self.label_2.setText(_translate("Form", "SETTINGS"))
        self.label_3.setText(_translate("Form", "ACQUISITION"))
        self.reference_button.setText(_translate("Form", "Reference spectrum"))
        self.sample_button.setText(_translate("Form", "Sample spectrum"))
        self.label_4.setText(_translate("Form", "Crappy spectrometer 1.0"))
        self.label_5.setText(_translate("Form", "by Karl Adolfsson"))
from mplplot import MplPlot


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
