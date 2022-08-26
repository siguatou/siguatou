import requests
import time
import random
import urllib
import json
from lxml import etree
import re
import csv

def crawler(keyword):
    # xperia 5 iii
    global page_size, headers
    proxies = {
        'http':'http://125.106.138.9:4226',
        'https':'https://221.203.6.14:9713'
    }
    headers = {
        # 'accept':'application/json, text/plain, */*',
        # 'accept-encoding':'gzip, deflate, br',
        # 'accept-language':'en-US,en;q=0.9',
        'cookie':'_uuid=26422339-877F-B27E-4333-4595AB43F5BF91999infoc; buvid_fp=404d1f55f56e263e33a8f70751827f16; buvid3=7386ED15-3C8B-5483-8805-187EF5DEAB4793341infoc; b_nut=1661137592; buvid4=D228C0EE-1E0C-A861-89AD-CB701069960C93341-022082211-SV1aRNo/hDR9d1U0GFAy/A%3D%3D; innersign=0; i-wanna-go-back=-1; b_ut=7; b_lsid=2C5A69C3_182C391CAA1; bsource=search_baidu; nostalgia_conf=-1; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_7386ED15%22%3A%22182C391CE51%22%2C%22333.337.fp.risk_7386ED15%22%3A%22182C391E678%22%7D%7D; CURRENT_BLACKGAP=0; CURRENT_FNVAL=80; sid=5tg9l6i3; PVID=3',
        'origin':'https://search.bilibili.com',
        'referer':'https://search.bilibili.com/video?keyword=Xperia+1+IV&from_source=webtop_search&spm_id_from=333.1007',
        # 'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        # 'sec-ch-ua-mobile':'?0',
        # 'sec-ch-ua-platform':'"Linux"',
        # 'sec-fetch-dest':'empty',
        # 'sec-fetch-mode':'cors',
        # 'sec-fetch-site':'same-site',
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    keyword_parse = urllib.parse.quote(keyword)
    url_pg1 = 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=1&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={}&category_id=&search_type=video&dynamic_offset=0&preload=true&com2co=true'.format(keyword_parse)
    res_pg1 = requests.get(url=url_pg1,headers=headers)
    res_pg1_dict = json.loads(res_pg1.text)
    # page_size = int(res_pg1_dict['data']['pagesize'])
    numResults = int(res_pg1_dict['data']['numResults'])
    # numPages = int(res_pg1_dict['data']['numPages'])
    numPages = 30
    page_size = numResults // numPages
    if numResults % numPages != 0:
        page_size += 1

    #------------------ 至此，当前关键字下的所有视频页数获取成功

    for page_num in range(1,page_size+1):
        # if page_num<=6:
        #     continue
        url_pg= 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page={}&page_size={}&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={}&category_id=&search_type=video&dynamic_offset={}&preload=true&com2co=true'.format(page_num,page_size,keyword_parse,30*(page_num-1))
        #        https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=12&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=xperia%205%20iii&category_id=&search_type=video&dynamic_offset=264&preload=true&com2co=true
        print('页数为:',page_num)
        print('url为:',url_pg)
        res_pg = requests.get(url=url_pg, headers=headers)
        # print('当前视频页面response内容:',res_pg.text)
        time.sleep(random.randint(1,3))

        # 获取到当前页的所有视频的数据信息
        res_videoes_dict = json.loads(res_pg.text)
        try:
            videoes_result_list = res_videoes_dict['data']['result']
            # print(videoes_result_list)
        except Exception as e:
            print('获取到当前页的所有视频的数据信息出错，出错信息为:',e)
            continue

        # 开始遍历当前页的所有视频数据
        # 遍历当前页的每一个当前视频的信息
        for video_info in videoes_result_list:
            # 获取到当前视频的url
            video_url = video_info['arcurl']
            oid = video_info['id'] # 每一个视频的id标识
            # 对当前视频url发起requests请求，获取到视频标题和视频发布时间
            res = requests.get(url=video_url)
            video_html = etree.HTML(res.text)
            video_title = video_html.xpath("//div[@class='left-container']/div[@id='viewbox_report']/h1")[0].get('title')
            model_regex = re.compile(r'.*{}.*'.format(keyword), re.I)
            if model_regex.findall(video_title) == []:
                continue
            video_time = video_html.xpath("//span[@class='pudate-text']/text()")[0].strip()
            print([video_title,video_time,oid])
            # 至此，获取到了当前视频的视频标题和视频发表时间
# --------------------------
            # 获取当前视频下，第一个main_reply的response数据
            first_main_cmt_url = "https://api.bilibili.com/x/v2/reply/main?mode=3&next=0&oid={}&plat=1&type=1".format(oid)
                                # https://api.bilibili.com/x/v2/reply/main?mode=3&next=0&oid=755169978&plat=1&type=1
            res_first_main_cmt = requests.get(first_main_cmt_url).text
            res_first_main_cmt_dict = json.loads(res_first_main_cmt)
            time.sleep(random.randint(1, 3))
            # print(res_first_main_cmt_dict)
            # 372994550
            # 获取第一个main_reply的评论数据列表
            try:
                first_main_cmt_list = res_first_main_cmt_dict['data']['replies']
                if first_main_cmt_list == None:
                    continue
            except Exception as e:
                print('获取第一个main_reply的评论数据列表出错，出错信息为:',e)
                continue

            # 遍历第一个main_reply的评论数据列表
            for first_main_cmt_dict in first_main_cmt_list:
                first_main_cmt = first_main_cmt_dict['content']['message']
                # 通过时间辍得到标准时间格式的时间
                first_main_cmt_time = int(first_main_cmt_dict['ctime'])
                first_main_cmt_time = time.localtime(first_main_cmt_time)
                first_main_cmt_time = time.strftime("%Y-%m-%d %H:%M:%S", first_main_cmt_time)
                print([first_main_cmt,first_main_cmt_time,video_title,video_time])
                yield [first_main_cmt,first_main_cmt_time,video_title,video_time]

                # 获取second_reply需要的rpid
                rpid = first_main_cmt_dict['rpid_str']
                # 对第一个second_reply发起requests请求
                first_reply_cmt_url = 'https://api.bilibili.com/x/v2/reply/reply?oid={}&pn=1&ps=10&root={}&type=1'.format(oid,rpid)
                res_first_reply_cmt = requests.get(url=first_reply_cmt_url).text
                # 得到第一个second_reply的响应数据
                res_first_reply_cmt_dict = json.loads(res_first_reply_cmt)
                time.sleep(random.randint(1, 3))
                # 获取第一个second_reply的评论总个数、评论大小，从而计算出评论页数
                replies_count = res_first_reply_cmt_dict['data']['page']['count']
                replies_size = res_first_reply_cmt_dict['data']['page']['size']
                replies_page_count = replies_count // replies_size
                if replies_count % replies_size != 0:
                    replies_page_count += 1
                # 遍历第个second_reply的所有翻页的url
                for replies_page in range(1,replies_page_count+1):
                    first_reply_cmt_url = 'https://api.bilibili.com/x/v2/reply/reply?oid={}&pn={}&ps=10&root={}&type=1'.format(oid,replies_page,rpid)
                    # res_first_reply_cmt = requests.get(url=first_reply_cmt_url,headers=headers,proxies=proxies).text
                    res_first_reply_cmt = requests.get(url=first_reply_cmt_url).text
                    # 得到第一个second_reply的响应数据
                    res_first_reply_cmt_dict = json.loads(res_first_reply_cmt)
                    # 得到当前翻页下的评论数据列表replies
                    first_relies_list = res_first_reply_cmt_dict['data']['replies']
                    time.sleep(random.randint(1,3))
                    # 开始遍历得到的评论数据列表
                    for first_replies_dict in first_relies_list:
                        replies_cmt = first_replies_dict['content']['message']
                        replies_time = int(first_replies_dict['ctime'])
                        replies_time = time.localtime(replies_time)
                        replies_time = time.strftime("%Y-%m-%d %H:%M:%S", replies_time)
                        print([replies_cmt, replies_time, video_title, video_time])
                        yield [replies_cmt, replies_time, video_title, video_time]

            page_next = 2
            # 循环对第二个和之后的main_reply发起请求
            while True:
                url_main_reply_after = 'https://api.bilibili.com/x/v2/reply/main?mode=3&next={}&oid={}&plat=1&type=1'.format(page_next,oid)
                res_main_after = requests.get(url=url_main_reply_after).text
                res_main_after_dict = json.loads(res_main_after)
                page_next += 1
                is_end = res_main_after_dict['data']['cursor']['is_end']
                # 先判断是否请求到了最后一个main_reply，如果到了最后一个,则跳出循环
                if is_end == True:
                    break

                # 获取当前next下的main_reply的所有replies
                main_after_list = res_main_after_dict['data']['replies']
                # 遍历第一个main_reply的评论数据列表
                for after_main_cmt_dict in main_after_list:
                    after_main_cmt = after_main_cmt_dict['content']['message']
                    # 通过时间辍得到标准时间格式的时间
                    after_main_cmt_time = int(after_main_cmt_dict['ctime'])
                    after_main_cmt_time = time.localtime(after_main_cmt_time)
                    after_main_cmt_time = time.strftime("%Y-%m-%d %H:%M:%S", after_main_cmt_time)
                    print([after_main_cmt, after_main_cmt_time, video_title, video_time])
                    yield [after_main_cmt,after_main_cmt_time,video_title,video_time]

                    # 获取second_reply需要的rpid
                    rpid = after_main_cmt_dict['rpid_str']
                    # 对第一个second_reply发起requests请求
                    after_reply_cmt_url = 'https://api.bilibili.com/x/v2/reply/reply?oid={}&pn=1&ps=10&root={}&type=1'.format(
                        oid, rpid)
                    # res_after_reply_cmt = requests.get(url=after_reply_cmt_url,headers=headers,proxies=proxies).text
                    res_after_reply_cmt = requests.get(url=after_reply_cmt_url).text
                    # 得到第一个second_reply的响应数据
                    res_after_reply_cmt_dict = json.loads(res_after_reply_cmt)
                    time.sleep(random.randint(1, 3))
                    # 获取second_reply的评论总个数、评论大小，从而计算出评论页数
                    try:
                        replies_count = res_after_reply_cmt_dict['data']['page']['count']
                    except Exception as e:
                        print('在获取第一个之后的second_reply的评论总个数、评论大小，从而计算出评论页数时出错，出错信息为:',e)
                        continue
                    replies_size = res_after_reply_cmt_dict['data']['page']['size']
                    replies_page_count = replies_count // replies_size
                    if replies_count % replies_size != 0:
                        replies_page_count += 1
                    # 遍历第个second_reply的所有翻页的url
                    for replies_page in range(1, replies_page_count + 1):
                        first_reply_cmt_url = 'https://api.bilibili.com/x/v2/reply/reply?oid={}&pn={}&ps=10&root={}&type=1'.format(
                            oid, replies_page, rpid)
                        res_first_reply_cmt = requests.get(url=first_reply_cmt_url).text
                        # res_first_reply_cmt = requests.get(url=first_reply_cmt_url,headers=headers,proxies=proxies).text
                        # 得到第一个second_reply的响应数据
                        res_first_reply_cmt_dict = json.loads(res_first_reply_cmt)
                        # 得到当前翻页下的评论数据列表replies
                        first_relies_list = res_first_reply_cmt_dict['data']['replies']
                        time.sleep(random.randint(1, 3))
                        # 开始遍历得到的评论数据列表
                        for first_replies_dict in first_relies_list:
                            replies_cmt = first_replies_dict['content']['message']
                            replies_time = int(first_replies_dict['ctime'])
                            replies_time = time.localtime(replies_time)
                            replies_time = time.strftime("%Y-%m-%d %H:%M:%S", replies_time)
                            print([replies_cmt, replies_time, video_title, video_time])
                            yield [replies_cmt, replies_time, video_title, video_time]

            #root = 98109791232
        print('='*70)

if __name__ == '__main__':
    # xperia 5 iii xperia 1 iii xperia 1 IV
    keyword = input('请输入你的关键字:')
    # keyword = "xperia 5 iii"
    with open('data/{}.csv'.format(keyword),'w',encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cmt','cmt_time','video_title','video_time'])
        for item in crawler(keyword):
            writer.writerow(item)
