from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal,QTime
from PyQt5.QtWidgets import QMessageBox
from Forms.MoveGlove import Ui_MoveGloveClass  # importing our generated file
from threading import Thread
import pygatt
import PyVisualization
import MoveMouse
import GloveMode
import GloveCalibration
import sys

class mywindow(QtWidgets.QMainWindow):
    serialPortBleUsb='COM3'
    EspMac='3c:71:bf:1c:33:c2'
    BleCharacteristics="6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

    tab=0
    tab_2=0
    tab_3=0
    tab_4=0
    adapter = pygatt.BGAPIBackend(serial_port=serialPortBleUsb)
    device = pygatt.device
    threadFinished=pyqtSignal()
    value={}
    isConnected=False
    connectionError=pyqtSignal()
    updateTime=pyqtSignal()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MoveGloveClass()
        self.ui.setupUi(self)
        #self.ui.actionSearch.triggered.connect(self.ConnectToGlove)
        self.tab = PyVisualization.Visuali()
        self.tab_2 = GloveMode.GloveMode()
        self.tab_3 = GloveCalibration.GloveCalibration()
        self.tab_4 = MoveMouse.MoveMouse()
        self.ui.tabWidget.addTab(self.tab,"Visualisierung")
        self.ui.tabWidget.addTab(self.tab_2,"GloveMode")
        self.ui.tabWidget.addTab(self.tab_3,"GloveCalibration")
        self.ui.tabWidget.addTab(self.tab_4,"MoveMouse")
        self.ui.actionSearch.setText("UART Verbindung")
        self.threadFinished.connect(self.startThred)
        #self.ui.actionSearch.triggered.connect(self.worker)
        self.ui.actionSearch.triggered.connect(self.uartWorker)
        self.connectionError.connect(self.BleErro)
        self.updateTime.connect(self.timeUpdater)
        self.adjustSize()
        self.updateTime.emit()

    def uartWorker(self):
        t = Thread(target=self.tab.uratData);
        t.start()

    def worker(self):
        if self.isConnected:
            return
        t=Thread(target=self.ConnectToGlove)
        t.start()

    def timeUpdater(self):
        t=Thread(target=self.updateMyTime)
        t.start()

    def updateMyTime(self):
        self.ui.MyTime_label.setText(QTime.currentTime().toString("hh:mm:ss.zzz"))
        self.updateTime.emit()

    def BleErro(self):
        msg = QMessageBox.question(self, 'Keine Verbindung', "Nochmal versuchen?",
                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if msg == QMessageBox.Yes:
            self.ui.actionSearch.triggered.emit()
        else:
            self.adapter.stop()

    def ConnectToGlove(self):
        if self.isConnected:
            return
        try:
            self.adapter.start()
            self.device = self.adapter.connect(self.EspMac)
        except pygatt.exceptions.NotConnectedError:
            self.isConnected = False
            self.connectionError.emit()
            return
        self.isConnected=True
        self.myThread()


    def myThread(self):
        buffer=0
        try:
            self.value = self.device.char_read(self.BleCharacteristics)
            buffer=self.value[0]
        except pygatt.exceptions.BLEError:
            self.device.disconnect()
            self.adapter.stop()
            self.isConnected=False
            return
        self.update()
        self.threadFinished.emit()

    def startThred(self):
        t=Thread(target=self.myThread)
        t.start()

    def updateData(self):
        mouseX = 0
        mouseY = 0
        AcceleroDataX = 0
        AcceleroDataY = 0
        AcceleroDataZ = 0
        GyroDataX = 0
        GyroDataY = 0
        GyroDataZ = 0
        mouseX, mouseY, AcceleroDataX, AcceleroDataY, AcceleroDataZ, GyroDataX, GyroDataY, GyroDataZ = self.splitArryHandBack(self.value)

    def splitArryHandBack(self, data):

        mouseX = 0
        mouseY = 0
        AcceleroDataX = data[3]
        AcceleroDataY = data[4]
        AcceleroDataZ = data[5]
        GyroDataX = data[0]
        GyroDataY = data[1]
        GyroDataZ = data[2]

        return mouseX, mouseY, AcceleroDataX, AcceleroDataY, AcceleroDataZ, GyroDataX, GyroDataY, GyroDataZ


#Main Window
app = QtWidgets.QApplication([])
application = mywindow()
#application.showFullScreen()
application.show()
sys.exit(app.exec())