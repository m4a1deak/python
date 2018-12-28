import requests

url = 'http://httpbin.org/get'

# 代理服务器

proxy_host = 'http-pro.abuyun.com'
proxy_pory = '9010'
proxy_user = 'HC4757608382TI4P'
proxy_pass = '5549FB0162750154'
proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'pass': proxy_pass,
    'user': proxy_user,
    'port': proxy_pory
}
proxies = {
    'http': proxy_meta,
    'https': proxy_meta
}
response = requests.get(url, proxies=proxies)
print(response.status_code)
print(response.text)
