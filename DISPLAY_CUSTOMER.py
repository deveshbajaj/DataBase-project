import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("DISPLAY_CUSTOMER.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE




conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='wholesale_management_system')
class CUSTOMER(QMainWindow, form_class):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.puut()
        self.pushButton.clicked.connect(self.display_data)
    def puut(self):
        cursor = conn.cursor()
        query_1 = ("select custmer_id from customer")
        cursor.execute(query_1)
        c=[]
        for x in cursor:
            data=[str(i) for i in x]
            #print(data[0])
            c.append(data[0])
            
        self.comboBox_2.addItems(c)
        
        



        
    def display_data(self):
        
        cursor = conn.cursor()
        #x = self.lineEdit.text()
        x=str(self.comboBox_2.currentText())
        x=int(x)
        query_1 = ("SELECT * FROM customer WHERE custmer_id = '%s'"%x)
        query_2 = ("SELECT * FROM customer_adress WHERE custmer_id = '%s'"%x)
        query_3 = ("SELECT * FROM payment WHERE custmeer_id = '%s'"%x)
        cursor.execute(query_1)
        for x in cursor:
            data=[str(i) for i in x]
        #print(data)
        self.label_15.setText(data[1])

        self.label_16.setText(data[0])
            
        self.label_14.setText(data[2])
            
        self.label_19.setText(data[3])
        cursor.execute(query_2)
        for x in cursor:
            data=[str(i) for i in x]
        #print(data)
        self.label_17.setText(data[2])

        self.label_21.setText(data[3])
        
        cursor.execute(query_3)
        for x in cursor:
            data=[str(i) for i in x]
        #print(data)
        self.label_22.setText(data[1])

        self.label_18.setText(data[2])
            
        

        
        


  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = CUSTOMER()
    dv.show()
    app.exec_()

