from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# 隐式延迟
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)


# 显式延迟

browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 1) # 指定等待时长
input = wait.until(
    EC.presence_of_element_located((By.ID, 'q'))) # 两个括号
# button = wait.until(
#     EC.element_to_be_clickable(
#         (By.CSS_SELECTOR, '.btn-search')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
