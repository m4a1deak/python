from selenium import webdriver
from selenium.webdriver.common.by import By

# find_element_by_id(id) 等价于 find_element(By.ID,id)
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()
