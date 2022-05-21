from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

webDriver = webdriver.Chrome()
print("打开百度")
webDriver.get('https://www.baidu.com/')
webDriver.maximize_window()

# 打开新闻网页
ele = webDriver.find_element_by_link_text("新闻")
ActionChains(webDriver).click(ele).perform()
sleep(2)

# 悬停鼠标
webDriver.switch_to.window(webDriver.window_handles[1])
e2 = webDriver.find_element_by_class_name('item.acces-sibility')
ActionChains(webDriver).move_to_element(e2).perform()
sleep(2)
#鼠标右键
target = webDriver.find_element_by_id('s_ipt_wr')
ActionChains(webDriver).context_click(target).perform()
sleep(2)

# 拖动操作
source = webDriver.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a')
ActionChains(webDriver).click_and_hold(source).drag_and_drop(source, target).perform()
sleep(2)
