import json

str = '''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(type(data),data)
print(data[0]['name'])
print(data[1].get('name'))
print(data[1].get('age',13))


with open('data.json','r') as file:
    str = file.read()
    data = json.loads(str)
    print(type(data),data)



data = str =[{
    "name":"王伟",
    "gender":"男",
    "birthday":"1992-10-18"
}]
with open('data.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))
