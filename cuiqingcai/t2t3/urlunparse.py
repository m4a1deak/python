from urllib.parse import urlunparse,urlsplit,urlunsplit,urlencode,parse_qs,parse_qsl,quote,unquote

data = ['https','www,baidu.com','index.html','user','a=6','comment']
print(urlunparse(data)) # length==6

result = urlsplit('https://www,baidu.com/index.html;user?a=6#comment')
print(type(result),result)

data = ['https','www,baidu.com','index.html','a=6','comment']
print(urlunsplit(data))  #length ==5

params = {
    'name':'xiaoming',
    'age':22
}
base_url = 'https://www.baidu.com?'
url = base_url+urlencode(params)
print(url)

query = 'name=xiaoming&age=22'
print(type(parse_qs(query)),parse_qs(query))

query = 'name=xiaoming&age=23'
print(type(parse_qsl(query)),parse_qsl(query))


keyword ='安装'
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)

url= 'https://www.baidu.com/s?wd=%E5%AE%89%E8%A3%85'
print(unquote(url))