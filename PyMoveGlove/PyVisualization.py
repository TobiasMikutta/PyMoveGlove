from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import PyQt5.QtChart as QtChart
from PyQt5.QtCore import QTimer,QTime
from datetime import datetime
import random
import MoveMouse
import serial
import json
from Forms.GloveVisualization import Ui_GloveVisualization  # importing our generated file
from threading import Thread



class Visuali(QtWidgets.QWidget):

    __mouse=0
    __timer=QTimer()
    __FirstTime=0
    __useDemo=0
    __chartView = 0
    __chart = 0
    __xAxis = 0
    __yAxis = 0
    __demoX=[]
    __demoY=[]
    __demoZ=[]
    __maxY=0
    __minY=0
    __counter=0
    __acceleratorX = 0
    __acceleratorY = 0
    __acceleratorZ = 0
    __gyroX = 0
    __gyroY = 0
    __gyroZ = 0
    __AcceleroData=0
    __GyroData=1
    __X_Axis=0
    __Y_Axis=1
    __Z_Axis=2
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM4'
    ser.open()

    def __init__(self):
        super(Visuali, self).__init__()
        self.ui = Ui_GloveVisualization()
        self.ui.setupUi(self)
        self.__mouse=MoveMouse


        #self.ui.Connect_PushButton.clicked.connect(self.ConnectToGlove)
        self.ui.AcceleroX_checkBox.clicked.connect(self.__hide_show_data)
        self.ui.AcceleroY_checkBox.clicked.connect(self.__hide_show_data)
        self.ui.AcceleroZ_checkBox.clicked.connect(self.__hide_show_data)

        self.ui.GyroX_checkBox.clicked.connect(self.__hide_show_data)
        self.ui.GyroY_checkBox.clicked.connect(self.__hide_show_data)
        self.ui.GyroZ_checkBox.clicked.connect(self.__hide_show_data)

        self.__chartView = QtChart.QChartView()
        self.__chart = QtChart.QChart()
        self.__xAxis = QtChart.QValueAxis()
        self.__yAxis = QtChart.QValueAxis()
        self.__acceleratorX = QtChart.QLineSeries()
        self.__acceleratorY = QtChart.QLineSeries()
        self.__acceleratorZ = QtChart.QLineSeries()
        self.__gyroX = QtChart.QLineSeries()
        self.__gyroY = QtChart.QLineSeries()
        self.__gyroZ = QtChart.QLineSeries()

        self.__gyroX.setName("Gyro_X")
        self.__gyroY.setName("Gyro_Y")
        self.__gyroZ.setName("Gyro_Z")

        self.__acceleratorX.setName("Accelero_X")
        self.__acceleratorY.setName("Accelero_Y")
        self.__acceleratorZ.setName("Accelero_Z")

        self.__chart.addSeries(self.__gyroX)
        self.__chart.addSeries(self.__gyroY)
        self.__chart.addSeries(self.__gyroZ)
        self.__chart.addSeries(self.__acceleratorX)
        self.__chart.addSeries(self.__acceleratorY)
        self.__chart.addSeries(self.__acceleratorZ)

        self.__xAxis.setMin(0)
        self.__yAxis.setMin(-10)
        self.__yAxis.setMax(20)

        self.__chart.createDefaultAxes()
        self.__chart.setAxisX(self.__xAxis)
        self.__chart.setAxisY(self.__yAxis)

        self.__acceleratorX.attachAxis(self.__yAxis)
        self.__acceleratorY.attachAxis(self.__yAxis)
        self.__acceleratorZ.attachAxis(self.__yAxis)
        self.__acceleratorX.attachAxis(self.__xAxis)
        self.__acceleratorY.attachAxis(self.__xAxis)
        self.__acceleratorZ.attachAxis(self.__xAxis)

        self.__gyroX.attachAxis(self.__yAxis)
        self.__gyroY.attachAxis(self.__yAxis)
        self.__gyroZ.attachAxis(self.__yAxis)
        self.__gyroX.attachAxis(self.__xAxis)
        self.__gyroY.attachAxis(self.__xAxis)
        self.__gyroZ.attachAxis(self.__xAxis)

        self.__chart.setTitle("Sensordaten Handrücken")

        self.__chartView.setChart(self.__chart)
        self.ui.formLayout.addWidget(self.__chartView)
        self.__chartView.setMinimumHeight(700)
        self.__chartView.setMinimumWidth(1755)
        self.__chartView.adjustSize()
        self.ui.formLayout.update()
        self.ui.Connect_PushButton.hide()
        #self.__test()

    def uratData(self):
        line = self.ser.read_all()
        first = line
        while first == line:
            line = self.ser.read_all()
        value = self.ser.readline()
        while True:
            value = self.ser.readline()
            value = self.ser.readline()
            value = value.decode("utf-8")
            value = json.loads(value)["BMI160_ARRAY"]
            mouseX = 0
            mouseY = 0
            AcceleroDataX = 0
            AcceleroDataY = 0
            AcceleroDataZ = 0
            GyroDataX = 0
            GyroDataY = 0
            GyroDataZ = 0
            mouseX, mouseY, AcceleroDataX, AcceleroDataY, AcceleroDataZ, GyroDataX, GyroDataY, GyroDataZ = self.splitArryHandBack(value)
            self.addData(AcceleroDataX, AcceleroDataY, AcceleroDataZ, GyroDataX, GyroDataY, GyroDataZ)

    def __hide_show_data(self):
        if self.ui.AcceleroX_checkBox.isChecked():
            self.__acceleratorX.show()
        else:
            self.__acceleratorX.hide()

        if self.ui.AcceleroY_checkBox.isChecked():
            self.__acceleratorY.show()
        else:
            self.__acceleratorY.hide()

        if self.ui.AcceleroZ_checkBox.isChecked():
            self.__acceleratorZ.show()
        else:
            self.__acceleratorZ.hide()

        if self.ui.GyroX_checkBox.isChecked():
            self.__gyroX.show()
        else:
            self.__gyroX.hide()

        if self.ui.GyroY_checkBox.isChecked():
            self.__gyroY.show()
        else:
            self.__gyroY.hide()

        if self.ui.GyroZ_checkBox.isChecked():
            self.__gyroZ.show()
        else:
            self.__gyroZ.hide()

    def __demoXYZ(self):

        for i in range (0,100):
            self.__demoX.append(random.randint(-180, 180))
            self.__demoY.append(random.randint(-180, 180))
            self.__demoZ.append(random.randint(-180, 180))

    def __test(self):
        self.__demoXYZ()
        self.__timer.timeout.connect(self.__setDemoDataToSeries)
        self.__timer.setInterval(100)
        self.__timer.start()

    def __setDemoDataToSeries(self):
        time= self.__FirstTime + 0.1
        self.__FirstTime=time
        self.__moveTimeAxis(time)

        if self.__maxY<self.__demoX[self.__counter]:
            self.__maxY=self.__demoX[self.__counter]
            self.__scaleAxisY()

        if self.__maxY<self.__demoY[self.__counter]:
            self.__maxY=self.__demoY[self.__counter]
            self.__scaleAxisY()

        if self.__maxY < self.__demoZ[self.__counter]:
            self.__maxY = self.__demoZ[self.__counter]
            self.__scaleAxisY()

        if self.__minY > self.__demoX[self.__counter]:
            self.__minY = self.__demoX[self.__counter]
            self.__scaleAxisY()

        if self.__minY > self.__demoY[self.__counter]:
            self.__minY = self.__demoY[self.__counter]
            self.__scaleAxisY()

        if self.__minY > self.__demoZ[self.__counter]:
            self.__minY = self.__demoZ[self.__counter]
            self.__scaleAxisY()

        self.__acceleratorX.append(time, self.__demoX[self.__counter])
        self.__acceleratorY.append(time, self.__demoY[self.__counter])
        self.__acceleratorZ.append(time, self.__demoZ[self.__counter])

        self.__counter=random.randint(0, 99)

        self.__chart.update()
        self.__chartView.update()

    def __scaleAxisY(self):
        self.__yAxis.setMin(self.__minY - 1.0)
        self.__yAxis.setMax(self.__maxY + 1.0)

    def __moveTimeAxis(self, time):
        self.__xAxis.setMax(time + 1.0)
        if time>5.0:
            self.__xAxis.setMin(time - 5.0)

    def addData(self,AcceleroDataX,AcceleroDataY,AcceleroDataZ,GyroDataX,GyroDataY,GyroDataZ):
        time = 0
        if self.__FirstTime==0:
            self.__FirstTime=datetime.now()
        else:
            time=datetime.now()-self.__FirstTime
            time=time.total_seconds()
        self.__moveTimeAxis(time)

        grates=self.__findGratestValue(AcceleroDataX, AcceleroDataY, AcceleroDataZ, GyroDataX, GyroDataY, GyroDataZ)
        smalest=self.__findSmalestValue(AcceleroDataX, AcceleroDataY, AcceleroDataZ, GyroDataX, GyroDataY, GyroDataZ)
        if self.__maxY < grates :
            self.__maxY = grates
            self.__scaleAxisY()

        if self.__minY > smalest:
            self.__minY = smalest
            self.__scaleAxisY()

        self.__acceleratorX.append(time, AcceleroDataX)
        print("AcceleroDataX:"+str(AcceleroDataX)+" time:"+str(time))
        print("AcceleroDataY:" + str(AcceleroDataY) + " time:" + str(time))
        print("AcceleroDataZ:" + str(AcceleroDataZ) + " time:" + str(time))
        self.__acceleratorY.append(time, AcceleroDataY)
        self.__acceleratorZ.append(time, AcceleroDataZ)

        self.__gyroX.append(time, GyroDataX)
        print("GyroDataX:" + str(GyroDataX) + " time:" + str(time))
        print("GyroDataY:" + str(GyroDataY) + " time:" + str(time))
        print("GyroDataZ:" + str(GyroDataZ) + " time:" + str(time))
        self.__gyroY.append(time, GyroDataY)
        self.__gyroZ.append(time, GyroDataZ)


    def __findGratestValue(self, v1, v2, v3, v4, v5, v6):
        list={v1,v2,v3,v4,v5,v6}
        greatest=0
        for i in list:
            if i>greatest:
                greatest=i;

        #sorted(list,reverse=True)
        return greatest

    def __findSmalestValue(self, v1, v2, v3, v4, v5, v6):
        list = {v1, v2, v3, v4, v5, v6}
        smallest = 0
        for i in list:
            if i < smallest:
                smallest = i;

        # sorted(list)
        return smallest

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