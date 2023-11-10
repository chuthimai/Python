import sys
from PyQt6.QtWidgets import *

class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Initialize default constructor of parent class

        self.layout = QFormLayout()

        self.input_num1 = QLineEdit()
        self.sign = QLineEdit()
        self.input_num2 = QLineEdit()
        self.button = QPushButton("Calculate")
        self.label = QLabel()

        self.layout.addRow(QLabel("Enter num 1"))
        self.layout.addRow(self.input_num1)
        self.layout.addRow(QLabel("Enter sign (+, -, *, /)"))
        self.layout.addRow(self.sign)
        self.layout.addRow(QLabel("Enter num 2"))
        self.layout.addRow(self.input_num2)
        self.layout.addRow(self.button)
        self.layout.addRow(self.label)

        self.setLayout(self.layout)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.input_num1 = self.input_num1.text()
        self.sign = self.sign.text()
        self.input_num2 = self.input_num2.text()
        res = ""
        if self.input_num1!="" and self.input_num2!="" and self.sign!="":
            if self.sign == "+":
                res = str(float(self.input_num1) + float(self.input_num2))
            if self.sign == "-":
                res = str(float(self.input_num1) - float(self.input_num2))
            if self.sign == "*":
                res = str(float(self.input_num1) * float(self.input_num2))
            if self.sign == "/":
                res = str(float(self.input_num1) / float(self.input_num2))
        if res == "":
            self.label.setText("Invalid")
        else:
            self.label.setText(res)
        # self.button.setEnabled(False)


application = QApplication(sys.argv)
window = MyMainWindow()
window.setWindowTitle("Calculator")

window.show()
application.exec()




