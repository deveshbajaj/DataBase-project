import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("CRONTROL.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

#ser = serial.Serial('com3',9600)



class ddisplay(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.entry)
        self.pushButton_5.clicked.connect(self.display_yo)
        self.pushButton_7.clicked.connect(self.modify)
        self.pushButton_3.clicked.connect(self.delete)
        
        
    def entry(self):#create process that will display all telementry data
        Popen([executable, 'DATA.py'], creationflags=CREATE_NEW_CONSOLE)
    def display_yo(self):
        Popen([executable, 'DISPLAY.py'], creationflags=CREATE_NEW_CONSOLE)
    def modify(self):
        Popen([executable, 'MODIFY.py'], creationflags=CREATE_NEW_CONSOLE)
    def delete(self):
        Popen([executable, 'DELETE.py'], creationflags=CREATE_NEW_CONSOLE)
    
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = ddisplay()
    dv.show()
    app.exec_()

