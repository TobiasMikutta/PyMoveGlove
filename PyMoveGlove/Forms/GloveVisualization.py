# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GloveVisualization.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GloveVisualization(object):
    def setupUi(self, GloveVisualization):
        GloveVisualization.setObjectName("GloveVisualization")
        GloveVisualization.resize(285, 249)
        self.formLayout = QtWidgets.QFormLayout(GloveVisualization)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.Connect_PushButton = QtWidgets.QPushButton(GloveVisualization)
        self.Connect_PushButton.setObjectName("Connect_PushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Connect_PushButton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.Accelero_label = QtWidgets.QLabel(GloveVisualization)
        self.Accelero_label.setObjectName("Accelero_label")
        self.gridLayout.addWidget(self.Accelero_label, 0, 1, 1, 1)
        self.GyroX_checkBox = QtWidgets.QCheckBox(GloveVisualization)
        self.GyroX_checkBox.setChecked(True)
        self.GyroX_checkBox.setObjectName("GyroX_checkBox")
        self.gridLayout.addWidget(self.GyroX_checkBox, 1, 0, 1, 1)
        self.AcceleroX_checkBox = QtWidgets.QCheckBox(GloveVisualization)
        self.AcceleroX_checkBox.setChecked(True)
        self.AcceleroX_checkBox.setObjectName("AcceleroX_checkBox")
        self.gridLayout.addWidget(self.AcceleroX_checkBox, 1, 1, 1, 1)
        self.GyroY_checkBox = QtWidgets.QCheckBox(GloveVisualization)
        self.GyroY_checkBox.setChecked(True)
        self.GyroY_checkBox.setObjectName("GyroY_checkBox")
        self.gridLayout.addWidget(self.GyroY_checkBox, 2, 0, 1, 1)
        self.Gyro_label = QtWidgets.QLabel(GloveVisualization)
        self.Gyro_label.setObjectName("Gyro_label")
        self.gridLayout.addWidget(self.Gyro_label, 0, 0, 1, 1)
        self.GyroZ_checkBox = QtWidgets.QCheckBox(GloveVisualization)
        self.GyroZ_checkBox.setChecked(True)
        self.GyroZ_checkBox.setObjectName("GyroZ_checkBox")
        self.gridLayout.addWidget(self.GyroZ_checkBox, 3, 0, 1, 1)
        self.AcceleroY_checkBox = QtWidgets.QCheckBox(GloveVisualization)
        self.AcceleroY_checkBox.setChecked(True)
        self.AcceleroY_checkBox.setObjectName("AcceleroY_checkBox")
        self.gridLayout.addWidget(self.AcceleroY_checkBox, 2, 1, 1, 1)
        self.AcceleroZ_checkBox = QtWidgets.QCheckBox(GloveVisualization)
        self.AcceleroZ_checkBox.setChecked(True)
        self.AcceleroZ_checkBox.setObjectName("AcceleroZ_checkBox")
        self.gridLayout.addWidget(self.AcceleroZ_checkBox, 3, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)

        self.retranslateUi(GloveVisualization)
        QtCore.QMetaObject.connectSlotsByName(GloveVisualization)

    def retranslateUi(self, GloveVisualization):
        _translate = QtCore.QCoreApplication.translate
        GloveVisualization.setWindowTitle(_translate("GloveVisualization", "GloveVisualization"))
        self.Connect_PushButton.setText(_translate("GloveVisualization", "Connect to Glove"))
        self.Accelero_label.setText(_translate("GloveVisualization", "Accelero"))
        self.GyroX_checkBox.setText(_translate("GloveVisualization", "X"))
        self.AcceleroX_checkBox.setText(_translate("GloveVisualization", "X"))
        self.GyroY_checkBox.setText(_translate("GloveVisualization", "Y"))
        self.Gyro_label.setText(_translate("GloveVisualization", "Gyro"))
        self.GyroZ_checkBox.setText(_translate("GloveVisualization", "Z"))
        self.AcceleroY_checkBox.setText(_translate("GloveVisualization", "Y"))
        self.AcceleroZ_checkBox.setText(_translate("GloveVisualization", "Z"))
