# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MoveGlove.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MoveGloveClass(object):
    def setupUi(self, MoveGloveClass):
        MoveGloveClass.setObjectName("MoveGloveClass")
        MoveGloveClass.resize(1039, 856)
        self.centralWidget = QtWidgets.QWidget(MoveGloveClass)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.MyTime_label = QtWidgets.QLabel(self.centralWidget)
        self.MyTime_label.setObjectName("MyTime_label")
        self.gridLayout.addWidget(self.MyTime_label, 0, 0, 1, 1)
        MoveGloveClass.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MoveGloveClass)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1039, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuBluetooth = QtWidgets.QMenu(self.menuBar)
        self.menuBluetooth.setObjectName("menuBluetooth")
        MoveGloveClass.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MoveGloveClass)
        self.mainToolBar.setObjectName("mainToolBar")
        MoveGloveClass.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MoveGloveClass)
        self.statusBar.setObjectName("statusBar")
        MoveGloveClass.setStatusBar(self.statusBar)
        self.actionSearch = QtWidgets.QAction(MoveGloveClass)
        self.actionSearch.setObjectName("actionSearch")
        self.menuBluetooth.addAction(self.actionSearch)
        self.menuBar.addAction(self.menuBluetooth.menuAction())

        self.retranslateUi(MoveGloveClass)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MoveGloveClass)

    def retranslateUi(self, MoveGloveClass):
        _translate = QtCore.QCoreApplication.translate
        MoveGloveClass.setWindowTitle(_translate("MoveGloveClass", "MoveGlove"))
        self.MyTime_label.setText(_translate("MoveGloveClass", "TextLabel"))
        self.menuBluetooth.setTitle(_translate("MoveGloveClass", "Bluetooth"))
        self.actionSearch.setText(_translate("MoveGloveClass", "Search"))
#import MoveGlove_rc
