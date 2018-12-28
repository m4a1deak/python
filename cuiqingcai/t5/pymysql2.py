import pymysql

db = pymysql.connect(host='localhost',user='root',password='12345678',port=3306,db='py')
cursor = db.cursor()
sql = " create table if not exists students (id varchar(255) not null,name varchar(255) not null,age int not null ,primary key (id))"
cursor.execute(sql)
db.close()