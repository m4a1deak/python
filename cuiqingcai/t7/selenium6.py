from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('python')  # 输入python
time.sleep(3)
input.clear()  # 情况输入框
input.send_keys('java')  # 输入java
button = browser.find_element_by_class_name('btn-search')  # 动作
button.click()
