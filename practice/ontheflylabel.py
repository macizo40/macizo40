# this practice is almost the same of the previous buttons.py but now lets put the out put in the window
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# we do use the same methods to insert and run the objects 
app = QApplication(sys.argv)
root = QWidget()
root.setWindowTitle("On the fly example")

# we will use now a button that is clickable, with an action

# first lets define a quick method or function, which will be excuted when you click the button
def clickme():
    print("You click me")

# to do something in the window, lets first define a method example create a label
def create_label():
    # this need to follow the same process as any other graphic object
    label = QLabel("Dynamic label creation")
    layout.addWidget(label)

# layout is required in PySide6 to organize widgets
layout = QVBoxLayout()
root.setLayout(layout)

# as you can see the parameter command will call the method
# in PySide6 we use signals (clicked.connect)
button = QPushButton("Click me")
button.clicked.connect(create_label)
layout.addWidget(button)

root.show()
sys.exit(app.exec())
