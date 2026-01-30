from PySide6.QtWidgets import QApplication, QMainWindow
import sys

# we are now will be working with Menus this are the regular ones in any application
app = QApplication(sys.argv)
root = QMainWindow()
root.setWindowTitle("Menus example")

# there are some some non stablished rules but the common programming practices does suggest follow this

# we need to set a master menu, this is usually called
menubar = root.menuBar()

# now it is time to create the menus inside menus and we create a tree of menus

filemenu = menubar.addMenu("File")  # as you can see we add it as child of menubar which is the principal
# now it is time to add the options that each menu will have and they will be actions that will start a command
filemenu.addAction("Open")  # this case add command is different from cascade since we want an action
filemenu.addAction("Save")
filemenu.addAction("Close")
filemenu.addSeparator()  # this creates a line to separete a different section
filemenu.addAction("Exit", root.close)  # this will be always the exit command

# now lets do the same as before for the next edit menu
editmenu = menubar.addMenu("Edit")
editmenu.addAction("Copy")
editmenu.addAction("Cut")
editmenu.addAction("Paste")
editmenu.addSeparator()
editmenu.addAction("Select all")

# now lets give somce format to the help menu
helpmenu = menubar.addMenu("Help")
helpmenu.addAction("Help")
helpmenu.addSeparator()
helpmenu.addAction("About...")

root.show()
sys.exit(app.exec())
