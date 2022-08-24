import datetime
import json
import time
import re
import random
import numpy as np
import cv2
import pymysql
from selenium.webdriver import ChromeOptions, ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import requests
import csv

# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver = webdriver.Chrome(options=option)

# driver.get('https://www.douyin.com/')

class TikTok:
    def __init__(self,keyword):
        self.video_url_element = None
        self.option = ChromeOptions()

        self.headless_option = Options()
        self.headless_option.add_argument('--headless')
        self.headless_option.add_argument('--disable-gpu')

        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=self.option)
        # self.driver = webdriver.Chrome(options=self.option,chrome_options=self.headless_option)
        self.keyword = keyword
        self.wait = WebDriverWait(self.driver, 50)

        self.list_temp = []
        self.list_all_comment = []
        with open('tiktok_cookies.txt', 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        print('读取保存的cookies成功!')
        count = 0
        # 往self.driver里添加cookies
        for cookie in listCookies:
            cookie_dict = {
                'domain': cookie.get('domain'),
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'path': '/',
                'expires': '',
                'sameSite': 'None',
                'secure': cookie.get('secure')
            }

            if count == 0:
                self.driver.get('https://www.douyin.com/')
                # self.driver.quit()

            self.driver.add_cookie(cookie_dict)
            if count == len(listCookies) - 1:
                self.driver.get('https://www.douyin.com/')
                # self.driver.refresh()
                # self.driver.switch_to.window(driver.window_handles[-1])

                # self.driver.close()

            count += 1
        self.driver.set_window_size(1400,1200)
        print('cookie到这里全部读取完毕，登录完成')
        # 等待登录引导界面弹出
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='NRiH5zYV']/div[@class='F55pZYYH dq39KdYi XMvzRCvu']/img")))

        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='_3bff5b39583f586be04d25d1198a16ea-scss']")))
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='_3bff5b39583f586be04d25d1198a16ea-scss']")))

        print('登录成功！')
        self.init_mysql()

    def init_mysql(self):
        db_config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'db': 'db_social_media_comment',
            'charset': 'utf8mb4'
        }
        self.conn = pymysql.connect(**db_config)
        self.cur = self.conn.cursor()

    # 将页面的滚动条一直向下拉，直到拉到底部
    def scroll_to_bottom(self):
        try:
            self.driver.find_element(By.XPATH,"//div[@id='captcha_container']")
            time.sleep(7)
        except Exception as e:
            print('没有跳出验证码滑动条')

        js = "return action=document.body.scrollHeight"
        # 初始化现在滚动条所在高度为0
        height = 0
        # 当前窗口总高度
        new_height = self.driver.execute_script(js)

        while height < new_height:
            self.driver.execute_script('window.scrollTo(999999999,0)')
            time.sleep(1)
            # 将滚动条调整至页面底部
            for i in range(height, new_height, 100):
                self.driver.execute_script('window.scrollTo(0, 9999999999)')
            height = new_height
            time.sleep(1)
            new_height = self.driver.execute_script(js)




    def main_steps_loops(self):
        # 第一步：选中搜索栏，输入关键字，例：索尼，然后点击"搜索"按钮;将驱动转移至新跳转的页面上来，等待新页面跳转完毕;
        # 第二步：将新页面不断地向下拖，一直拖到最底部;获取所有视频块的元素集合;
        # 第三步: 开始遍历视频块元素集合，获取当前视频的URL，进行url点击，跳转到新的视频评论页面中，并将驱动转移到新的页面上来,获取信的页面上的所有评论信息，将信息追加到总数据列表中
        # 第四步：将总数据列表中的数据，一行一行写入csv文件中，满50W条记录，则新建一份csv文件，到最后剩下来的记录，再新建一份csv文件保存
        # 结束
        #------------------------------------------------
        self.step_one()
        self.step_two()
        self.step_three()
        self.close_mysql_settings()
        # self.step_four()

    # 关闭数据库链接
    def close_mysql_settings(self):
        self.cur.close()
        self.conn.close()

    # 在搜索栏中输入关键字搜索，并将网页驱动加载到搜索后的页面中
    def step_one(self):

        # 选中搜索栏，输入关键字后，点击“搜索”按钮
        search_column_element = self.driver.find_element(By.XPATH,"//input[@class='igFQqPKs qYYUxsS2']")
        # search_column_element = self.driver.find_element(By.XPATH,"//div[@class='_7bced65174c7e8498243a4e5b0a769f7-scss']/form/input")
        search_column_element.send_keys(self.keyword)
        # //button[@class='_913d1e3dbc906c79f2227a5d1a6e4d6c-scss']
        search_button_element = self.driver.find_element(By.XPATH,"//button[@class='rB8dMXOc']")
        # search_button_element = self.driver.find_element(By.XPATH,"//button[@class='_913d1e3dbc906c79f2227a5d1a6e4d6c-scss']")
        search_button_element.send_keys(Keys.ENTER)


        # 将浏览器驱动转移到当前页面上来
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 等待搜索按钮点击完成之后的视频列表界面显示
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_72f7d11f84881fa1d76aed351818d9ff-scss']")))
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='筛选']")))
        print('搜索关键字后的页面显示完成！')

        # 点击“视频”按钮
        try:
            self.driver.find_element(By.XPATH, "//span[text()='视频']").click()
        except Exception as e:
            print('点击“视频”按钮出错，出错信息为：', e)

        time.sleep(1)
        # 点击“筛选”
        # //span[@class='fbc05f82091d1654f0af2ae017c1616b-scss']
        self.driver.find_element(By.XPATH, "//span[text()='筛选']").click()
        time.sleep(1)

        # 点击“最新发布”
        # //span[text()='最新发布']
        self.driver.find_element(By.XPATH, "//span[text()='最新发布']").click()
        time.sleep(1)

    # 在总的视频页面中，将网页拖到底后，获取所有视频的url元素集合
    def step_two(self):
        self.wait.until_not(EC.presence_of_element_located((By.XPATH, "//div[@class='captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 zGYIR']")))

        # 点击“视频”按钮
        # try:
        #     self.driver.find_element(By.XPATH,"//span[text()='视频']").click()
        # except Exception as e:
        #     print('点击“视频”按钮出错，出错信息为：',e)

        # self.wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='fbe2b2b02040793723b452dc2de2b770-scss _924e252b5702097b657541b9e3b21448-scss']")))
        # print('页面转换到"视频"页面成功！')
        bottom_count = 0
        while True:
            self.scroll_to_bottom()
            # self.roll(9999)

            try:
                # 判断是否到达底部了
                if self.driver.find_element(By.XPATH,"//div[@class='Bllv0dx6']/span"):
                    shuaxin_element = self.driver.find_element(By.XPATH,"//div[@class='Bllv0dx6']/span")
                    self.driver.execute_script('arguments[0].click();',shuaxin_element)
                    time.sleep(1)
                    continue
                # if self.driver.find_element(By.XPATH,"//div[text()='暂时没有更多了']"):
                #     break

                # if self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_7ce8711a27620d9356e5d8a0dbec1e32-scss']"))):
                #     break
            except Exception as e:
                bottom_count +=1
                if bottom_count >=4:
                    try:
                        self.driver.find_element(By.XPATH,"//div[text()='暂时没有更多了']")
                        break
                    except Exception as e:
                        try:
                            self.driver.find_element(By.XPATH, "//div[text()='暂时没有更多评论']")
                            break
                        except Exception as e:
                            print('把所有视频拖到最低部出错，出错信息为:',e)


        try:
            self.video_blocks_url_elements_list = self.driver.find_elements(By.XPATH,"//li[@class='aCTzxbOJ pYgrEk__']/div/div/a[1]")
            # self.video_blocks_url_elements_list = self.driver.find_elements(By.XPATH,"//li[@class='cfe08356d79318ea5da702f1065736dc-scss a3cc5072a10a34f3d46c4e722ef788c1-scss']/div/a[1]")
            # self.video_blocks_url_elements_list = self.driver.find_elements(By.XPATH,"//li[@class='cfe08356d79318ea5da702f1065736dc-scss a3cc5072a10a34f3d46c4e722ef788c1-scss']/div/a[1]")
            # self.video_blocks_url_elements_list = self.driver.find_elements(By.XPATH,"//div[@class='cdfb2696b192e707e529d93274fe5752-scss']/div[2]/ul/li/div/a[1]")
            # print(self.video_blocks_url_elements_list)  # 获取到所有视频的url元素
            print('获取到所有视频的url元素,一共%d个'%len(self.video_blocks_url_elements_list))  # 获取到所有视频的url元素
        except Exception as e:
            print('获取到所有视频的url元素出错，出错信息为：',e)

    # 获取所有的视频url元素列表集，遍历点击url元素，将视频拖到底之后，点击所有评论区按钮
    def step_three(self):
        global comment_button_user_elements, list_comment_date, comment_list_elements, head_comment, head_comment_date
        video_count = 0
        # 遍历当前的视频url元素
        for self.video_url_element in self.video_blocks_url_elements_list:
            video_count += 1
            # if video_count == 5:
            #     break
            if video_count < 100:
                continue
            if video_count == 200:
                break
            print('当前爬取的是第当前爬取的是第{}个视频了'.format(video_count))
            #-------------------------------数据 0-100完成
            time.sleep(1)


            # current_video_url = self.video_url_element.get_attribute('href')
            # print('当前的视频url为：',current_video_url)
            # self.driver.get(current_video_url)
            # self.video_url_element.click() # 点击当前视频urlcubans
            # self.video_url_element.send_keys(Keys.ENTER)
            self.driver.execute_script("arguments[0].click();",self.video_url_element)
            print('当前视频url点击完毕！')
            time.sleep(3)
            windows_num = len(self.driver.window_handles)
            print('当前网页页数为：',windows_num)
            while windows_num !=3:
                self.driver.execute_script("arguments[0].click();",self.video_url_element)
                time.sleep(3)
                windows_num = len(self.driver.window_handles)
                print('当前window网页数量为：',windows_num)
            # 将浏览器驱动转移到当前页面上来
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # 等待视频页面加载完毕
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='Yja39qrE']/div/div[@class='r3zuuG3C'][1]")))
            # self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='f03f306b3850ed6b37197944d685ef92-scss']")))
            # self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='videoContainer xgplayer-container-inactive']")))
            print('视频页面加载完毕！')
            print('视频页面开始往下拖！')
            while True:

                try:
                    self.scroll_to_bottom()
                    try:
                        if self.driver.find_element(By.XPATH,"//div[@class='_2b22e342b8c47a455d1f3ef37ea9e7b2-scss _418f31c5788fcd221a966068331a4aa5-scss']"):
                            break                            #//div[@class='_2b22e342b8c47a455d1f3ef37ea9e7b2-scss _418f31c5788fcd221a966068331a4aa5-scss']
                    except Exception as e:
                        print('判断到达视频评论区底部的步骤有错，div，错误信息为：',e)

                    try:
                        # 如果等到了页面最底部的element标签，则跳出循环
                        if self.driver.find_element(By.XPATH,"//p[@class='_2b22e342b8c47a455d1f3ef37ea9e7b2-scss _418f31c5788fcd221a966068331a4aa5-scss']"):
                            break
                    except Exception as e:
                        print('判断到达视频评论区底部的步骤有错，p，错误信息为：', e)

                        #//div[@class='edb6f0127b7d9bef4b22ed123b3dd140-scss']
                    try:
                        # 如果该视频暂时没有评论信息时
                        if self.driver.find_element(By.XPATH,"//div[@class='edb6f0127b7d9bef4b22ed123b3dd140-scss']"):
                            break
                    except Exception as e:
                        print('该视频是有评论信息的，没有找到提示标签的报错信息为：',e)


                        #//div[@class='_3f6f0f96f137417475844d1f8deeabd7-scss']
                    try:
                        # 如果有“载入中”这个标签元素的话
                        if self.driver.find_element(By.XPATH,"//div[contains(text(),'暂时没有更多评论')]"):
                            break
                    except Exception as e:
                        print('页面还没到底')

                    try:
                        # 如果有“载入中”这个标签元素的话
                        if self.driver.find_element(By.XPATH,"//div[contains(text(),'暂无评论')]"):
                            break
                    except Exception as e:
                        print('定位"暂无评论"元素出错，出错信息为：',e)

                    try:
                        # 如果有“载入中”这个标签元素的话                         部分评论因未授权抖音，暂不支持查看
                        if self.driver.find_element(By.XPATH,"//p[text()='部分评论因未授权抖音，暂不支持查看']"):
                            break
                    except Exception as e:
                        print('定位"暂无评论"元素出错，出错信息为：',e)
                    #_2b22e342b8c47a455d1f3ef37ea9e7b2-scss _418f31c5788fcd221a966068331a4aa5-scss
                except Exception as e:
                    print('当前视频页面中，往下拖的时候，页面加载评论的时候超时了！出错信息为：',e)
            print('视频页面拖到底了！')
            print('获取当前视频的所有按钮元素')

            # //button[@class='QRKcPlh-'] 用户展开xx条回复
            # //button[@class='uC2PejCF'] 作者展开xx条回复，用户展开更多回复，收起
