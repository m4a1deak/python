from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '183.131.154.143:10072'
# proxy = 'username:password@183.131.154.143:10072'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opner = build_opener(proxy_handler)
try:
    response = opner.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
