import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("DISPLAY.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

#ser = serial.Serial('com3',9600)



class ddisplay(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.customer)
        self.pushButton_6.clicked.connect(self.product_detail)
        self.pushButton_2.clicked.connect(self.employee)
        
    def customer(self):#create process that will display all telementry data
        Popen([executable, 'DISPLAY_CUSTOMER.py'], creationflags=CREATE_NEW_CONSOLE)
    def product_detail(self):
        Popen([executable, 'DISPLAY_PRODUCT_DETAIL.py'], creationflags=CREATE_NEW_CONSOLE) 
    def employee(self):
        Popen([executable, 'DISPLAY_EMPLOYEE.py'], creationflags=CREATE_NEW_CONSOLE) 

  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = ddisplay()
    dv.show()
    app.exec_()

