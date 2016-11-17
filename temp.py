import datetime
import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='deveshbajaj')
cursor = conn.cursor()



tab='employee'
pro='fname'
new='shivam'
old='kamal'

#query= ("UPDATE %s  SET   %s='%s'   WHERE   %s= '%s'")%(tab,pro,new,pro,old)
#ELETE FROM tutorials_tbl WHERE tutorial_id=3;
#query= ("DELETE FROM %s WHERE %s='%s'") %(tab,pro,new)
#x=int(2003)
#query = ("SELECT %S FROM product WHERE product_id = '%s'"%x)
query= ("SELECT %s  from  %s")%(pro,tab)
cursor.execute(query)

 
#cursor.execute(query)
c=[]
for x in cursor:
    data=[str(i) for i in x]
    #print(data[0])
    c.append(data[0])
print(c)
conn.commit()



cursor.close()
conn.close()
