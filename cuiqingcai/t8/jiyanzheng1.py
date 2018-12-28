from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import time

EAMIL = '1030657055@qq.com'
PASSWORD = 'guanhui123123'


class CrackGeettest():
    def __init__(self):
        print('xxxx')
        self.url = 'https://auth.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 30)
        self.eamil = EAMIL
        self.password = PASSWORD
        self.get_email_pass()
        button = self.get_geetest_button()
        button.click()
        slider = self.get_slider()
        slider.click()
        x = self.get_getest_image()
        print(x)

    def get_geetest_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_email_pass(self):
        list = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'ivu-input')))
        list[0].clear()
        list[0].send_keys(self.eamil)
        list[1].clear()
        list[1].send_keys(self.password)

    def get_position(self):
        img = self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME,
                'geetest_canvas_img'))
        print(img)
        time.sleep(2)
        location = img.location
        size = img.size
        top = location['y']
        bottom = location['y'] + size['height']
        left = location['x']
        right = location['x'] + size['width']
        return (top, bottom, left, right)

    def get_getest_image(self, name='captcha.png'):
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop(left, top, right, bottom)
        return captcha

    def get_slider(self):
        slider = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, 'geetest_slider_button')))
        return slider


t = CrackGeettest()
