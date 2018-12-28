from selenium import webdriver

browser = webdriver.Chrome()  # 声明浏览器对象
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q') # ID选择器
input_second = browser.find_element_by_css_selector('#q') # CSS选择器
input_third = browser.find_element_by_xpath('//*[@id="q"]') # Xpath
# print(browser.page_source)
print(input_first,input_second,input_third)
browser.close()


