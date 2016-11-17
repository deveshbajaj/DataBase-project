import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("DELETE.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE




conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='wholesale_management_system')
class PRODUCT(QMainWindow, form_class):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display_data)
        self.pushButton_2.clicked.connect(self.dele)
        self.pushButton_3.clicked.connect(self.name)
    def name(self):
        tab = str(self.comboBox.currentText())
        pro= str(self.comboBox_2.currentText())
        cursor = conn.cursor()
        
        query= ("SELECT %s  from  %s")%(pro,tab)
        cursor.execute(query)
        c=[]
        for x in cursor:
            data=[str(i) for i in x]
            #print(data[0])
            c.append(data[0])
            
        self.comboBox_3.addItems(c)
        
        conn.commit()
        self.comboBox_3.clear()
        self.comboBox_3.addItems(c)
        
    
    def display_data(self): 
        customer=["custmer_id ","mobile_no "]
        customer_adress=["custmer_id "]
        payment=["custmeer_id ","payment_id "]
        employee=["employee_id ","mobile_no ","salary"]
        product=["product_id ","store_loc  "]
        stock=["product_id ","model_no "]
        wholesaler=["wholesaler_id ","product_id "]
        self.comboBox_2.clear()
        text = str(self.comboBox.currentText())
        if text == "customer":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(customer)
        elif text == "customer_adress":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(customer_adress)
        elif text == "payment":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(payment)
        elif text == "employee":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(employee)
        elif text == "product":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(product)
        elif text == "stock":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(stock)
        elif text == "wholesaler":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(wholesaler)
        
        
    def dele(self):
        
        tab = str(self.comboBox.currentText())
        pro= str(self.comboBox_2.currentText())
        new = str(self.comboBox_3.currentText())
        
        cursor = conn.cursor()
      
        query_1= ("DELETE FROM %s WHERE %s='%s'") %(tab,pro,int(new))
        #query_1= 'UPDATE %s  SET   %s="%s"   WHERE   %s="%s" '%(tab,pro,new,pro,old)
        print(query_1)
        cursor.execute(query_1)
        conn.commit()
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = PRODUCT()
    dv.show()
    app.exec_()

