import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QPushButton)



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(500,250,500,500)
        self.button=QPushButton("Click!",self)
        self.label=QLabel("Welcome",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(100,150,100,100)
        self.button.setStyleSheet("font-size:20px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,200,200,200)
        self.label.setStyleSheet("font-size : 50px;")

    def on_click(self):
        print("button clicked!")
        self.button.setText("Clicked")
        self.button.setDisabled(True)


def main():
    app=QApplication([])
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()        
        