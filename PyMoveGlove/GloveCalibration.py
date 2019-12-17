from PyQt5 import QtWidgets
from Forms.GloveCalibration import Ui_GloveCalibration

class GloveCalibration(QtWidgets.QWidget):

    def __init__(self):
        super(GloveCalibration, self).__init__()
        self.ui = Ui_GloveCalibration()
        self.ui.setupUi(self)