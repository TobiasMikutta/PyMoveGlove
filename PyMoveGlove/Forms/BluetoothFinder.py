# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BluetoothFinder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BluetoothFinder(object):
    def setupUi(self, BluetoothFinder):
        BluetoothFinder.setObjectName("BluetoothFinder")
        BluetoothFinder.resize(516, 85)
        self.formLayout = QtWidgets.QFormLayout(BluetoothFinder)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.Search_pushButton = QtWidgets.QPushButton(BluetoothFinder)
        self.Search_pushButton.setObjectName("Search_pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Search_pushButton)
        self.comboBox = QtWidgets.QComboBox(BluetoothFinder)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.Connect_pushButton = QtWidgets.QPushButton(BluetoothFinder)
        self.Connect_pushButton.setObjectName("Connect_pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Connect_pushButton)

        self.retranslateUi(BluetoothFinder)
        QtCore.QMetaObject.connectSlotsByName(BluetoothFinder)

    def retranslateUi(self, BluetoothFinder):
        _translate = QtCore.QCoreApplication.translate
        BluetoothFinder.setWindowTitle(_translate("BluetoothFinder", "BluetoothFinder"))
        self.Search_pushButton.setText(_translate("BluetoothFinder", "Search"))
        self.Connect_pushButton.setText(_translate("BluetoothFinder", "Connect"))
