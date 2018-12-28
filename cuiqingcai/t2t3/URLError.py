from urllib import request,error
try:
    response = request.urlopen("http://www.baidu.com/1asdasd.html")
except error.URLError as e:
    print(e)