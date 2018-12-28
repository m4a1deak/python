from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=0)
redis.set('name','Bob')
redis.set('name1','Bob1')
redis.set('name2','Bob2')
redis.set('name3','Bob3')
redis.set('name4','Bob4')
redis.set('name5','Bob5')
redis.set('name6','Bob6')
redis.set('name7','Bob7')
print(redis.get('name7'))