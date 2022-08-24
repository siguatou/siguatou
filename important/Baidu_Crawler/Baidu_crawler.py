import requests
import re

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'BIDUPSID=CDD61DA64829C990DE1711436F787880; PSTM=1658223624; BD_UPN=123353; BAIDUID=0BE98239668D92624B968E09BFF949E7:FG=1; BDUSS=5xQlhEemJZT3RYYWdya3lKZVJzaVZOdk1XU2RVcWJvZ0haLXFvUDEwNjctd3BqRVFBQUFBJCQAAAAAAAAAAAEAAAA-x56Px9q33LXEuc%7ENtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALtu42K7buNicE; BDUSS_BFESS=5xQlhEemJZT3RYYWdya3lKZVJzaVZOdk1XU2RVcWJvZ0haLXFvUDEwNjctd3BqRVFBQUFBJCQAAAAAAAAAAAEAAAA-x56Px9q33LXEuc%7ENtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALtu42K7buNicE; newlogin=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=5; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; BA_HECTOR=2k2gag042gala1a08h05ijmc1hf1cs817; ZFY=bUkb8OJKbVlSymH4pyBiGqdOLHcd2HHVIV2jr0SOcHo:C; H_PS_PSSID=36553_36748_36642_36721_37112_36413_36954_36947_36165_36918_36885_37126_36745_26350_36862; sugstore=0; H_PS_645EC=4b16GVE4AbuZaaynkFkE3C6aUdxpBb8MyxjsPv5vPWbbXgAdCe34D8SXd10hd0moUUE8; COOKIE_SESSION=514_0_9_9_4_26_0_2_9_8_1_2_381_0_0_0_1659938029_0_1659943292%7C9%230_1_1659433411%7C1; BDSVRTM=312; ispeed_lsm=10',
    'Host':'www.baidu.com',
    'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

data = {
    'ie':'utf-8',
    'f':'8',
    'rsv_bp':'1',
    'rsv_idx':'2',
    'tn':'baiduhome_pg',
    'wd':'爬虫 js逆向',
    'oq':'%E7%88%AC%E8%99%AB%20js%E9%80%86%E5%90%91',
    'rsv_pq':'ea1d38430003c090',
    'rsv_t':'6d77W3acqz0TZJwPUg+9lh5iiRaFWeopScudgzzN/pPKZ5nfFUBhhox/T+lgHmSueJe1',
    'rqlang':'cn',
    'rsv_enter':'1',
    'rsv_dl':'tb',
    'rsv_btype':'t',
    'inputT':'5',
    'rsv_sug3':'2',
    'rsv_sug1':'2',
    'rsv_sug7':'100',
    'rsv_sug2':'0',
    'rsv_sug4':'611'
}
# f2d429b80004daee
# e5c0d21c00051eba
# rsv_t = bds.comm.encTn
# rsv_pq = bds.comm.qid
url = 'https://www.baidu.com/s'
res = requests.get(url=url,headers=headers,params=data)
# print(res.text)

rsv_pq = re.findall('bds.comm.qid = "(.*?)";',res.text)[0]
rsv_t = re.findall("bds.comm.encTn = '(.*?)';",res.text)[0]
print('rsv_pq:',rsv_pq,'rsv_t:',rsv_t)