#--------------------------------------------------------------------------------------------
            # //button[@class='N10j3PcL'] 作者展开xx条回复
            # //button[@class='zeyRYM2J'] 用户展开xx条回复
            try:
                # 获取用户展开xx条回复的所有按钮元素
                comment_button_author_elements = self.driver.find_elements(By.XPATH,"//button[@class='N10j3PcL']")
                # comment_button_elements = self.driver.find_elements(By.XPATH,"//div[@class='c7ee22de401c856152e3646bffd656a3-scss']/div[2]/button")
            except Exception as e:
                print('获取用用户展开xx条回复按钮元素集出错，出错信息为：',e)
            print('用户展开xx条回复，一共有%d个按钮元素' % len(comment_button_author_elements))

            # 遍历每一个按钮元素，并进行按键操作,点击‘展开**条回复’
            for comment_button_author_element in comment_button_author_elements:
                time.sleep(1)
                try:
                    # comment_button_user_element.click()
                    self.driver.execute_script("arguments[0].click();", comment_button_author_element)
                    # comment_button_user_element.send_keys(Keys.ENTER)
                except Exception as e:
                    print("作者展开xx条回复按钮点击出错，出错信息为:", e)

            try:
                # 获取用户展开xx条回复的所有按钮元素
                comment_button_user_elements = self.driver.find_elements(By.XPATH,"//button[@class='zeyRYM2J']")
                # comment_button_elements = self.driver.find_elements(By.XPATH,"//div[@class='c7ee22de401c856152e3646bffd656a3-scss']/div[2]/button")
            except Exception as e:
                print('获取用用户展开xx条回复按钮元素集出错，出错信息为：',e)
            print('用户展开xx条回复，一共有%d个按钮元素' % len(comment_button_user_elements))

            # 遍历每一个按钮元素，并进行按键操作,点击‘展开**条回复’
            for comment_button_user_element in comment_button_user_elements:
                time.sleep(1)
                try:
                    # comment_button_user_element.click()
                    self.driver.execute_script("arguments[0].click();", comment_button_user_element)
                    # comment_button_user_element.send_keys(Keys.ENTER)
                except Exception as e:
                    print("用户展开xx条回复按钮点击出错，出错信息为:", e)

            # //button[@class='QRKcPlh-'] 用户展开xx条回复
            # //button[@class='uC2PejCF'] 作者展开xx条回复，用户展开更多回复，收起
            time.sleep(1)
            # try:
            #     comment_button_elements = self.driver.find_elements(By.XPATH,"//div[@class='x+4i3kAc']")
            #     # comment_button_elements = self.driver.find_elements(By.XPATH,"//div[@class='c7ee22de401c856152e3646bffd656a3-scss']/div[2]/button")
            # except Exception as e:
            #     print('获取全部用户评论数据块元素出错，出错信息为：',e)
            #
            # print('全部用户评论数据块元素，有%d个'%len(comment_button_elements))

            while True:
                try:
                    spread_more_element = self.driver.find_element(By.XPATH,"//button/span[contains(text(),'展开更多')]")
                    self.driver.execute_script("arguments[0].click();", spread_more_element)
                    time.sleep(1)
                except Exception as e:
                    break


            print('至此，当前视频页面下的所有评论，展开完全！')
            # 先作测试用，不遍历下一个视频
            #----------至此，可以开始在当前url对应的视频页面中，获取视频标题、视频发布者、视频发布时间，还有关于该视频所有的评论内容、评论者、评论时间----------
            current_url = self.driver.current_url
            try:
                video_title = self.driver.find_element(By.XPATH,"//h1[@class='z8_VexPf']/span[@class='Nu66P_ba']/span[1]/span/span/span").text
            except Exception as e:
                video_title =''
                print('获取视频标题元素出错，出错信息为：',e)
            dianzaishu = self.driver.find_element(By.XPATH,"//div[@class='kr4MM4DQ'][1]/span[@class='CE7XkkTw']").text

            time.sleep(1)
            # 获取当前视频下的所有评论区元素块列表集
            comment_block_elements = self.driver.find_elements(By.XPATH,"//div[@class='tMWlo89q']/div[@class='BOJBWh64']/div[@class='mQjJJImN HO1_ywVX']/div[3]/div")
            print('一共获取到了%d个评论区元素块!'%len(comment_block_elements))

            # 遍历所有评论区元素块列表集，即每一个评论区块元素，获取每一个评论区的头评论的评论内容，评论时间

            # # 获取到了头评论的内容和日期元素集合，如何进行11对应？
            # head_comments = self.driver.find_elements(By.XPATH,"//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/p/span/span/span/span/span/span").text
            # head_comment_dates = self.driver.find_elements(By.XPATH,"div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[1]/div[1]/p").text

            # 循环遍历每一个评论块元素，获取当前评论块元素
            for comment_block_element in comment_block_elements:
                try:
                    head_comment = ''
                    print('--------------------------头评论中的数据-----------------------------')
                    # 获取评论头的评论内容和评论时间
                    try:
                                                                                    #/div/div[2]/div/p/span/span/span/span/span/span
                        head_comment = comment_block_element.find_element(By.XPATH,"./div/div[2]/div/p/span/span/span/span/span/span").text
                    except Exception as e:
                        print('获取一级评论内容出错，出错信息为：',e)
                    try:
                        head_comment_date = comment_block_element.find_element(By.XPATH,"./div/div[2]/div/div[2]/div/p").text
                    except Exception as e:
                        print('获取一级评论日期出错，出错信息为：',e)
                    if head_comment =='':
                        continue
                    self.list_temp.append(head_comment)
                    self.list_temp.append(head_comment_date)
                    self.list_temp.append('comment')
                    self.list_temp.append(current_url)
                    self.list_temp.append(video_title)
                    self.list_temp.append(dianzaishu)
                    print(self.list_temp)
                    #--------------这里需要添加数据库数据插入操作
                    sql = 'insert into tb_TikTok values(%s,%s,%s,%s,%s,%s)'
                    self.cur.execute(sql, [head_comment, head_comment_date, 'comment', current_url, video_title,
                                           dianzaishu])
                    self.conn.commit()
                    self.list_temp = []


                    print('--------------------------二级评论中的数据-----------------------------')
                    # 当前评论块中，二级评论的评论块元素集合获取
                    try:
                        comment_list_elements = comment_block_element.find_elements(By.XPATH, "./div/div[2]/div[2]/div")
                    except Exception as e:
                        print('获取二级评论的评论列表元素集合出错，出错信息为:',e)
                    for comment_list_element in comment_list_elements:
                        list_comment = ""
                        try:
                            list_comment = comment_list_element.find_element(By.XPATH,"./div[2]/div/p/span/span/span/span/span/span").text
                            print('当前视频下，二级评论的评论内容为：', list_comment)
                        except Exception as e:
                            print('获取二级评论的评论内容时出错，出错原因：', e)

                        try:
                            list_comment_date = comment_list_element.find_element(By.XPATH,"./div[2]/div/div[2]/div/p").text
                            print('当前视频下，二级评论的评论日期为：', list_comment_date)
                        except Exception as e:
                            print('获取二级评论的评论日期时出错，出错原因：', e)
                        if list_comment == '':
                            continue

                        self.list_temp.append(list_comment)
                        self.list_temp.append(list_comment_date)
                        self.list_temp.append('comment')
                        self.list_temp.append(current_url)
                        self.list_temp.append(video_title)
                        self.list_temp.append(dianzaishu)
                        print(self.list_temp)
                        sql = 'insert into tb_TikTok values(%s,%s,%s,%s,%s,%s)'
                        self.cur.execute(sql, [list_comment, list_comment_date, 'comment', current_url, video_title,
                                               dianzaishu])
                        self.conn.commit()

                        self.list_temp = []
                except Exception as e:
                    print('获取评论的时候出错，出错原因：',e)

            self.driver.close()
            print('这里执行里self.driver.close()方法！')
            handles = self.driver.window_handles
            print('一共有%d个网页'%len(handles))
            self.driver.switch_to.window(self.driver.window_handles[-1])
            print('网页驱动回到了总视频目录下了！')
            self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='筛选']")))
            print('总视频目录网页加载完毕')

    # 循环遍历总数据列表，将总数据列表中的列表数据，一行一行写入csv文件中
    def step_four(self):
        count = 0 # 50W条记录，计数用
        n = 1 # 每一份csv文件个数，计数用
        list_data_500000 =[]  # 定义一个列表，存放50w条记录
        for item_list in self.list_all_comment:
            list_data_500000.append(item_list)
            count += 1

            if count >= 500000:
                with open('data/TikTok_%s_%d.csv'%(self.keyword,n),'a',encoding='utf-8') as  f:
                    writer = csv.writer(f,delimiter = ',')
                    writer.writerow(['comment','comment_time','source_type'])
                    for item_list in self.list_data_500000:
                        writer.writerow(item_list)

                n += 1
                count = 0
                list_data_500000 = []

        # 对最后剩余的零头文件数据进行读取写入
        with open('data/TikTok_%s_%d.csv'%(self.keyword,n), 'w', encoding='utf-8-sig',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['comment', 'comment_time', 'source_type'])
            for item_ in list_data_500000:
                writer.writerow(item_)

Tik1 = TikTok('索尼元宇宙') # 索尼大法好 索尼设备 索尼科技 索尼中国 索尼信仰 索尼智慧 索尼未来 索尼前沿 索尼世界 索尼高度 索尼深度
 # 索尼广度 索尼精度
Tik1.main_steps_loops()
