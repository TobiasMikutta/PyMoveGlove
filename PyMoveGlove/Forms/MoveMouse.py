# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MoveMouse.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MoveMouse(object):
    def setupUi(self, MoveMouse):
        MoveMouse.setObjectName("MoveMouse")
        MoveMouse.resize(330, 185)
        self.gridLayout = QtWidgets.QGridLayout(MoveMouse)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.right_pushButton = QtWidgets.QPushButton(MoveMouse)
        self.right_pushButton.setObjectName("right_pushButton")
        self.gridLayout.addWidget(self.right_pushButton, 2, 3, 1, 1)
        self.up_pushButton = QtWidgets.QPushButton(MoveMouse)
        self.up_pushButton.setObjectName("up_pushButton")
        self.gridLayout.addWidget(self.up_pushButton, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.left_pushButton = QtWidgets.QPushButton(MoveMouse)
        self.left_pushButton.setObjectName("left_pushButton")
        self.gridLayout.addWidget(self.left_pushButton, 2, 1, 1, 1)
        self.down_pushButton = QtWidgets.QPushButton(MoveMouse)
        self.down_pushButton.setObjectName("down_pushButton")
        self.gridLayout.addWidget(self.down_pushButton, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 4, 1, 1)

        self.retranslateUi(MoveMouse)
        QtCore.QMetaObject.connectSlotsByName(MoveMouse)
        MoveMouse.setTabOrder(self.up_pushButton, self.right_pushButton)
        MoveMouse.setTabOrder(self.right_pushButton, self.left_pushButton)
        MoveMouse.setTabOrder(self.left_pushButton, self.down_pushButton)

    def retranslateUi(self, MoveMouse):
        _translate = QtCore.QCoreApplication.translate
        MoveMouse.setWindowTitle(_translate("MoveMouse", "MoveMouse"))
        self.right_pushButton.setText(_translate("MoveMouse", "Right"))
        self.right_pushButton.setShortcut(_translate("MoveMouse", "Ctrl+D"))
        self.up_pushButton.setText(_translate("MoveMouse", "Up"))
        self.up_pushButton.setShortcut(_translate("MoveMouse", "Ctrl+W"))
        self.left_pushButton.setText(_translate("MoveMouse", "Left"))
        self.left_pushButton.setShortcut(_translate("MoveMouse", "Ctrl+A"))
        self.down_pushButton.setText(_translate("MoveMouse", "Down"))
        self.down_pushButton.setShortcut(_translate("MoveMouse", "Ctrl+S", "Ctrl+S"))
