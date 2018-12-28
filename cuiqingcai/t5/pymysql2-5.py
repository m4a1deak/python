import pymysql

db = pymysql.connect(host='localhost',user='root',password='newpass',port=3306,db='spiders')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print('Database version:',data)

sql = 'select * from students where age>=20'

#try:
#    cursor.execute(sql)
#    print('Count:',cursor.rowcount)
#    one = cursor.fetchone()
#    print('one:',one)
#    result = cursor.fetchall()
#    print('Results:',result)
#    print('Results type',type(result))
#    for row in result:
#        print(type(row),row)
#except Exception as e:
#    print('Error')


try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except Exception as e:
    print('Error')