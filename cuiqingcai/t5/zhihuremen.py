import requests
from pyquery import PyQuery as pq
import pymongo
import time
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.db
collection = db.zhihu

proxy_host = 'http-dyn.abuyun.com'
proxy_pory = '9020'
proxy_user = 'HQ2LNZC68778D72D'
proxy_pass = 'A968B377C19502D7'
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
headers = {
    'Accept': '*/*',
    'Referer': 'https://www.zhihu.com/explore',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'cookie': 'tgw_l7_route=e0a07617c1a38385364125951b19eef8; _zap=2072e08f-96ab-46b7-993f-b950b68fbe0f; _xsrf=FqY77HlaQVw7epYlTWE7Xb7tBCIdV8Oq; d_c0="ADAhhieMlg6PTlQukM3Ejzlkc7Qr9Tv4bG0=|1543401238"; capsion_ticket="2|1:0|10:1543401241|14:capsion_ticket|44:Zjk2MjFmODZmNzRiNDQ5Mjk4MjJlZDIyNzc5NjQyYWY=|5fc8fdde83d0619a04b847c22ba2ea8a9aabb67c22999f0d2bf6a0dc79026b08"; l_n_c=1; r_cap_id="NGZiOTljNThkMGQ4NDc1Mzg1OWYwODVjZWQ5YzIyMmI=|1543401246|19737fd0a0d103266344f2c85c1ca11156458539"; cap_id="OGE0NTBlNmNhODk4NDRmZmI1MjNmNjUzYjM4YTkyNGI=|1543401246|a0c39786dea9c75099c0a7a2263b6dc4f652a0cf"; l_cap_id="Njc1OTQwYTQ4ZmUyNGYxMjk0ZDQxMDk1NWJjOGRiZWI=|1543401246|0be5e1ea7d00da47b47755bafaf55cfe8b85c394"; n_c=1; z_c0=Mi4xZ0pGcUFnQUFBQUFBTUNHR0o0eVdEaGNBQUFCaEFsVk5JNzNyWEFCQjBPcC1Vd09yTWFsazNNY2RkMG02Y0FCZWdR|1543401251|97a9079b9b1bc2d98e4ff3af72e1375102230414; tst=h; q_c1=be79873485434774b8b81bc4685d9772|1543401504000|1543401504000; __utma=51854390.1707457777.1543401508.1543401508.1543401508.1; __utmb=51854390.0.10.1543401508; __utmc=51854390; __utmz=51854390.1543401508.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20151226=1^3=entry_date=20151226=1'
}


def get_page(page):
    url = 'https://www.zhihu.com/node/ExploreAnswerListV2?params={"offset":%d,"type":"day"}'
    res = requests.get(url % page, headers=headers, proxies=proxies)
    text = res.text
    if text:
        doc = pq(text)
        list = doc('div .feed-item').items()
        for i in list:
            zhihu = {}
            zhihu['title'] = i.find('a.question_link').text()
            zhihu['content'] = pq(i.find('textarea').html()).text()
            zhihu['count1'] = i.find('div.zm-votebar .count').text() + "个赞"
            zhihu['count2'] = i.find('a.toggle-comment').text()
            zhihu['zuozhe'] = i.find('div.answer-head a.author-link').text()
            zhihu['bio'] = i.find('div.answer-head .bio').text()
            zhihu['time'] = i.find(
                'p.visible-expanded a.answer-date-link').text()
            yield zhihu
    else:
        print("空")


def save(t):
    result = collection.insert(t)
    print(result)


if __name__ == '__main__':
    for page in range(200, 1000000, 5):
        tt = get_page(page)
        for t in tt:
            save(t)
