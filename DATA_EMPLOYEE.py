import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("DATA_EMPLOYEE.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE




conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='wholesale_management_system')
class employee(QMainWindow, form_class):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display_data)
    
    def display_data(self):
        name = self.lineEdit.text()
        e_id = self.lineEdit_2.text()
        j_d = self.lineEdit_3.text()
        c_n = self.lineEdit_4.text()
        sal= self.lineEdit_5.text()
        cursor = conn.cursor()
        query= ("INSERT INTO employee  VALUES ('%s','%s','%s',%s,%s)" %( int(e_id),name,j_d,int(c_n),int(sal)))
        cursor.execute(query)
        conn.commit()
        


        
        


  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = employee()
    dv.show()
    app.exec_()

