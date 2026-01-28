import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QColorDialog,
    QFileDialog
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My buttons to play")

        layout = QVBoxLayout()

        colorbutton = QPushButton("Clickme for colors")
        colorbutton.clicked.connect(self.choosecolor)

        filebutton = QPushButton("Clickme for files")
        filebutton.clicked.connect(self.openfilepath)

        savebutton = QPushButton("Clickme for colors")
        savebutton.clicked.connect(self.savefileas)

        layout.addWidget(colorbutton)
        layout.addWidget(filebutton)
        layout.addWidget(savebutton)
        
        self.setLayout(layout)

    def choosecolor(self):
        # Color chooser (returns QColor)
        color = QColorDialog.getColor(
            title="Select a color",
            parent=self
        )

        if color.isValid():
            # RGB and HEX equivalents
            rgb = color.getRgb()[:3]
            hex_color = color.name()
            print(f"Here is the selected color (RGB): {rgb}, HEX: {hex_color}")

    def openfilepath(self):
        # Open file dialog
        filepath, _ = QFileDialog.getOpenFileName(
            self,
            "Please open a file",
            "C:/",
            "Text file (*.txt);;Python file (*.py)"
        )

        if filepath:
            print(f"this is the path of the open file {filepath}")

    def savefileas(self):
        # Save file dialog
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            "Save the file as",
            "",
            "Text file (*.txt)"
        )

        if filepath:
            with open(filepath, "w") as file:
                file.write("You save me!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())