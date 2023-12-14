import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from calculator import Ui_Form
import math
import re

class Simple_Calculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btn_1.clicked.connect(lambda: self.add_text("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_text("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_text("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_text("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_text("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_text("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_text("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_text("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_text("9"))
        self.ui.btn_0.clicked.connect(lambda: self.add_text("0"))
        self.ui.btn_add.clicked.connect(lambda: self.add_text("+"))
        self.ui.btn_minus.clicked.connect(lambda: self.add_text("-"))
        self.ui.btn_multiply.clicked.connect(lambda: self.add_text("*"))
        self.ui.btn_divide.clicked.connect(lambda: self.add_text("/"))
        self.ui.btn_mod.clicked.connect(lambda: self.add_text("%"))
        self.ui.btn_dot.clicked.connect(lambda: self.add_text("."))
        self.ui.btn_curly_open.clicked.connect(lambda: self.add_text("("))
        self.ui.btn_curly_close.clicked.connect(lambda: self.add_text(")"))
        self.ui.btn_sin.clicked.connect(lambda: self.add_text("sin"))
        self.ui.btn_cos.clicked.connect(lambda: self.add_text("cos"))
        self.ui.btn_tan.clicked.connect(lambda: self.add_text("tan"))
        self.ui.btn_sqrt.clicked.connect(lambda: self.add_text("sqrt"))
        self.ui.btn_pi.clicked.connect(lambda: self.add_text("𝝅"))
        self.ui.btn_pow.clicked.connect(lambda: self.add_text("^"))
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_equal.clicked.connect(self.calculate)

    def add_text(self, text):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + text)

    def delete(self):
        self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1])
        
    def reset(self):
        self.ui.lineEdit.setText('')
        
    def calculate(self):
        expression = self.ui.lineEdit.text()
        try:
            expression = expression.replace("^","**")
            result = eval(expression)
            self.ui.lineEdit.setText(str(result))
        except Exception as e:
            result = self.evaluate_expression(expression)
            self.ui.lineEdit.setText(str(result))
            
    def evaluate_expression(self, expression):
        # Custom function to evaluate sin, cos, tan, sqrt, and pi
        print(expression)
        expression = expression.replace("sin","math.sin")
        expression = expression.replace("cos","math.cos")
        expression = expression.replace("tan","math.tan")
        expression = expression.replace("𝝅","math.pi")
        expression = expression.replace("sqrt","math.sqrt")
        
        print(expression)
        print("4^2 ",4**2)
        
        return eval(expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Simple_Calculator()
    window.show()
    sys.exit(app.exec())
