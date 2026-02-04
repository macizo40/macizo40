# we will start to use the graphics with tkinter
# (now converted to PySide6 / Qt)

# as first you need to import the widgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt
import sys


# the initial is to create a root object
app = QApplication(sys.argv)
root = QMainWindow()

# we can start cutomizing the title of the window
root.setWindowTitle("GYM-RAT")

# also we can add an icon
root.setWindowIcon(QIcon("practice/files/image-cup.gif"))

# using this code we can set an specific size and let the user re size it or not.
# (fixed size = not resizable)
root.setFixedSize(300, 300)


# the term frame is where we will stablish the content so then we will use the next

# calling the frame object
frame = QFrame()  # you need to pass as argument in which root this frame will exist, w and h too
frame.setFixedSize(600, 600)

# frame.pack(side="top",anchor="center")  # after that you need to pack the frame in the root, we set the side
# Qt uses layouts instead of pack
layout = QVBoxLayout()
layout.addWidget(frame)

container = QFrame()
container.setLayout(layout)
root.setCentralWidget(container)

# we will use more the config property to give color, border and more
frame.setCursor(QCursor(Qt.PointingHandCursor))  # pirate cursor doesn't exist in Qt

# bg is the background
# bd is the border size
# relief is the shape of the border
frame.setStyleSheet("""
    background-color: lightblue;
    border: 20px solid gray;
""")
frame.setFrameShape(QFrame.Box)     # similar to relief
frame.setFrameShadow(QFrame.Sunken) # this is the shape of the border


# but you can also set the same properties of the frame to the root as is

root.setCursor(QCursor(Qt.ArrowCursor))

root.setStyleSheet("""
    background-color: blue;
    border: 20px solid gray;
""")

# ridge style approximation
root.setContentsMargins(10, 10, 10, 10)


# then we need to initialize the windows, this is like the start
root.show()
sys.exit(app.exec())
