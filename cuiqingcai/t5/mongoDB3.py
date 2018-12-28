import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collention = db.students
condition = {'name':'AA'}
student = collention.find_one(condition)
print(student)
result = collention.update(condition,student)
print(result)


#client = pymongo.MongoClient(host='localhost',port=27017)
#db = client.test
#collention = db.students
#
#result = collention.find_one({'name':'Jordan'})
#print(type(result))
#print(result)
#student['age']= 25
#result = collention.update(condition,student)


