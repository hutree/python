import time
from time import sleep

from selenium import webdriver

webDriver = webdriver.Chrome()
webDriver.get('https://www.baidu.com/')
inputKw = webDriver.find_element_by_id('kw')
inputKw.send_keys("民族")
sleep(2)
print(inputKw.get_attribute('value'))

cur_cookies = webDriver.get_cookies()
print(cur_cookies)
print(type(cur_cookies))

file_name = str(time.time()) + '.png'
webDriver.save_screenshot(file_name)
