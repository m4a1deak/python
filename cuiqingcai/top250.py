import requests
import re
import time
import json
import urllib.request

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    #print(response.text)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<li>.*?item.*?pic.*?em.*?>(.*?)</em>.*?img.*?src="(.*?)".*?hd.*?title.*?>(.*?)</span>.*?bd.*?p.*?>(.*?)<br>(.*?)</p>.*?average.*?>(.*?)</span>.*?content.*?<span>(.*?)</span>.*?inq.*?>(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern,html)
    print(items)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'fenshu':item[5],
            'pingjia':item[6],
            'jianjie':item[7]
        }

def main(num):
    url = 'https://movie.douban.com/top250?start='+str(num)+'&filter='
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

def write_to_file(content):
    with open('douban1.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) +'\n')
        urllib.request.urlretrieve(content['image'], 'doubanimg/' + content['title'] + '.jpg')

if __name__ == '__main__':
    for i in range(10):
        main(num =i*25)
        time.sleep(2)

#
