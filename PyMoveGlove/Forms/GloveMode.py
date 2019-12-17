# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GloveMode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GloveMode(object):
    def setupUi(self, GloveMode):
        GloveMode.setObjectName("GloveMode")
        GloveMode.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(GloveMode)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.apply_pushButton = QtWidgets.QPushButton(GloveMode)
        self.apply_pushButton.setObjectName("apply_pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.apply_pushButton)
        self.mode_comboBox = QtWidgets.QComboBox(GloveMode)
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mode_comboBox)
        self.Date_time_label = QtWidgets.QLabel(GloveMode)
        self.Date_time_label.setObjectName("Date_time_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Date_time_label)

        self.retranslateUi(GloveMode)
        QtCore.QMetaObject.connectSlotsByName(GloveMode)

    def retranslateUi(self, GloveMode):
        _translate = QtCore.QCoreApplication.translate
        GloveMode.setWindowTitle(_translate("GloveMode", "GloveMode"))
        self.apply_pushButton.setText(_translate("GloveMode", "Apply Mode"))
        self.Date_time_label.setText(_translate("GloveMode", "TextLabel"))
