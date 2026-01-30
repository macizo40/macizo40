from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PySide6.QtCore import Qt
import sys

# lets start doing some actions like what is we have a simple calculation in the buttons

def sum():
    # this operation will be kind different due is managing in the GUI
    result.setText(str(float(number1.text()) + float(number2.text())))
    clean_values()  # calling clean to set text values to nothing

def reduction():
    # this operation will be kind different due is managing in the GUI
    result.setText(str(float(number1.text()) - float(number2.text())))
    clean_values()  # calling clean to set text values to nothing

def multiply():
    # this operation will be kind different due is managing in the GUI
    result.setText(str(float(number1.text()) * float(number2.text())))
    clean_values()  # calling clean to set text values to nothing

# lets define a method that cleand the text values after the button is clicked

def clean_values():
    # we will net just to set the values to nothing
    number1.setText("")
    number2.setText("")
    # now this need to be called in the operation method


app = QApplication(sys.argv)

root = QWidget()
root.setWindowTitle("Simple Calculator")
# lets use borders to give more presentation to this code
root.setStyleSheet("padding: 15px;")  # this are the spaces that we will set to the elements.

layout = QVBoxLayout(root)

# create the calculations variables, since they need to exist to be used in the calculations.
number1 = QLineEdit()
number2 = QLineEdit()
result = QLineEdit()

# now lets create the entry fields in the GUI
# we can set labels to identify the values that we will input
layout.addWidget(QLabel("First value"))
number1.setAlignment(Qt.AlignCenter)
layout.addWidget(number1)

layout.addWidget(QLabel("Second value"))
number2.setAlignment(Qt.AlignCenter)
layout.addWidget(number2)

layout.addWidget(QLabel("Result"))
result.setDisabled(True)
result.setAlignment(Qt.AlignCenter)
layout.addWidget(result)

# we do define the button and the method that will do the actions, the method need to exist before this
btn_operation = QPushButton("Sum")
btn_operation.clicked.connect(sum)
layout.addWidget(btn_operation)

btn_reduction = QPushButton("Reduction")
btn_reduction.clicked.connect(reduction)
layout.addWidget(btn_reduction)

btn_multiply = QPushButton("Multiply")
btn_multiply.clicked.connect(multiply)
layout.addWidget(btn_multiply)

root.show()
sys.exit(app.exec())
