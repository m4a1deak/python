import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
html = requests.get(url,headers=headers).text
#print(html)
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    print('='*100)
    #print(item)
    print(item.find('h2').text())
    wenzhangming = item.find('h2').text()
    print(item.find('.author-link-line').text())
    zuozhe = item.find('.author-link-line').text()
    #print(item.find('.content').text())
    print(pq(item.find('.content').html()).text())
    neirong = pq(item.find('.content').html()).text()

    #file = open('explore.txt','a',encoding='utf-8')
    #file.write('\n'.join([wenzhangming,zuozhe,neirong]))
    #file.write('\n'+'='*50+'\n')
    #file.close()
    with open('explore.txt','a',encoding='utf-8') as file:
        file.write('\n'.join([wenzhangming,zuozhe,neirong]))
        file.write('\n'+'='*50+'\n')


print("ok")