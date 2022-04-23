from time import sleep

from selenium import webdriver

webDriver = webdriver.Chrome()
webDriver.get('https://www.baidu.com/')
inputKw = webDriver.find_element_by_id('kw')
inputKw.send_keys("民族")
sleep(2)
webDriver.find_element_by_xpath('//*[@id="su"]').click()

