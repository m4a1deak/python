import requests
import re

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore",headers=headers)
# pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>",re.S)
# titles = re.findall(pattern,r.text)
# print(titles)



# rr = requests.get("https://github.com/favicon.ico")
# print(rr.text)
# print(rr.content)
# with open('favicon.ico','wb') as f:
#     f.write(rr.content)


headers = {
     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
 }
r = requests.get("https://www.zhihu.com/explore",headers=headers)
#print(r.text)


r = requests.get("https://www.jianshu.com/")
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)
exit() if not r.status_code == requests.codes.forbidden else print("Request Successfully")