#python program to update mysql table in databases
import mysql.connector as mysql
con=mysql.connect(host='localhost',user='root',password='',database='admission')
cur=con.cursor()
regno=input('enter the regno')
name=input('enter the name')
cur.execute('select * from student where regno=%s',(regno,))
result=cur.fetchall()
print(result)
if(len(result)==0):
    print('student not found')
else:
    cur.execute('update student set regno=%s, name=%s where regno=%s',(regno,name,regno))
    print(str(cur.rowcount)+' row updated')
    con.commit()
con.close()