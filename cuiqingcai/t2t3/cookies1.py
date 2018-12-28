import  requests

# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+"="+value)

cookies = 'tgw_l7_route=5bcc9ffea0388b69e77c21c0b42555fe; _zap=07992e1e-9aa9-4a2e-a3c6-3344c41f3d84; _xsrf=ZakZ5efDDWEzChYkf8dNTPe3xGiRAYQx; d_c0="APBox7UQeg6PTuM1gTvNr0M1Ab0iiOLaXuQ=|1541489830"; capsion_ticket="2|1:0|10:1541489834|14:capsion_ticket|44:YmVkMGM1MjA5NzY5NGQyMzgyYTg3YzMyODQ1YzFjMGE=|3edef71a2c57e786d6a61537280e5de637b47d28fe0fdee93b583a9814641213"; l_n_c=1; r_cap_id="YjFlMTQ3YzIzZWUwNGM1MzlmMmRmNTc0YmY3NjQyZTU=|1541489843|0c9b5c364e2c0029953d13aa659ef8563b1d6370"; cap_id="YWU2YWI5MTU5NDc4NDQzMjhmNmI1MTY2ZDMwMjMzYjk=|1541489843|7f439c8d715c045a0ae7fcd59592b5029781ead9"; l_cap_id="ZTU0ODc2OWMwZjdjNGRiYjhhOGY4YjhhM2I1ZWFhNjQ=|1541489843|7fa86a474e556904d3ecaf86b3c88efcc2441004"; n_c=1; z_c0=Mi4xZ0pGcUFnQUFBQUFBOEdqSHRSQjZEaGNBQUFCaEFsVk51cExPWEFEVjZlRGRhQ2piSFEtdVZpQ1cwcHNTNUFLcTNB|1541489850|d4f3a873a70506cf86081467134f3bb34230f99c; tst=r'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key,value = cookies.split('=',1)
    jar.set(key,value)
r = requests.get("https://www.zhihu.com",cookies=jar,headers=headers)
print(r.text)