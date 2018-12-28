from urllib import request,parse
#import urllib.request
#import urllib.parse
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

url = 'http://172.16.0.189:8080/SrmWeb/userLogin/loginCheck.do'
headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host':'172.16.0.189:8080'
}
dict={
    'userName':'zhouya2',
    'password':'12345678'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))