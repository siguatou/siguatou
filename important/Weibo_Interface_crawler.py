import requests
import time
import random
import urllib
import re
import json
from lxml import etree
import csv


def crawler(keyword):

    keyword_parse = urllib.parse.quote(keyword)
    url_user = 'https://s.weibo.com/weibo?q={}'.format(keyword_parse)
    headers_user = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'SINAGLOBAL=1578118557271.9414.1661141890567; ULV=1661146981410:2:2:2:5635421923182.709.1661146981399:1661141890572; PC_TOKEN=b13111c738; SCF=AqJZOQWI6SbzJ1WYuN7thA2B6DJyBQtfQf1xQS16P3Q_CUp_lYRRgebciPe18INIyhMieGWI9VkEq9ynkf3defk.; XSRF-TOKEN=201Nbnf7Fyu2Uryk39Om-kV0; SUB=_2A25ODFbNDeRhGeNG4lIR8CrFzjiIHXVteM8FrDV8PUNbmtAfLXHekW9NSxAq7JykWctshyVdGGr8tbsy_o8Sw03D; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqgvVUwh09uuICfXdsH6Rz5JpX5KzhUgL.Fo-R1K57ehB4SKB2dJLoIEBLxK-L12zLBKBLxK-LBK-L12zLxKML1-2L1hBLxKML1KeL1-et; ALF=1693014556; SSOLoginState=1661478557; WBPSESS=Dt2hbAUaXfkVprjyrAZT_F8TjtW1Mnh-ovDHVItKM0dHkP2Wqod3maPL6ERpEK9C0tx36h2UUkDpQpS1edPqIHeiNdBMd4pp9rontb4s03h6QXUjPkBxHk-xxn2xdbqEgvQUpb9pYenfllSxuTl4hRhPapK6UQkAHCku5b9Awzo=',
        'referer': 'https://weibo.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    res = requests.get(url=url_user, headers=headers_user)
    res_text = res.text
    print(res_text)
    user_id = re.findall("\$CONFIG\['uid'\] = '(.*?)';", res_text)[0]
    # ---------------------至此，user_id获取完毕

    # 获取当前关键字下一共有多少页数据
    # <a href="/weibo?q=Xperia%201%20IV&page=
    page_num = len(re.findall('<a href="/weibo\?q=.*&page=.*">第.*页</a></li>', res_text))
    print('总页数为:', page_num)
    #  -------------------至此，当前关键字下总页数获取完毕

    # 获取当前关键字下所有页的所有的版主的uid
    # https://s.weibo.com/weibo?q=Xperia%201%20IV&page=2
    for pg_num in range(1, page_num + 1):
        url_pages = 'https://s.weibo.com/weibo?q={}&page={}'.format(keyword_parse, pg_num)
        res = requests.get(url=url_pages, headers=headers_user)
        res_text = res.text
        uid_list = re.findall('&touid=(.*?)&from', res_text)
        print('一共有uid:',len(uid_list)) # 显示当前页面一共有多少个版主uid
        time.sleep(random.randint(1, 3))
        # 获取当前关键字下所有页的所有版主的uid成功

        # 获取当前页面所有版主的up_title和up_time
        HTML = etree.HTML(res_text)
        up_block_elements = HTML.xpath("//div[@class='card-wrap']/div[@class='card']/div/div[2]")
        up_mid_list = HTML.xpath("//div[@action-type='feed_list_item']")
        for up_mid_elem in up_mid_list:
            if up_mid_elem.get('mid') == None:
                up_mid_list.remove(up_mid_elem)
        print('一共有up_block:',len(up_block_elements)) # 显示当前页面一共有多少个版主uid
        print('一共有up_mid:',len(up_mid_list)) # 显示当前页面一共有多少个版主uid


        # 接下来获取每一页，每一个版主对应的所有评论数据
        # 获取当前页的，当前版主uid下的所有评论数据
        uid_and_up_bloc_list = zip(uid_list,up_block_elements,up_mid_list)
        for blend_item in uid_and_up_bloc_list:
            # blend_item中是当前页中当前版主对应的uid和网页元素数据对象
            # print(blend_item) # ('2213561393', <Element div at 0x7f141afefd88>)
            uid = blend_item[0]
            up_block_element = blend_item[1]
            up_mid = blend_item[2].get('mid')

            up_title = up_block_element.xpath('./p//text()')
            up_title = ''.join(up_title).strip()

            Xperia_5_iii_regex = re.compile(r'.*{}.*'.format(keyword), re.I)
            if  Xperia_5_iii_regex.findall(up_title) == []:
                continue

            up_time = up_block_element.xpath("./div[@class='from']/a/text()")[0]
            up_time = ''.join(up_time).strip()

            print('up_title:',up_title)
            print('up_time:',up_time)
            # 4800947844552311
            url_comment_first = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id={}&is_show_bulletin=2&is_mix=0&count=10&uid={}'.format(up_mid,uid)
            res = requests.get(url=url_comment_first, headers=headers_user)
            res_text = res.text
            print(res_text)
            try:
                res_dict = json.loads(res_text)
            except Exception as e:
                print('buildcomment_first网络请求出错，出错信息为:',e)
                continue
            # 获取当前版主uid下的第一个buildcomment中的评论数据列表
            cmt_datalist = res_dict['data']
            # 开始遍历第一个buildcomment中的评论数据列表
            for cmt_data in cmt_datalist:
                cmt_main = cmt_data['text_raw']
                cmt_time = cmt_data['created_at']
                yield [cmt_main,cmt_time,up_title,up_time]
                print([cmt_main,cmt_time,up_title,up_time])
                # 主评论获取完毕

                if cmt_data['comments'] != []:
                    for cmt_reply_data in cmt_data['comments']:
                        cmt_reply = cmt_reply_data['text_raw']
                        cmt_reply_time = cmt_reply_data['created_at']
                        yield [cmt_reply, cmt_reply_time, up_title, up_time]
                        print([cmt_reply, cmt_reply_time, up_title, up_time])

            # 获取max_id,准备循环进行first_buildcomment之后的build_comment(after)的评论数据获取
            max_id = res_dict['max_id']
            trendsText = ''
            while max_id != 0 and trendsText !='已加载全部评论':
                url_buildcmt_after = 'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={}&is_show_bulletin=2&is_mix=0&max_id={}&count=20&uid={}'.format(up_mid,max_id,uid)
                res = requests.get(url=url_buildcmt_after,headers=headers_user)
                res_txt = res.text
                print(res_txt)
                try:
                    res_dict = json.loads(res_txt)
                except Exception as e:
                    print('build_comment_after评论数据网络请求出错了！出错信息为:',e)
                    break

                cmt_datalist = res_dict['data']
                # 开始遍历buildcomment_after中的评论数据列表
                for cmt_data in cmt_datalist:
                    cmt_main_after = cmt_data['text_raw']
                    cmt_time_after = cmt_data['created_at']
                    yield [cmt_main_after,cmt_time_after,up_title,up_time]
                    print([cmt_main_after, cmt_time_after, up_title, up_time])
                    # 主评论获取完毕

                    if cmt_data['comments'] != []:
                        for cmt_reply_data in cmt_data['comments']:
                            cmt_reply_after = cmt_reply_data['text_raw']
                            cmt_reply_time_after = cmt_reply_data['created_at']
                            yield [cmt_reply_after, cmt_reply_time_after, up_title, up_time]
                            print([cmt_reply_after, cmt_reply_time_after, up_title, up_time])

                # 获取max_id,准备循环进行first_buildcomment之后的build_comment(after)的评论数据获取
                max_id = res_dict['max_id']
                trendsText = res_dict['trendsText']

            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    # xperia 5 iii  xperia 1 iii xperia 1 IV
    keyword = input('请输入搜索关键字:')
    with open('data/{}.csv'.format(keyword), 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cmt','cmt_time','up_title','up_time'])
        for item in crawler(keyword):
            writer.writerow(item)


