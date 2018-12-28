import urllib.request
import urllib.parse
response = urllib.request.urlopen("http://172.16.0.189:8080/SrmWeb/page/login.jsp",timeout=1)
#data = bytes(urllib.parse.urlencode({'userName':'zhouya2','password':'12345678'}),encoding='utf8')
#response = urllib.request.urlopen('http://172.16.0.189:8080/SrmWeb/page/login.jsp',data=data)
#response = urllib.request.urlopen('http://172.16.0.189:8080/SrmWeb/userLogin/loginCheck.do',data=data)

print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
