import json
import time

from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)

driver.get('https://www.douyin.com/')
driver.set_window_size(1400,1200)
wait = WebDriverWait(driver,120)
# time.sleep(5)

# 这里开始自动点击登录，输入用户名和密码
print('开始自动点击登录，输入用户名和密码')

# 等待抖音首页加载完成
# wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_4011301917c5b32466dd581abd757550-scss']")))
# wait.until_not()
# print('抖音首页加载完毕')
# # 点击登录
# try:
#     driver.find_element(By.XPATH,"//button[text()='登录']").click()
# except Exception as e:
#     print(e)
# 等待登录引导界面弹出
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='NRiH5zYV']/div[@class='F55pZYYH dq39KdYi XMvzRCvu']/img")))

print('登录成功！')
# # 将浏览器驱动转移到当前页面上来
# driver.switch_to.window(driver.window_handles[-1])


# 获取list的cookies
dictCookies = driver.get_cookies()
print(dictCookies)

# 将获取到的cookies转换成字符串保存
jsonCookies = json.dumps(dictCookies)
print(jsonCookies)
print('登录网页cookies获取完毕')

with open('tiktok_cookies.txt','w',encoding='utf-8') as f:
    f.write(jsonCookies)
print('cookies保存成功！')