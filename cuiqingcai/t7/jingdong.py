from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from selenium.common.exceptions import NoSuchElementException
import pymongo
from urllib.parse import urlencode
import time
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 200)
mongo_url = 'localhost'
mongo_db = 'jd'
mongo_collection = 'products'
client = pymongo.MongoClient(mongo_url)
db = client[mongo_db]
max_page = 100
params = {
    'keyword': '笔记本',
    'enc': 'utf-8'
}


def index_page(page):
    """
    加载页面
    """
    print('正在爬取第', page, '页')
    try:
        #url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8'
        url = 'https://search.jd.com/Search?' + urlencode(params)
        print(url)
        browser.get(url)
        #target = browser.find_element_by_id("J_bottomPage")
        # browser.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        # browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        if page > 1:
            time.sleep(60)
            input = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@id="J_bottomPage"]//input[@class="input-txt"]')))
            submit = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="J_bottomPage"]//a[@class="btn btn-default"]')))
            input.clear()
            input.send_keys(page)
            submit.click()
        print("判断结束!")
        wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH,
                 '//div[@id="J_bottomPage"]//a[@class="curr"]'),
                str(page)))
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@id="J_goodsList"]//li[@class="gl-item"]')))
        get_products()
    except NoSuchElementException:
        print("No Logo")
    except TimeoutException as e:
        print(str(e))
        print(repr(e))
        print('超时!')
    except Exception as e:
        print(str(e))
        print(repr(e))


def get_products():
    """
    解析结果集
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#J_goodsList .gl-warp .gl-item').items()
    for item in items:
        # print(item.find('.p-name').text())
        # print(item.find('.p-price').text())
        # print(item.find('.p-commit').text())
        # print(item.find('.p-shop').text())
        # print(item.find('.p-icons').text())
        # print("="*50)
        product = {
            'biaoti': item.find('.p-name').text().replace('\n', ''),
            'jiage': item.find('.p-price').text().replace('\n', ''),
            'guanzhu': item.find('.p-commit').text().replace('\n', ''),
            'dianpu': item.find('.p-shop').text().replace('\n', ''),
            'ziying': item.find('.p-icons').text().replace('\n', '')
        }
        print(product)
        save_to_mongodb(product)


def save_to_mongodb(product):
    """
    保存到mongodb
    """
    print(type(product))
    try:
        if db[mongo_collection].insert(product):
            print("保存成功")
    except Exception as e:
        print(str(e))
        print(repr(e))
    print("=" * 50)


def main():
    """
    遍历每一页
    """
    for i in range(1, max_page + 1):
        index_page(i)


if __name__ == '__main__':
    main()
