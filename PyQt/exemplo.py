import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World")
    textLabel.move(10, 10)

    button1 = QPushButton(widget)
    button1.setText("Button 1")
    button1.move(120, 64)
    button1.clicked.connect(button1_clicked)

    button2 = QPushButton(widget)
    button2.setText("Button 2")
    button2.move(120, 96)
    button2.clicked.connect(button2_clicked)

    button3 = QPushButton(widget)
    button3.setText("Show dialog!")
    button3.move(120, 128)
    button3.clicked.connect(showDialog)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())

def button1_clicked():
    print("Button 1 clicked")

def button2_clicked():
    print("Button 2 clicked")

def showDialog():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Message box pop up window")
    msgBox.setWindowTitle("QMessageBox Example")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('Ok clicked')
    else:
        print('Cancel clicked')

def msgButtonClick(i):
    print("Button clicked is:", i.text())

if __name__ == '__main__':
    window()