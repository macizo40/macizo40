#now lets test another GUI package that is common in the market, this will be pyside6, you can see differences in the way to call objects

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


# slot / callback
def clickme():
    print("You click me")
    app.exit()


# Qt apps need an application object
app = QApplication(sys.argv)


# main window
root = QWidget()
root.setWindowTitle("This is my title")


# button
button = QPushButton("Click me")
button.clicked.connect(clickme)


# layout (Qt always uses layouts instead of pack/grid/place)
layout = QVBoxLayout()
layout.addWidget(button)
root.setLayout(layout)


# show window and start event loop
root.show()
app.exec()