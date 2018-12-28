import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import  Pool

headers = {
    'Host':'www.toutiao.com',
    'Referer':'www.toutiao.com//search_content', ### 从哪个页面发出
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'山水画',
        'autoload':'true',
        'count':'20',
        'cur_tab':'3',
        'from':'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title');
            images = item.get('image_list')
            for image in images:
                yield {
                    'image':'http:'+image.get('url'),
                    'title':title
                }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            print(response.content)
            print(md5(response.content))
            print(md5(response.content).hexdigest())
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Alredy Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 2

if __name__ ==  '__main__':
    #res = get_page(20)
    #for s in get_images(res):
    #    print(type(s))
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()