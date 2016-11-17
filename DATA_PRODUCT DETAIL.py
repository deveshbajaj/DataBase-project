import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication
import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()




form_class, QMainWindow = uic.loadUiType("DATA_PRODUCT DETAIL.ui")

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
        p_id = self.lineEdit_2.text()
        amount= self.lineEdit_3.text()
        m_no= self.lineEdit_4.text()
        w_id= self.lineEdit_5.text()
        s_loc= self.lineEdit_6.text()
        q_or= self.lineEdit_7.text()
        avl= self.lineEdit_8.text()
        w_name= self.lineEdit_10.text()
        profit= self.lineEdit_9.text()
        
        cursor = conn.cursor()
        
        query_1= ("INSERT INTO product  VALUES (%s,'%s',%s,%s)" %( int(p_id),name,int(s_loc),int(avl)))
        query_2= ("INSERT INTO stock  VALUES (%s,%s,%s,%s)" %( int(avl),int(q_or),int(m_no),int(p_id)))
        query_3= ("INSERT INTO wholesaler  VALUES (%s,'%s',%s,%s,%s)" %( int(w_id),w_name,int(p_id),int(amount),int(profit)))
        cursor.execute(query_1)
        cursor.execute(query_2)
        cursor.execute(query_3)
        conn.commit()
    
        


        
        


  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = employee()
    dv.show()
    app.exec_()

