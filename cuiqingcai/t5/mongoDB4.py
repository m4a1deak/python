import pymongo

clinet = pymongo.MongoClient(host='localhost',port=27017)
db = clinet.test
collection = db.students

result = collection.delete_one({'name':'VV'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age':{'$lt':25}})
print(result.deleted_count)