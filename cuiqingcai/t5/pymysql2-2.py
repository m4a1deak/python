import pymysql

db = pymysql.connect(host='localhost',user='root',password='newpass',port=3306,db='spiders')
cursor = db.cursor()

data = {
    'id':'20110004',
    'name':'Bob',
    'age':31
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'insert into {table} ({keys}) values({values}) '.format(table=table,keys=keys,values=values)
print(sql)
print(tuple(data.values()))
try:
   if cursor.execute(sql,tuple(data.values())):
       print('Successful')
       db.commit()
except Exception as e:
   print(str(e))
   print('Failed')
   db.rollback()
db.close()
