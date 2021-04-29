from PyQt5 import QtWidgets
from calcUi import Ui_MainWindow
from mathlib import *
import string


superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"}

upper_number = str.maketrans(''.join(superscript_map.keys()),''.join(superscript_map.values()))
normal_number = str.maketrans(''.join(superscript_map.values()),''.join(superscript_map.keys()))

##
# @brief Connection between UI and math library
#

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

##
# @brief Function that initialize buttons
#
# By pressing on the right button,
# functions, that button represent, executes
#

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

##
# @brief Digit buttons
#
# Buttons 0-9
#

    def button_digit(self):
        button = self.sender()

        if "Error" in self.label.text():
            self.label.setText("")

        if len(self.label.text()) <= 25:
            self.label.setText(self.label.text() + button.text())
        else:
            pass

##
# @brief Decimal point button
#
# Button "."
#

    def button_decimal(self):
        if "Error" in self.label.text():
            self.label.setText("")

        if "/" in self.label.text() or "*" in self.label.text() \
                or "+" in self.label.text() \
                or "%" in self.label.text() or "^" in self.label.text() \
                or "√" in self.label.text():
            for letter in self.label.text():
                if letter == "/" or letter == "*" or letter == "+" or \
                        letter == "%" or letter == "^" or letter == "√":
                    text_after_symbol = self.label.text()[self.label.text().index(letter) + 1:]
                    if "." in text_after_symbol or len(text_after_symbol) == 0:
                        pass
                    else:
                        self.label.setText(self.label.text() + ".")
        elif "-" in self.label.text():
            self.label.setText(self.label.text() + ".")
        elif len(self.label.text()) <= 24:
            if "." in self.label.text() or len(self.label.text()) == 0:
                pass
            else:
                self.label.setText(self.label.text() + ".")
        else:
            pass

##
# @brief Operation buttons
#

    def button_activate(self):
        button = self.sender()

        if "Error" in self.label.text():
            self.label.setText("")

        if button.text() == "Sin":
            self.label.setText("Sin")
        elif button.text() == "Cos":
            self.label.setText("Cos")
        elif button.text() == "Tan":
            self.label.setText("Tan")
        elif button.text() == "x!":
            self.label.setText("!")
        elif len(self.label.text()) <= 24:

            if button.text() == "-":
                if len(self.label.text()) == 0:
                    self.label.setText(self.label.text() + "-")
                elif self.label.text().count("-") == 3:
                    pass
                elif "Sin" in self.label.text() or "Cos" in self.label.text() or "Tan" in self.label.text() or \
                        "!" in self.label.text() or "/" in self.label.text() or "*" in self.label.text() or \
                        "+" in self.label.text() or "^" in self.label.text() or \
                        "√" in self.label.text() or "%" in self.label.text():
                    for letter in self.label.text():
                        if letter == "n" or letter == "s" or letter == "+" or \
                                letter == "*" or letter == "/" or letter == "√" or \
                                letter == "!" or letter == "^" or letter == "%":
                            text_after_symbol = self.label.text()[self.label.text().index(letter) + 1:]
                            if "-" in text_after_symbol:
                                pass
                            elif len(text_after_symbol) == 0:
                                self.label.setText(self.label.text() + "-")
                elif self.label.text().count("-") == 2 and self.label.text()[-1] == "-":
                    self.label.setText(self.label.text() + "-")
                elif self.label.text().count("-") == 2 and self.label.text()[-1] != "-":
                    pass
                elif self.label.text()[0] == "-" and len(self.label.text()) > 1:
                    self.label.setText(self.label.text() + "-")
                elif len(self.label.text()) == 1 and self.label.text()[0] != "-":
                    self.label.setText(self.label.text() + "-")
                elif self.label.text().count("-") == 0:
                    self.label.setText(self.label.text() + "-")
                elif self.label.text().count("-") == 1 and self.label.text()[-1] == "-":
                    self.label.setText(self.label.text() + "-")

            elif len(self.label.text()) == 0 \
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
                elif button.text() == "ⁿ√":
                    self.label.setText(self.label.text().translate(upper_number) + "√")
                elif button.text() == "xⁿ":
                    self.label.setText(self.label.text() + "^")
        else:
            pass

##
# @brief Button that delete one symbol
#
# Erase last symbol
#

    def clear_last(self):
        if "Error" in self.label.text():
            self.label.setText("")
        else:
            new_label = self.label.text()
            self.label.setText(new_label[:-1])

##
# @brief Button that delete all symbols
#
# Erase all symbols
#

    def clear_all(self):
        self.label.setText("")

