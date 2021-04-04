from PyQt5 import QtWidgets
from calcUi import Ui_MainWindow


class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
