#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow

##
# @brief File that start application
#

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())
