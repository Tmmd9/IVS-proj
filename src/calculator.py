# Connection between UI and math library

from PyQt5 import QtWidgets
from calcUi import Ui_MainWindow
from mathlib import *


class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Buttons activation

        self.pushButton_0.clicked.connect(self.button_digit)
        self.pushButton_1.clicked.connect(self.button_digit)
        self.pushButton_2.clicked.connect(self.button_digit)
        self.pushButton_3.clicked.connect(self.button_digit)
        self.pushButton_4.clicked.connect(self.button_digit)
        self.pushButton_5.clicked.connect(self.button_digit)
        self.pushButton_6.clicked.connect(self.button_digit)
        self.pushButton_7.clicked.connect(self.button_digit)
        self.pushButton_8.clicked.connect(self.button_digit)
        self.pushButton_9.clicked.connect(self.button_digit)

        self.pushButton_dot.clicked.connect(self.button_decimal)

        self.pushButton_plus.clicked.connect(self.button_activate)
        self.pushButton_minus.clicked.connect(self.button_activate)
        self.pushButton_multiply.clicked.connect(self.button_activate)
        self.pushButton_division.clicked.connect(self.button_activate)

        self.pushButton_root.clicked.connect(self.button_activate)
        self.pushButton_power.clicked.connect(self.button_activate)
        self.pushButton_factorial.clicked.connect(self.button_activate)
        self.pushButton_mod.clicked.connect(self.button_activate)

        self.pushButton_cos.clicked.connect(self.button_activate)
        self.pushButton_sin.clicked.connect(self.button_activate)
        self.pushButton_tan.clicked.connect(self.button_activate)

        self.pushButton_clear.clicked.connect(self.clear_all)
        self.pushButton_del.clicked.connect(self.clear_last)

        self.pushButton_equal.clicked.connect(self.equal_activate)

# 0-9 buttons

    def button_digit(self):
        button = self.sender()

        if len(self.label.text()) <= 25:
            self.label.setText(self.label.text() + button.text())
        else:
            pass

# dot button

    def button_decimal(self):
        if len(self.label.text()) <= 24:
            if "." in self.label.text() or len(self.label.text()) == 0:
                pass
            else:
                self.label.setText(self.label.text() + ".")
        else:
            pass

# operation buttons

    def button_activate(self):
        button = self.sender()

        if button.text() == "Sin":
            self.label.setText("Sin")
        elif button.text() == "Cos":
            self.label.setText("Cos")
        elif button.text() == "Tan":
            self.label.setText("Tan")
        elif button.text() == "x!":
            self.label.setText("!")
        elif len(self.label.text()) <= 24:
            if button.text() == "-" and self.label.text().count("-") < 3:
                self.label.setText(self.label.text() + button.text())

            elif len(self.label.text()) == 0 or self.label.text()[-1] == "." \
                    or "/" in self.label.text() or "*" in self.label.text() \
                    or "+" in self.label.text() \
                    or "%" in self.label.text() or "^" in self.label.text() \
                    or "√" in self.label.text() or "!" in self.label.text() \
                    or "Cos" in self.label.text() or "Sin" in self.label.text() \
                    or "Tan" in self.label.text():

                pass

            else:

                if button.text() == "⨯":
                    self.label.setText(self.label.text() + "*")
                elif button.text() == "÷":
                    self.label.setText(self.label.text() + "/")
                elif button.text() == "+":
                    self.label.setText(self.label.text() + button.text())
                elif button.text() == "Mod":
                    self.label.setText(self.label.text() + "%")
                elif button.text() == "√":
                    self.label.setText(self.label.text() + button.text())
                elif button.text() == "xⁿ":
                    self.label.setText(self.label.text() + "^")
        else:
            pass

# erase last button

    def clear_last(self):
        new_label = self.label.text()

        self.label.setText(new_label[:-1])

# erase all button

    def clear_all(self):
        self.label.setText("")

# = button

    def equal_activate(self):

        if "-" in self.label.text():
            if "/" in self.label.text() or "*" in self.label.text() \
                    or "+" in self.label.text() \
                    or "%" in self.label.text() or "^" in self.label.text() \
                    or "√" in self.label.text() or "!" in self.label.text() \
                    or "Cos" in self.label.text() or "Sin" in self.label.text() \
                    or "Tan" in self.label.text():
                pass
            elif self.label.text().count("-") == 3:
                empty1, first_number, empty2, second_number = map(str, self.label.text().split("-"))
                answer = sub(float("-" + first_number), float("-" + second_number))
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
            elif self.label.text().count("-") == 2 and self.label.text()[0] != "-":
                first_number, empty, second_number = map(str, self.label.text().split("-"))
                answer = sub(float(first_number), float("-" + second_number))
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))

        if "+" in self.label.text():
            first_number, second_number = map(float, self.label.text().split("+"))
            answer = add(first_number, second_number)
            if int(answer) == float(answer):
                answer = int(answer)
            self.label.setText(str(answer))
        elif "*" in self.label.text():
            first_number, second_number = map(float, self.label.text().split("*"))
            answer = mul(first_number, second_number)
            if int(answer) == float(answer):
                answer = int(answer)
            self.label.setText(str(answer))
        elif "/" in self.label.text():
            first_number, second_number = map(float, self.label.text().split("/"))
            if second_number == 0:
                self.label.setText("Error: zero division")
            else:
                answer = div(first_number, second_number)
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "%" in self.label.text():
            first_number, second_number = map(float, self.label.text().split("%"))
            if float(first_number) != int(first_number):
                self.label.setText("Error: float in modulo")
            elif float(second_number) != int(second_number):
                self.label.setText("Error: float in modulo")
            elif second_number == 0:
                self.label.setText("Error: zero division")
            else:
                answer = mod(int(first_number), int(second_number))
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "^" in self.label.text():
            first_number, second_number = map(float, self.label.text().split("^"))
            if first_number == 0 and second_number < 0:
                self.label.setText("Error: raise zero to negative")
            else:
                answer = pow(first_number, second_number)
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "√" in self.label.text():
            first_number, second_number = map(float, self.label.text().split("√"))
            if first_number < 0:
                self.label.setText("Error: negative root")
            else:
                answer = root(first_number, second_number)
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "Sin" in self.label.text():
            number = self.label.text()[3:]
            answer = sin(float(number))
            if int(answer) == float(answer):
                answer = int(answer)
            self.label.setText(str(answer))
        elif "Cos" in self.label.text():
            number = self.label.text()[3:]
            answer = cos(float(number))
            if int(answer) == float(answer):
                answer = int(answer)
            self.label.setText(str(answer))
        elif "Tan" in self.label.text():
            number = self.label.text()[3:]
            answer = tan(float(number))
            if int(answer) == float(answer):
                answer = int(answer)
            self.label.setText(str(answer))
        elif "!" in self.label.text():
            number = float(self.label.text()[1:])
            if int(number) < 0:
                self.label.setText("Error: must be greater then -1")
            elif int(number) != number:
                self.label.setText("Error: value must be integer")
            else:
                answer = fact(int(number))
                self.label.setText(str(answer))
