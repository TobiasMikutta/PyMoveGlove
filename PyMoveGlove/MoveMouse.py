from PyQt5 import QtWidgets

from Forms.MoveMouse import Ui_MoveMouse
import pyautogui
import uart

class MoveMouse(QtWidgets.QWidget):
    def __init__(self):
        super(MoveMouse, self).__init__()
        self.ui = Ui_MoveMouse()
        self.ui.setupUi(self)
        self.ui.down_pushButton.clicked.connect(self.__moveDown)
        self.ui.up_pushButton.clicked.connect(self.__moveUp)
        self.ui.left_pushButton.clicked.connect(self.__moveLeft)
        self.ui.right_pushButton.clicked.connect(self.__moveRigt)

    def __moveDown(self):
        self.moveDown(100)

    def __moveUp(self):
        self.moveUp(100)

    def __moveLeft(self):
        self.moveLeft(100)

    def __moveRigt(self):
        self.moveRigt(100)

    def moveDown(self,moveBy):
        if moveBy<0:
            moveBy=moveBy*(-1)
        self.moveMouseRel(0,moveBy)

    def moveUp(self,moveBy):
        if moveBy>0:
            moveBy=moveBy*(-1)
        self.moveMouseRel(0,moveBy)

    def moveLeft(self,moveBy):
        if moveBy > 0:
            moveBy = moveBy * (-1)
        self.moveMouseRel(moveBy,0)

    def moveRigt(self,moveBy):
        if moveBy < 0:
            moveBy = moveBy * (-1)
        self.moveMouseRel(moveBy,0)

    def moveMouseRel(self,x,y):
        pyautogui.moveRel(x,y)