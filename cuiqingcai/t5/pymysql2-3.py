import pymysql

db = pymysql.connect(host='localhost',user='root',password='newpass',port=3306,db='spiders')
cursor = db.cursor()

data = {
    'id':'20110001',
    'name':'Bob',
    'age':21
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
#print(values)
sql = 'insert into {table} ({keys}) values({values}) on duplicate key update '.format(table=table,keys=keys,values=values)
#print(sql)
update = ','.join(["{key}=%s".format(key=key) for key in data])
#print(update)
sql += update
#print(sql)
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Successful')
        db.commit()
except Exception as e:
    print(str(e))
    db.rollback()
db.close()