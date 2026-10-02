#Create a gui 
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(500,250,500,500)
        self.setWindowIcon(QIcon("first.png"))

        #label=QLabel("Welcome",self)
       # label.setFont(QFont("Arial",30))
        #label.setGeometry(0,0,700,200)
        #label.setStyleSheet("color : #5b5b61;"
        #                    "background-color : #60b0bd;"
       #                     "font-wieght : bold;"
        #                    "font-Style : Italic ")
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignCenter)
        label=QLabel(self)
        label.setGeometry(0,0,200,200)

        pixmap = QPixmap("first.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        label.setGeometry((self.width()-label.width())//2,
                          (self.height()-label.height())//2,#this division is done to maintain the label in the center of the gui
                          label.width(),
                          label.height())

def main():
    app=QApplication([])
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()