import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.db

collection = db.students

student = {
    'id': 20170101,
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student1 = {
    'biaoti': '荣耀MagicBook 14英寸轻薄窄边框笔记本电脑（intel八代酷睿i7-8550U 8G 256G MX150 2G独显）冰河银【12月超值秒杀抢购】微边框护眼全高清IPS屏，满血版MX150独显，薄至15.8mm，数量有限，先到先得更多产品详情猛戳》》》',
    'jiage': '￥5699.00',
    'guanzhu': '二手有售7.8万+条评价',
    'dianpu': '荣耀京东自营旗舰店',
    'ziying': '自营'
}
print(type(student1))
result = collection.insert(student1)
print(result)
