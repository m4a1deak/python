from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# li = browser.find_elements_by_css_selector('.service-bd li')
li = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(li)
browser.close()
