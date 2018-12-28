import urllib.request
import urllib.parse
import  socket
import urllib.error
#response = urllib.request.urlopen("http://172.16.0.189:8080/SrmWeb/page/login.jsp",timeout=0.1)
#data = bytes(urllib.parse.urlencode({'userName':'zhouya2','password':'12345678'}),encoding='utf8')
#response = urllib.request.urlopen('http://172.16.0.189:8080/SrmWeb/page/login.jsp',data=data)
#response = urllib.request.urlopen('http://172.16.0.189:8080/SrmWeb/userLogin/loginCheck.do',data=data)
try:
    response = urllib.request.urlopen("https://www.zhihu.com",timeout=0.1)
except urllib.error.URLError as e:
    print(e)
    print(e.reason)
    print(socket.timeout)
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT")
#print(response.read().decode('utf-8'))
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))
