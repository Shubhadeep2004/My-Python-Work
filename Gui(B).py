import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                            QRadioButton,QButtonGroup)

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700,250,500,500)
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("UPI",self)
        self.radio3=QRadioButton("Mastercard",self)
        self.radio4=QRadioButton("Gift Card",self)
        self.radio5=QRadioButton("In-Store",self)
        self.radio6=QRadioButton("Online",self)

        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio3.setGeometry(0,150,300,50)
        self.radio3.setGeometry(0,200,300,50)
        self.radio3.setGeometry(0,250,300,50)

        self.setStyleSheet("QRadioButton{"
                           "font-size :30px;"
                            "font-family : Arial;"
                            "padding :  10px;"
                           "}")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group1.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        self.button_group2.addButton(self.radio6)

        self.radio1.toggle.connect(self.radio_button_changed)
        self.radio2.toggle.connect(self.radio_button_changed)
        self.radio3.toggle.connect(self.radio_button_changed)
        self.radio4.toggle.connect(self.radio_button_changed)
        self.radio5.toggle.connect(self.radio_button_changed)
        self.radio6.toggle.connect(self.radio_button_changed)
        

    def radio_button_changed(self):
        radio_button =self.sender()
        if radio_button.isChecked():
            print(f"{radio_button} is selected")

def main():
    app=QApplication([])
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main() 