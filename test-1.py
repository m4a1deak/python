from selenium import webdriver
browser = webdriver.Chrome()
import time
#browser.get('https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8')
#input_1 = browser.find_element_by_xpath('//div[@id="J_bottomPage"]//a[@class="btn btn-default"]')
#input_2 = browser.find_element_by_xpath('//div[@id="J_bottomPage"]//input[@class="input-txt"]')
#input_3 = browser.find_element_by_xpath('//div[@id="J_bottomPage"]//a[@class="curr"]')
#input_3 = browser.find_element_by_xpath('//div[@id="J_goodsList"]//li[@class="gl-item"]')
#print(input_1,input_2,input_3)



print('____________------_________')
browser.get('https://auth.geetest.com/login/')
time.sleep(30)
print('+++++++')
input_1 = browser.find_elements_by_class_name('ivu-input')
print(input_1)





