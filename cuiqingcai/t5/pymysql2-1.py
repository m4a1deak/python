import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost',user='root',password='newpass',port=3306,db='spiders')
cursor = db.cursor()
sql = "insert into students(id,name,age) values(%s,%s,%s)"
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()