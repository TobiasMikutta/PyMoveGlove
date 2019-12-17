from PyQt5 import QtWidgets
from Forms.GloveMode import Ui_GloveMode

class GloveMode(QtWidgets.QWidget):
    def __init__(self):
        super(GloveMode, self).__init__()
        self.ui = Ui_GloveMode()
        self.ui.setupUi(self)