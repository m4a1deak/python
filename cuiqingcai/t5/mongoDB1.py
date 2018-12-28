import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)

db = client.test

collection = db.students

student = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2 = {
    'id':'20170102',
    'name':'AA',
    'age':20,
    'gender':'male'
}
student3 = {
    'id':'20170103',
    'name':'VV',
    'age':20,
    'gender':'male'
}
student4 = {
    'id':'20170104',
    'name':'BB',
    'age':20,
    'gender':'male'
}
#result = collection.insert_one(student)
result = collection.insert_many([student,student2,student3,student4])
print(result)
#print(result.inserted_id)
print(result.inserted_ids)