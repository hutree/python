from time import sleep
from selenium import webdriver


def findkw(kw):
    webDriver = webdriver.Chrome()
    # 打开百度的网页
    webDriver.get('https://www.baidu.com/')
    inputKw = webDriver.find_element_by_id('kw')
    inputKw.send_keys(kw)
    sleep(1)
    webDriver.find_element_by_xpath('//*[@id="su"]').click()
    webDriver.quit()
    return


i = 0
while i < 10:
    findkw(str(i))
    print("运行完第" + str(i) + "次")
    sleep(1)
    i += 1