##
# @brief Equal button
#
# Button that calculate answer
#

    def equal_activate(self):

        if "+" in self.label.text():
            try:
                first_number, second_number = map(float, self.label.text().split("+"))
                answer = add(first_number, second_number)
            except ValueError:
                self.label.setText("Error: syntax")
            except Exception:
                self.label.setText("Error")
            else:
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "*" in self.label.text():
            try:
                first_number, second_number = map(float, self.label.text().split("*"))
                answer = mul(first_number, second_number)
            except ValueError:
                self.label.setText("Error: syntax")
            except Exception:
                self.label.setText("Error")
            else:
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "/" in self.label.text():
            try:
                first_number, second_number = map(float, self.label.text().split("/"))
                answer = div(first_number, second_number)
            except ZeroDivisionError:
                self.label.setText("Error: zero division")
            except ValueError:
                self.label.setText("Error: syntax")
            except Exception:
                self.label.setText("Error")
            else:
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "%" in self.label.text():
            try:
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
            except ValueError:
                self.label.setText("Error: syntax")
            except Exception:
                self.label.setText("Error")
        elif "^" in self.label.text():
            try:
                first_number, second_number = map(float, self.label.text().split("^"))
                if first_number == 0 and second_number < 0:
                    self.label.setText("Error: raise zero to negative")
                else:
                    answer = pow(first_number, second_number)
                    if int(answer) == float(answer):
                        answer = int(answer)
                    self.label.setText(str(answer))
            except ValueError:
                self.label.setText("Error: syntax")
            except Exception:
                self.label.setText("Error")
        elif "√" in self.label.text():   
            try:
                first_number, second_number = self.label.text().split("√")
                first_number = first_number.translate(normal_number)
                first_number = float(first_number)
                second_number = float(second_number) 
                if first_number < 0:
                    self.label.setText("Error: negative root")
                elif second_number == 0:
                    self.label.setText("Error: root of zero")
                else:
                    answer = root(second_number, first_number)
                    if int(answer) == float(answer):
                        answer = int(answer)
                    self.label.setText(str(answer))
            except ValueError:
                self.label.setText("Error: syntax")
            except Exception:
                self.label.setText("Error")
        elif "Sin" in self.label.text():
            try:
                number = self.label.text()[3:]
                answer = sin(float(number))
            except OverflowError:
                self.label.setText("Error: too big number")
            except ValueError:
                self.label.setText("Error")
            else:
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "Cos" in self.label.text():
            try:
                number = self.label.text()[3:]
                answer = cos(float(number))
            except OverflowError:
                self.label.setText("Error: too big number")
            except ValueError:
                self.label.setText("Error")
            else:
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "Tan" in self.label.text():
            try:
                number = self.label.text()[3:]
                answer = tan(float(number))
            except OverflowError:
                self.label.setText("Error: too big number")
            except ValueError:
                self.label.setText("Error")
            else:
                if int(answer) == float(answer):
                    answer = int(answer)
                self.label.setText(str(answer))
        elif "!" in self.label.text():
            try:
                number = float(self.label.text()[1:])
                if int(number) < 0:
                    self.label.setText("Error: must be greater then -1")
                elif int(number) != number:
                    self.label.setText("Error: value must be integer")
                else:                    
                    answer = fact(int(number))
                    self.label.setText(str(answer))
            except RecursionError:
                self.label.setText("Error: too big number")
            except Exception:
                self.label.setText("Error")
        elif "-" in self.label.text():                                  # dealing with operations with "-"
            if self.label.text().count("-") == 3:
                try:
                    empty1, first_number, empty2, second_number = map(str, self.label.text().split("-"))
                    answer = sub(float("-" + first_number), float("-" + second_number))
                except ValueError:
                    self.label.setText("Error: syntax")
                except Exception:
                    self.label.setText("Error")
                else:
                    if int(answer) == float(answer):
                        answer = int(answer)
                    self.label.setText(str(answer))
            elif self.label.text().count("-") == 2 and self.label.text()[0] != "-":
                try:
                    first_number, empty, second_number = map(str, self.label.text().split("-"))
                    answer = sub(float(first_number), float("-" + second_number))
                except ValueError:
                    self.label.setText("Error: syntax")
                except Exception:
                    self.label.setText("Error")
                else:
                    if int(answer) == float(answer):
                        answer = int(answer)
                    self.label.setText(str(answer))
            elif self.label.text().count("-") == 2 and self.label.text()[0] == "-":
                try:
                    empty, first_number, second_number = map(str, self.label.text().split("-"))
                    answer = sub(float("-" + first_number), float(second_number))
                except ValueError:
                    self.label.setText("Error: syntax")
                except Exception:
                    self.label.setText("Error")
                else:
                    if int(answer) == float(answer):
                        answer = int(answer)
                    self.label.setText(str(answer))
            elif self.label.text().count("-") == 1:
                try:
                    first_number, second_number = map(float, self.label.text().split("-"))
                    answer = sub(first_number, second_number)
                except ValueError:
                    self.label.setText("Error: syntax")
                except Exception:
                    self.label.setText("Error")
                else:
                    if int(answer) == float(answer):
                        answer = int(answer)
                    self.label.setText(str(answer))
