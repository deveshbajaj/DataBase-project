import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("MODIFY.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE




conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='wholesale_management_system')
class PRODUCT(QMainWindow, form_class):
    
    

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display_data)
        self.pushButton_3.clicked.connect(self.up_date)
        self.pushButton_2.clicked.connect(self.exe)
    
    def display_data(self): 
        

        customer=["custmer_id ","Name","email ","mobile_no "]
        customer_adress=["custmer_id ","street ","city  ","pincode "]
        payment=["custmeer_id ","payment_id ","amount ","method "]
        employee=["employee_id ","name ","join_date  ","mobile_no ","salary"]
        product=["product_id ","Name ","store_loc  ","avl_quantity  "]
        stock=[" avl_quantity_godown  "," quantity_to_order ","product_id ","model_no "]
        wholesaler=["wholesaler_id ","Name ","product_id ","netprice"," profit"]
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
        
        
    def up_date(self):
        
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
        
    def exe(self):
        tab = str(self.comboBox.currentText())
        pro= str(self.comboBox_2.currentText())
        old = str(self.comboBox_3.currentText())
        new = self.lineEdit_3.text()
        
        cursor = conn.cursor()
        
        
        #UPDATE employee  SET   name=" naruto "   WHERE    employee_id= 20001
        query_1= 'UPDATE %s  SET   %s="%s"   WHERE   %s="%s" '%(tab,pro,new,pro,old)
        print(query_1)
        cursor.execute(query_1)
        conn.commit()
        self.lineEdit_3.setText(" ")
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = PRODUCT()
    dv.show()
    app.exec_()

