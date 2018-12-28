from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=0)
redis.set('name','Bob')
redis.set('age','14')
print(redis.get('name'))
print(redis.get('age'))

print(redis.exists('name'))
print(redis.type('name'))
print(redis.delete('age'))
