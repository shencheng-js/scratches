# 自动打开百度搜索人民币
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(2)
text_input = driver.find_element_by_id('kw')
# send_keys 给input标签输入
text_input.send_keys('人民币')
sleep(2)
driver.find_element_by_id('su').click()

sleep(3)

#获取当前的页面源码数据（渲染后的数据）
print(driver.page_source)
driver.quit()