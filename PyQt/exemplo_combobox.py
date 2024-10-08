import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, 
                             QPushButton, QLineEdit, QMainWindow, QComboBox
                            )

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        combo = QComboBox(self)
        combo.addItem("Apple")
        combo.addItem("Pear")
        combo.addItem("Lemon")

        combo.move(50, 50)

        self.qlabel = QLabel(self)
        self.qlabel.move(50, 16)

        combo.activated[str].connect(self.onChanged)

        self.setGeometry(50, 50, 320, 200)
        self.setWindowTitle("QComboBox Example")
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
