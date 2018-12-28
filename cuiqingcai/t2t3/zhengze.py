import re

content = "Hello 123 4567 World_This is a Regex Demo"
print(len(content))
result = re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}",content)
print(result)
print(result.group())
print(result.span())
print('*'*50)

content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^Hello\s(\d+)\sWorld",content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
print('*'*50)

content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^Hello.*Demo$",content)
print(result)
print(result.group())
print(result.span())
print('*'*50)


content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^He.*(\d+).*Demo$",content)
print(result)
print(result.group())
print(result.group(1))
print('*'*50)


content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^He.*?(\d+).*Demo$",content)
print(result)
print(result.group())
print(result.group(1))
print('*'*50)

content = "http://weibo.com/comment/kEraCN"
result1 = re.match("http.*?comment/(.*?)",content)
result2 = re.match("http.*?comment/(.*)",content)
print('result1',result1.group(1))
print('result2',result2.group(1))
print('*'*50)

content = '''Hello 1234567 World_This
is a Regex Demo
'''
print(content)
result = re.match("^He.*?(\d+).*?Demo$",content,re.S)
print(result.group(1))
print('*'*50)

content = '（百度）www.baidu.com'
#result = re.match('\(百度\)www\.baidu\.com',content)
result = re.match('\（百度\）www\.baidu\.com',content)
print(result)
print('*'*50)

content = 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
print('*'*50)

html = '''
<div id="songs-list"> 
<h2 class＝"title">经典老歌</h2>
<p class="introduction">经典老歌列表</p> 
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7"><a href ＝”/2.mp3" singer="任贤齐">沧海一卢笑</a></li> 
<li data-view="4" class="active"><a href="/3.mp3" singer="齐泰">往事随风</a></li> 
<li data-view="5"><a href="/5.mp3" singer="除也琳">记事本</a></li>
<li data-view＝"6"><a href="/4.mp3" singer="beyond">尤辉岁月</a></li>
<li data-view="5"><a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li> 
</ul> 
</div>'''
print(html)
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
if result:
    print(result.group(1),result.group(2))
print('*'*50)


result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(type(result))
for res in result:
    print(res)
    print(res[0],res[1],res[2])


print('*'*50)

content = '54aKS4yrsoiRS4ixSL2g'
content = re.sub('\d+','',content)
print(content)
print('*'*50)

#resultt = re.findall('<li.*?\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
#print(type(resultt),resultt)
#for resultttttt in resultt:
#    print(resultttttt[1])
html1 = re.sub('<a.*?>|</a>','',html)
print(html1)
results = re.findall('<li.*?>(.*?)</li>',html1,re.S)
print(results)
for result in results:
    print(result.strip())
print('*'*50)

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-19 17:23'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1,result2,result3)
print('*'*50)