# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

##
# @brief Half generated user interface
#

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setWindowIcon(QtGui.QIcon("calcIcon.ico"))
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(34, 167, 255);")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(103, 215, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"qproperty-alignment: \'AlignVCenter | AlignRight\';")
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.pushButton_root = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_root.setGeometry(QtCore.QRect(240, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_root.setFont(font)
        self.pushButton_root.setMouseTracking(False)
        self.pushButton_root.setStyleSheet("QPushButton:pressed {\n"
"background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_root.setCheckable(False)
        self.pushButton_root.setChecked(False)
        self.pushButton_root.setAutoRepeat(False)
        self.pushButton_root.setAutoExclusive(False)
        self.pushButton_root.setAutoDefault(False)
        self.pushButton_root.setDefault(False)
        self.pushButton_root.setFlat(False)
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(120, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setMouseTracking(False)
        self.pushButton_equal.setStyleSheet("QPushButton:pressed {\n"
"background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_equal.setCheckable(False)
        self.pushButton_equal.setChecked(False)
        self.pushButton_equal.setAutoRepeat(False)
        self.pushButton_equal.setAutoExclusive(False)
        self.pushButton_equal.setAutoDefault(False)
        self.pushButton_equal.setDefault(False)
        self.pushButton_equal.setFlat(False)
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(180, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setMouseTracking(False)
        self.pushButton_plus.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_plus.setCheckable(False)
        self.pushButton_plus.setChecked(False)
        self.pushButton_plus.setAutoRepeat(False)
        self.pushButton_plus.setAutoExclusive(False)
        self.pushButton_plus.setAutoDefault(False)
        self.pushButton_plus.setDefault(False)
        self.pushButton_plus.setFlat(False)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(0, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setMouseTracking(False)
        self.pushButton_dot.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_dot.setCheckable(False)
        self.pushButton_dot.setChecked(False)
        self.pushButton_dot.setAutoRepeat(False)
        self.pushButton_dot.setAutoExclusive(False)
        self.pushButton_dot.setAutoDefault(False)
        self.pushButton_dot.setDefault(False)
        self.pushButton_dot.setFlat(False)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(60, 320, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setMouseTracking(False)
        self.pushButton_0.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_0.setCheckable(False)
        self.pushButton_0.setChecked(False)
        self.pushButton_0.setAutoRepeat(False)
        self.pushButton_0.setAutoExclusive(False)
        self.pushButton_0.setAutoDefault(False)
        self.pushButton_0.setDefault(False)
        self.pushButton_0.setFlat(False)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setMouseTracking(False)
        self.pushButton_1.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_1.setCheckable(False)
        self.pushButton_1.setChecked(False)
        self.pushButton_1.setAutoRepeat(False)
        self.pushButton_1.setAutoExclusive(False)
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_power = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_power.setGeometry(QtCore.QRect(240, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_power.setFont(font)
        self.pushButton_power.setMouseTracking(False)
        self.pushButton_power.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_power.setCheckable(False)
        self.pushButton_power.setChecked(False)
        self.pushButton_power.setAutoRepeat(False)
        self.pushButton_power.setAutoExclusive(False)
        self.pushButton_power.setAutoDefault(False)
        self.pushButton_power.setDefault(False)
        self.pushButton_power.setFlat(False)
        self.pushButton_power.setObjectName("pushButton_power")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(180, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setMouseTracking(False)
        self.pushButton_minus.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_minus.setCheckable(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_minus.setAutoRepeat(False)
        self.pushButton_minus.setAutoExclusive(False)
        self.pushButton_minus.setAutoDefault(False)
        self.pushButton_minus.setDefault(False)
        self.pushButton_minus.setFlat(False)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 200, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_factorial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_factorial.setGeometry(QtCore.QRect(240, 200, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_factorial.setFont(font)
        self.pushButton_factorial.setMouseTracking(False)
        self.pushButton_factorial.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_factorial.setCheckable(False)
        self.pushButton_factorial.setChecked(False)
        self.pushButton_factorial.setAutoRepeat(False)
        self.pushButton_factorial.setAutoExclusive(False)
        self.pushButton_factorial.setAutoDefault(False)
        self.pushButton_factorial.setDefault(False)
        self.pushButton_factorial.setFlat(False)
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 200, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(180, 200, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setMouseTracking(False)
        self.pushButton_multiply.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_multiply.setCheckable(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_multiply.setAutoRepeat(False)
        self.pushButton_multiply.setAutoExclusive(False)
        self.pushButton_multiply.setAutoDefault(False)
        self.pushButton_multiply.setDefault(False)
        self.pushButton_multiply.setFlat(False)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 200, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 140, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setAutoRepeat(False)
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_mod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mod.setGeometry(QtCore.QRect(240, 140, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mod.setFont(font)
        self.pushButton_mod.setMouseTracking(False)
        self.pushButton_mod.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_mod.setCheckable(False)
        self.pushButton_mod.setChecked(False)
        self.pushButton_mod.setAutoRepeat(False)
        self.pushButton_mod.setAutoExclusive(False)
        self.pushButton_mod.setAutoDefault(False)
        self.pushButton_mod.setDefault(False)
        self.pushButton_mod.setFlat(False)
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 140, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setAutoRepeat(False)
        self.pushButton_7.setAutoExclusive(False)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_division = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_division.setGeometry(QtCore.QRect(180, 140, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_division.setFont(font)
        self.pushButton_division.setMouseTracking(False)
        self.pushButton_division.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_division.setCheckable(False)
        self.pushButton_division.setChecked(False)
        self.pushButton_division.setAutoRepeat(False)
        self.pushButton_division.setAutoExclusive(False)
        self.pushButton_division.setAutoDefault(False)
        self.pushButton_division.setDefault(False)
        self.pushButton_division.setFlat(False)
        self.pushButton_division.setObjectName("pushButton_division")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 140, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setStyleSheet("QPushButton{"
"background-color: rgb(6, 126, 255); }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setAutoRepeat(False)
        self.pushButton_8.setAutoExclusive(False)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(0, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setMouseTracking(False)
        self.pushButton_del.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_del.setCheckable(False)
        self.pushButton_del.setChecked(False)
        self.pushButton_del.setAutoRepeat(False)
        self.pushButton_del.setAutoExclusive(False)
        self.pushButton_del.setAutoDefault(False)
        self.pushButton_del.setDefault(False)
        self.pushButton_del.setFlat(False)
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_sin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sin.setGeometry(QtCore.QRect(120, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setMouseTracking(False)
        self.pushButton_sin.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_sin.setCheckable(False)
        self.pushButton_sin.setChecked(False)
        self.pushButton_sin.setAutoRepeat(False)
        self.pushButton_sin.setAutoExclusive(False)
        self.pushButton_sin.setAutoDefault(False)
        self.pushButton_sin.setDefault(False)
        self.pushButton_sin.setFlat(False)
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.pushButton_cos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cos.setGeometry(QtCore.QRect(180, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setMouseTracking(False)
        self.pushButton_cos.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_cos.setCheckable(False)
        self.pushButton_cos.setChecked(False)
        self.pushButton_cos.setAutoRepeat(False)
        self.pushButton_cos.setAutoExclusive(False)
        self.pushButton_cos.setAutoDefault(False)
        self.pushButton_cos.setDefault(False)
        self.pushButton_cos.setFlat(False)
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(60, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setMouseTracking(False)
        self.pushButton_clear.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_clear.setCheckable(False)
        self.pushButton_clear.setChecked(False)
        self.pushButton_clear.setAutoRepeat(False)
        self.pushButton_clear.setAutoExclusive(False)
        self.pushButton_clear.setAutoDefault(False)
        self.pushButton_clear.setDefault(False)
        self.pushButton_clear.setFlat(False)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_tan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tan.setGeometry(QtCore.QRect(240, 80, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_tan.setFont(font)
        self.pushButton_tan.setMouseTracking(False)
        self.pushButton_tan.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(32, 140, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_tan.setCheckable(False)
        self.pushButton_tan.setChecked(False)
        self.pushButton_tan.setAutoRepeat(False)
        self.pushButton_tan.setAutoExclusive(False)
        self.pushButton_tan.setAutoDefault(False)
        self.pushButton_tan.setDefault(False)
        self.pushButton_tan.setFlat(False)
        self.pushButton_tan.setObjectName("pushButton_tan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(64, 210, 233);\n"
"background-color: rgb(64, 210, 233);")
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setCheckable(False)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionCredits)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

##
# @brief Function that add support of keyboard
#
# By pressing right button symbol
# display on the screen
#

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_root.setText(_translate("MainWindow", "ⁿ√"))
        self.pushButton_root.setShortcut(_translate("MainWindow", "R"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_equal.setShortcut(_translate("MainWindow", "return"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_plus.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_dot.setText(_translate("MainWindow", ","))
        self.pushButton_dot.setShortcut(_translate("MainWindow", ","))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_0.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_1.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_power.setText(_translate("MainWindow", "xⁿ"))
        self.pushButton_power.setShortcut(_translate("MainWindow", "^"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_minus.setShortcut(_translate("MainWindow", "-"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_factorial.setText(_translate("MainWindow", "x!"))
        self.pushButton_factorial.setShortcut(_translate("MainWindow", "!"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_multiply.setText(_translate("MainWindow", "⨯"))
        self.pushButton_multiply.setShortcut(_translate("MainWindow", "*"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_mod.setText(_translate("MainWindow", "Mod"))
        self.pushButton_mod.setShortcut(_translate("MainWindow", "%"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_7.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_division.setText(_translate("MainWindow", "÷"))
        self.pushButton_division.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_del.setText(_translate("MainWindow", "⬅"))
        self.pushButton_del.setShortcut(_translate("MainWindow", "backspace"))
        self.pushButton_sin.setText(_translate("MainWindow", "Sin"))
        self.pushButton_sin.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_cos.setText(_translate("MainWindow", "Cos"))
        self.pushButton_cos.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_clear.setShortcut(_translate("MainWindow", "del"))
        self.pushButton_tan.setText(_translate("MainWindow", "Tan"))
        self.pushButton_tan.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Show help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Shift+H"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionCredits.setStatusTip(_translate("MainWindow", "Show credits"))
        self.actionCredits.setShortcut(_translate("MainWindow", "Shift+C"))

        self.actionHelp.triggered.connect(self.helpWindow)
        self.actionCredits.triggered.connect(self.creditsWindow)
##
# @brief Function for help button
#
# Print out help for calculator
#
 
    def helpWindow(self):
        msg = QMessageBox()
        msg.setWindowTitle("Help")
        msg.setText('''The calculator provides basic functions of:
                                     Visual   Keyboard shortcuts
Addition -                     \"+\"           \"+\"    
Subtraction-                \"-\"            \"-\"
Multiplication -          \"⨯\"          \"*\"
Division -                      \"÷\"           \"/\"
Delete last symbol - \"⬅\"          \"Backspace\"
Clear all -                      \"C\"           \"Del\"

Advanced functions:

Factorial -                     \"x!\"           \"!\"
Root -                             \"√\"            \"R\"
Power -                          \"xⁿ\"           \"^\"

Trigonometric functions:

Sinus -                           \"Sin\"         \"Ctrl + S\"
Cosinus -                      \"Cos\"        \"Ctrl + C\"
Tangens -                     \"Tan\"        \"Ctrl + T\"

For get answer -         \"=\"            \"Enter\"
''')
        msg.setWindowIcon(QtGui.QIcon("calcIcon.ico"))
        msg.setIcon(QMessageBox.Question)

        x = msg.exec_()
##
# @brief Function for credits button
#
# Print out people that work on the project
#

    def creditsWindow(self):
        msg = QMessageBox()
        msg.setWindowTitle("Credits")
        msg.setText("Authors:\n\nMedvedev Anton\nVáclavič Jiří\nVerevkin Aleksandr\nKováčik Timotej")
        msg.setWindowIcon(QtGui.QIcon("calcIcon.ico"))
        msg.setIcon(QMessageBox.Question)

        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
