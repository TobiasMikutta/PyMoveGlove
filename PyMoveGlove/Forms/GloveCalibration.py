# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GloveCalibration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GloveCalibration(object):
    def setupUi(self, GloveCalibration):
        GloveCalibration.setObjectName("GloveCalibration")
        GloveCalibration.resize(157, 67)
        self.formLayout = QtWidgets.QFormLayout(GloveCalibration)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.calibration_pushButton = QtWidgets.QPushButton(GloveCalibration)
        self.calibration_pushButton.setObjectName("calibration_pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.calibration_pushButton)
        self.calibration_lineEdit = QtWidgets.QLineEdit(GloveCalibration)
        self.calibration_lineEdit.setObjectName("calibration_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.calibration_lineEdit)

        self.retranslateUi(GloveCalibration)
        QtCore.QMetaObject.connectSlotsByName(GloveCalibration)

    def retranslateUi(self, GloveCalibration):
        _translate = QtCore.QCoreApplication.translate
        GloveCalibration.setWindowTitle(_translate("GloveCalibration", "GloveCalibration"))
        self.calibration_pushButton.setText(_translate("GloveCalibration", "Calibration"))
