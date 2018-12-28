import pymysql

db = pymysql.connect(host='localhost',user='root',password='newpass',port=3306,db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age>20'
sql = 'delete from {table} where {condition} '.format(table=table,condition=condition)

try:
    cursor.execute(sql)
    db.commit()
except Exception as a:
    print(str(a))
    db.commit()
db.close()