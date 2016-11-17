import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("DATA_CUSTMER.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE




conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='wholesale_management_system')
class employee(QMainWindow, form_class):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display_data)
        self.pushButton_2.clicked.connect(self.bill)
    def display_data(self):
        name = self.lineEdit.text()
        c_id = self.lineEdit_2.text()
        city = self.lineEdit_3.text()
        pin= self.lineEdit_4.text()
        mail= self.lineEdit_5.text()
        c_no= self.lineEdit_6.text()
        steet= self.lineEdit_7.text()

        cursor = conn.cursor()
        query_1= ("INSERT INTO customer  VALUES ('%s','%s','%s',%s)" %( int(c_id),name,mail,int(c_no)))
        query_2= ("INSERT INTO customer_adress  VALUES ('%s','%s','%s',%s)" %( int(c_id),steet,city,int(pin)))
        cursor.execute(query_1)
        cursor.execute(query_2)
        conn.commit()
    def bill(self):
        Popen([executable, 'DATA_PAYMENT.py'], creationflags=CREATE_NEW_CONSOLE) 

        


        
        


  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = employee()
    dv.show()
    app.exec_()

