import datetime
import json
import time
import re
import random
import numpy as np
import cv2
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
        self.option = ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=self.option)
        self.keyword = keyword
        self.wait = WebDriverWait(self.driver, 60)

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

        # 等待登录引导界面弹出
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='D+4cr216']")))
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='_3bff5b39583f586be04d25d1198a16ea-scss']")))

        print('登录成功！')

    def save_slider_pic(self):
        html_big_pic = requests.get(self.big_pic_element_url)
        html_slider_pic = requests.get(self.slider_pic_element_url)

        with open('pic_slide/big_pic.jpg','wb') as f1:
            f1.write(html_big_pic.content)

        with open('pic_slide/slider_pic.jpg', 'wb') as f2:
            f2.write(html_slider_pic.content)

    def calculate_distance_(self):
        image = cv2.imread("pic_slide/big_pic.jpg", cv2.IMREAD_GRAYSCALE)
        binary = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 15)
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        se = cv2.morphologyEx(se, cv2.MORPH_CLOSE, (2, 2))
        mask = cv2.dilate(binary, se)
        cv2.imshow("image", image)

        mask1 = cv2.bitwise_not(mask)
        binary = cv2.bitwise_and(image, mask)
        result = cv2.add(binary, mask1)
        cv2.imwrite('pic_slide/temp.jpg', result)

        # 睡眠1s后，重新读取中间照片
        time.sleep(1)
        result = cv2.imread('pic_slide/temp.jpg')
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)  # 灰度
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # 5*5的内核高斯平滑
        thresh = cv2.threshold(blurred, 108, 255, cv2.THRESH_BINARY)[1]  # 阈值化，阈值化后形状被表示成黑色背景上的白色前景
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)  # iterations进行3次操作
        cv2.imwrite('pic_slide/temp.jpg', opening)

        # 读取处理过后的temp.jpg文件
        img = cv2.imread('pic_slide/temp.jpg', 1)
        dst = cv2.GaussianBlur(img, (5, 5), 1.5)
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=3)  # iterations进行3次操作

        contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            # 图像轮廓及中心点坐标
            M = cv2.moments(cnt)
            center_x = int(M['m10'] / M['m00'])
            center_y = int(M['m01'] / M['m00'])

            # 计算当前轮廓的周长
            perimeter = cv2.arcLength(cnt, True)

            # 计算当前轮廓的面积
            area = cv2.contourArea(cnt)

            if perimeter>=285 and perimeter<=375 and area >=1100  and area<=4000:
                print('满足周长和面积条件，现在进入了方法内部！')
                print('perimeter=', perimeter)
                print('area=', area)
                print('center_x:', center_x)
                print('center_y:', center_y)
                print('--------------------------------------------------------')
                cv2.drawContours(img, [box], -1, (0, 0, 255), 3)  # 画矩形框
                cv2.circle(img, (center_x, center_y), 7, 128, -1)  # 绘制中心点
                str1 = '(' + str(center_x) + ',' + str(center_y) + ')'
                cv2.putText(img, str1, (center_x - 50, center_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255, 255, 0), 2, cv2.LINE_AA)  # 绘制坐标点位
                cv2.imshow('show', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return center_x
            else:
                cv2.drawContours(img, [box], -1, (0, 0, 255), 3)  # 画矩形框
                cv2.circle(img, (center_x, center_y), 7, 128, -1)  # 绘制中心点
                str1 = '(' + str(center_x) + ',' + str(center_y) + ')'
                cv2.putText(img, str1, (center_x - 50, center_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 2,cv2.LINE_AA)  # 绘制坐标点位
                cv2.imshow('show', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


    # 将页面的滚动条一直向下拉，直到拉到底部
    def scroll_to_bottom(self):
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

    # def scroll_to_bottom(self):
    # def roll(self,rolnum):
    #     # 滚动到评论底部
    #     for ii in range(rolnum):
    #         # if self.driver.find_element_by_xpath('//*[@id="comment"]/div/div[2]/div/div[@class="loading-state"]').text=='没有更多评论':
    #         #     break
    #         if rolnum > 2000:
    #             if ii % 100 == 99:
    #                 self.driver.execute_script('window.scrollTo(999999999,0)')
    #                 time.sleep(1)
    #             self.driver.execute_script('window.scrollTo(0, 999999999)')
    #
    #         else:
    #             if rolnum > 1000:
    #                 if ii % 40 == 39:
    #                     self.driver.execute_script('window.scrollTo(999999999,0)')
    #                     time.sleep(1)
    #                 self.driver.execute_script('window.scrollTo(0, 999999999)')
    #
    #             else:
    #                 if ii % 20 == 19:
    #                     self.driver.execute_script('window.scrollTo(999999999,0)')
    #                     time.sleep(1)
    #
    #                 self.driver.execute_script('window.scrollTo(0, 999999999)')

    def get_move_track(self,distance):
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * (4 / 5)  # 前4/5段加速 后1/5段减速
        # 计算间隔
        t = random.randint(2, 3) / 10
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速度为+10
                a = 10
            else:
                # 加速度为-3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

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
        self.step_four()

    # 在搜索栏中输入关键字搜索，并将网页驱动加载到搜索后的页面中
    def step_one(self):

        # 选中搜索栏，输入关键字后，点击“搜索”按钮
        search_column_element = self.driver.find_element(By.XPATH,"//input[@placeholder='搜索视频和用户']")
        search_column_element.send_keys(self.keyword)
        # //button[@class='_913d1e3dbc906c79f2227a5d1a6e4d6c-scss']
        search_button_element = self.driver.find_element(By.XPATH,"//button[@class='kT0ePbyQ']")
        search_button_element.send_keys(Keys.ENTER)
        # 将浏览器驱动转移到当前页面上来
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 等待搜索按钮点击完成之后的视频列表界面显示
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_72f7d11f84881fa1d76aed351818d9ff-scss']")))
        print('搜索关键字后的页面显示完成！')

    # 在总的视频页面中，将网页拖到底后，获取所有视频的url元素集合
    def step_two(self):
        self.wait.until_not(EC.presence_of_element_located((By.XPATH, "//div[@class='captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 zGYIR']")))
        while True:
            self.scroll_to_bottom()
            # self.roll(9999)
            try:
                # 判断是否到达底部了
                if self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_7ce8711a27620d9356e5d8a0dbec1e32-scss']"))):
                    break
            except Exception as e:
                print("主视频区页面中，往下拖的时候，页面加载视频的时候超时了！出错信息为：",e)
        try:
            self.video_blocks_url_elements_list = self.driver.find_elements(By.XPATH,"//li[@class='cfe08356d79318ea5da702f1065736dc-scss a3cc5072a10a34f3d46c4e722ef788c1-scss']/div/a[1]")
            # self.video_blocks_url_elements_list = self.driver.find_elements(By.XPATH,"//div[@class='cdfb2696b192e707e529d93274fe5752-scss']/div[2]/ul/li/div/a[1]")
            # print(self.video_blocks_url_elements_list)  # 获取到所有视频的url元素
            print('获取到所有视频的url元素,一共%d个'%len(self.video_blocks_url_elements_list))  # 获取到所有视频的url元素
        except Exception as e:
            print('获取到所有视频的url元素出错，出错信息为：',e)

    # 获取所有的视频url元素列表集，遍历点击url元素，将视频拖到底之后，点击所有评论区按钮
    def step_three(self):
        video_count = 0
        # 遍历当前的视频url元素
        for self.video_url_element in self.video_blocks_url_elements_list:
            video_count += 1
            # if video_count == 5:
            #     break
            if video_count <= 200:
                continue
            if video_count == 250:
                break
            time.sleep(1)

            # self.video_url_element.click() # 点击当前视频urlcubans
            self.driver.execute_script("arguments[0].click();",self.video_url_element)
            # 将浏览器驱动转移到当前页面上来
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # 等待视频页面加载完毕
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='xgplayer-dynamic-bg']")))
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
                        print('页面还没到底')

                    #_2b22e342b8c47a455d1f3ef37ea9e7b2-scss _418f31c5788fcd221a966068331a4aa5-scss
                except Exception as e:
                    print('当前视频页面中，往下拖的时候，页面加载评论的时候超时了！出错信息为：',e)
            print('视频页面拖到底了！')
            print('获取当前视频的所有按钮元素')
            try:
                comment_button_elements = self.driver.find_elements(By.XPATH,"//div[@class='c7ee22de401c856152e3646bffd656a3-scss']/div[2]/button")
            except Exception as e:
                print('获取当前视频评论的所有按钮元素时出错，出错信息为：',e)

            print('一共有%d个按钮元素'%len(comment_button_elements))

            # 遍历每一个按钮元素，并进行按键操作,点击‘展开**条回复’
            for comment_button_element in comment_button_elements:
                try:
                    comment_button_element.send_keys(Keys.ENTER)
                    time.sleep(1)
                except Exception as e:
                    print("第344行代码出错了，遍历每一个按钮元素，按下'回车'出错，出错代码为:",e)

            # 此时页面上的所有'展开**条回复'按钮全部点击完毕，之后要开始点击,'展开更多‘按钮
            print('现在开始循环点击"展开更多"按钮"')
            while True:
                # slider_block_element = self.driver.find_element(By.XPATH,"//div[@class='captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 zGYIR']")
                # slider_element = self.driver.find_element(By.XPATH,"//div[@class='secsdk-captcha-drag-icon sc-kEYyzF fiQtnm']")
                # # 如果出现了滑块弹窗
                # if slider_block_element:

                try:
                    count = 0
                    # 获取所有的‘展开更多 ’按钮和‘收起‘按钮元素
                    comment_button_moreinfo_elements = self.driver.find_elements(By.XPATH,"//button[@class='b82d8f7a3085b37109200dce4939beb8-scss']")
                    print("comment_button_moreinfo_elements的长度：",len(comment_button_moreinfo_elements))
                    # 循环遍历所有的‘展开更多’和‘收起’按钮元素
                    for comment_button_moreinfo_element in comment_button_moreinfo_elements:
                        # 判断是“展开更多”按钮，还是“收起”按钮
                        judge_is_moreinfo_button_element = comment_button_moreinfo_element.find_element(By.XPATH,'./span')
                        while '展开' in judge_is_moreinfo_button_element.text:
                        # if '展开' in judge_is_moreinfo_button_element.text:
                        # if judge_is_moreinfo_button_element.text == '展开更多':
                            # 当遍历的元素是’展开更多‘按钮元素时，进行点击
                            comment_button_moreinfo_element.send_keys(Keys.ENTER)
                            count += 1
                            time.sleep(1)
                            print('展开对应的计数count=',count)
                        # 如果’收起‘按钮的个数，等于获取的按钮元素集合的长度，即此时当前页面评论区只有'收起'元素里
                        # if judge_is_moreinfo_button_element.text == '收起':
                        #     count += 1
                    print('统计"剩余展开更多"元素的count=',count)
                    # 如果‘收起’按钮的计数器统计个数等于当前页面评论区按钮元素集合的长度，说明此时已经没有‘展开更多’按钮，只有‘收起’按钮里
                    # if count  >= len(comment_button_moreinfo_elements):
                    #     break
                    if count == 0:
                        break
                except Exception as e:
                    print('循环点击"展开更多"按钮"出错了，说明当前页面中没有"展开更多"按钮了！此时退出循环点击！',e)
                    # break

            print('至此，当前视频页面下的所有评论，展开完全！')
            # 先作测试用，不遍历下一个视频
            #----------至此，可以开始在当前url对应的视频页面中，获取视频标题、视频发布者、视频发布时间，还有关于该视频所有的评论内容、评论者、评论时间----------

            # 获取当前视频下的所有评论区元素块列表集
            comment_block_elements = self.driver.find_elements(By.XPATH,"//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]")
            print('一共获取到了%d个评论区元素块!'%len(comment_block_elements))

            # 遍历所有评论区元素块列表集，即每一个评论区块元素，获取每一个评论区的头评论的评论内容，评论时间

            # # 获取到了头评论的内容和日期元素集合，如何进行11对应？
            # head_comments = self.driver.find_elements(By.XPATH,"//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/p/span/span/span/span/span/span").text
            # head_comment_dates = self.driver.find_elements(By.XPATH,"div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[1]/div[1]/p").text

            # 循环遍历每一个评论块元素，获取当前评论块元素
            for comment_block_element in comment_block_elements:
                try:
                    # 获取评论头的评论内容和评论时间
                    head_comment = comment_block_element.find_element(By.XPATH,"./p/span/span/span/span/span/span").text
                    head_comment_date = comment_block_element.find_element(By.XPATH,"./div[1]/div[1]/p").text
                    if head_comment =='':
                        continue
                    self.list_temp.append(head_comment)
                    self.list_temp.append(head_comment_date)
                    self.list_temp.append('comment')
                    self.list_all_comment.append(self.list_temp)
                    print('评论头的评论内容为：',head_comment)
                    print('评论头的评论日期为：',head_comment_date)
                    print('--------------------------头评论中的数据-----------------------------')

                    self.list_temp = []
                except Exception as e:
                    print('获取评论头的评论内容和评论日期时出错，出错原因：',e)

                #//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]
                #//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]
                # # 获取评论列表的
                # list_comments_elements = comment_block_element.find_elements(By.XPATH,"./div[3]/div/div[2]")

            # 获取当前视频下，所有二级评论的评论块元素
            comment_list_elements = self.driver.find_elements(By.XPATH,"//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]")
            for comment_list_element in comment_list_elements:
                #//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]
                #//div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]/p/span/span/span/span/span/span
                print('当前视频下，当前二级评论的评论块元素为：', comment_list_element)

                try:
                    list_comment = comment_list_element.find_element(By.XPATH,"./p/span/span/span/span/span/span").text
                    print('当前视频下，二级评论的评论内容为：',list_comment)
                except Exception as e:
                    print('获取二级评论的评论内容时出错，出错原因：',e)

                # //div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]/div[@class='_52058b306f496907c5d55c0facb81886-scss']/div/p
                # //div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]
                # //div[@class='d627fef252bbad6ef5448e9c6281dcb9-scss _418f31c5788fcd221a966068331a4aa5-scss']/div[4]/div/div/div[2]/div[3]/div/div[2]/div/div/p
                try:
                    list_comment_date = comment_list_element.find_element(By.XPATH,"./div[@class='_52058b306f496907c5d55c0facb81886-scss']/div/p").text
                    print('当前视频下，二级评论的评论日期为：',list_comment_date)
                except Exception as e:
                    print('获取二级评论的评论日期时出错，出错原因：',e)
                print('--------------------------二级评论中的数据-----------------------------')

                if list_comment == '':
                    continue

                self.list_temp.append(list_comment)
                self.list_temp.append(list_comment_date)
                self.list_temp.append('comment')
                self.list_all_comment.append(self.list_temp)
                self.list_temp = []

            self.driver.close()
            print('这里执行里self.driver.close()方法！')
            handles = self.driver.window_handles
            print('一共有%d个网页'%len(handles))
            self.driver.switch_to.window(handles[1])

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
        with open('data/TikTok_%s_%d.csv'%(self.keyword,n), 'w', encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['comment', 'comment_time', 'source_type'])
            for item_ in list_data_500000:
                writer.writerow(item_)

Tik1 = TikTok('索尼中国')
Tik1.main_steps_loops()