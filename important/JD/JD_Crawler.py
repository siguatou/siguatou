import requests
import re
import json
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
import random
import time

url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100021200777&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0&fold=1'
ua = UserAgent()
headers =  {
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'cookie':'__jdv=76161171|www.google.com.hk|-|referral|-|1656034839531; areaId=12; __jdu=16560348395311426748879; PCSYCityID=US_0_0_0; shshshfpa=b610dfad-546d-68db-7af0-72a7c2c895c4-1656034847; shshshfpb=aLW8YqsBWtVo35LYm9XhCdw; unpl=JF8EAKpnNSttWx4GUEkBSRcWHA9UWwkOGR9RPDQCXV5aHFECSVAaQBd7XlVdXhRKEB9tZhRVVVNPUQ4eASsSEXtdZFtYCk8fC19mBAtYWkhTVxgHSRdCTA5TX1lfTCcAb1cEZF1fT1MEGQcSEBhPX1ReWAtMEQZmbgNcbWhLXAErMisVFUxYUV9cC3sWM25XTjpcFUtTARwDGRcZSVVQXF0IThQEaWIMXVtQe1U1GA; shshshfp=dd8574b05e60213802e594814007144f; __jda=122270672.16560348395311426748879.1656034840.1656034840.1656554085.2; __jdc=122270672; token=fdf635cb2662271eba20b92a5bf0c1b3,2,920308; __tk=jzk4ic5akxPHZjpbSlVtZD5uAjCmlybcSkkIVl5Sn133lypUkz34ZDzkAj33lzR6kyCdY05n,2,920308; ip_cityCode=984; ipLoc-djd=12-984-3383-0; jwotest_product=99; __jdb=122270672.5.16560348395311426748879|2.1656554085; shshshsID=6ba32624dd61c95a242a00ec35e9c5ac_5_1656554954446; 3AB9D23F7A4B3C9B=MJYUDSECQF6GE3J5EJ6IAPLSCGCAZ73MEDNSHTGBALVSC3VIZ6AH3JRYT6C3QLBPO25AS4FA3UHMDCBSV6KYM5TLC4; JSESSIONID=428714AD749780CB04FFFA4F7DDDF057.s1',
'referer':'https://item.jd.com/',
'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'sec-fetch-dest':'script',
'sec-fetch-mode':'no-cors',
'sec-fetch-site':'same-site',
'user-agent':ua.chrome
}

res = requests.get(url=url,headers=headers)

res_text = res.text

dict_result = re.findall('fetchJSON_comment98\((.*?)\)',res_text)[0]
dict_result = json.loads(dict_result)
max_page = int(dict_result['maxPage'])
comment_count = 0
def start_requests(page_num):
    global ua, dict_result
    global comment_count
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100021200777&score=0&sortType=6&page={}&pageSize=10&isShadowSku=0&fold=1'.format(page_num)
    ua = UserAgent()
    res = requests.get(url=url, headers=headers)
    time.sleep(random.randint(1,4))
    res_text = res.text
    try:
        dict_result = re.findall('fetchJSON_comment98\((.*?)\)', res_text)[0]
        dict_result = json.loads(dict_result)
        comments_list = dict_result['comments']
        for comment in comments_list:
            comment_content = comment['content']
            print(comment_content)
            comment_count += 1
    except Exception as e:
        print('获取评论失败')
        print('请求返回的内容为:',res_text)

    print('第{}页爬完了！'.format(page_num))

# threadPool = ThreadPoolExecutor(max_workers=5)
# for page_num in range(max_page):
#     threadPool.submit(start_requests,page_num)
for page_num in range(max_page):
    start_requests(page_num)

print('总共有:',comment_count,'条评论')