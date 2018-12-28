import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collention = db.students

result = collention.find_one({'name':'Jordan'})
print(type(result))
print(result)

result = collention.find_one({'_id':ObjectId('5bef6e699dc6d613745c9d48')})
print(type(result))
print(result)

results = collention.find({'age':20})
print(results)
for result in results:
    print(result)



print(collention.find({'age':20}).count())


results = collention.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])


results = collention.find().sort('name',pymongo.ASCENDING).skip(2).limit(3)
print([result['name'] for result in results])