from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import time
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='12345678',
    port=3306,
    db='py')
cursor = db.cursor()
base_url = 'https://m.weibo.cn/api/container/getIndex?'
num = 0
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/6077805247',  # 从哪个页面发出
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076036077805247',
        'page': page
    }
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        if items:
            for item in items:
                item = item.get('mblog')
                if item:
                    weibo = {}
                    weibo['name'] = item.get('user').get('screen_name')
                    weibo['uid'] = item.get('id')
                    weibo['text'] = pq(item.get('text')).text()
                    weibo['zhuanfa'] = item.get('reposts_count')
                    weibo['dianzan'] = item.get('attitudes_count')
                    weibo['pinglun'] = item.get('comments_count')
                    weibo['time'] = item.get('edit_at')
                    weibo['source'] = item.get('source')
                    yield weibo
            else:
                print('*' * 100)


def tomysql(result):
    keys = ','.join(result.keys())
    values = ','.join(['%s'] * len(result))
    sql = 'insert into weibo ({keys}) values({values}) '.format(keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(result.values())):
            print('Successful')
            db.commit()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # for page in range(1,2):
    #    json = get_page(page)
    #    print(json)
    #    results = parse_page(json)
    #    for result in results:
    #        print(result)
    # json = get_page(1)
    # print(json)
    # pages = parse_page(json)
    # print(pages)
    # print(item)
    for page in range(1, 1000000000):
        json = get_page(page)
        print(json)
        results = parse_page(json)
        for result in results:
            if result:
                print("====" * 100)
                tomysql(result)
                time.sleep(0.1)
    db.rollback()
