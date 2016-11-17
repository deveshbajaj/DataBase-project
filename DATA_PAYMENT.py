import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("DATA_PAYMENT.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE




conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='wholesale_management_system')
class payment(QMainWindow, form_class):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.display_data)
    
    def display_data(self):
        p_id = self.lineEdit.text()
        c_id = self.lineEdit_2.text()
        amo= self.lineEdit_3.text()
        x= self.lineEdit_4.text()
        
        cursor = conn.cursor()
        query= ("INSERT INTO payment  VALUES (%s,%s,%s,'%s')" %( int(c_id),int(p_id),int(amo),x))
        cursor.execute(query)
        conn.commit()
        


        
        


  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = payment()
    dv.show()
    app.exec_()

