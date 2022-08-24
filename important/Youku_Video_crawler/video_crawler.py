import requests
import zipfile

url = 'https://pl-ali.youku.com/playlist/m3u8'
headers = {
    # 'accept':'*/*',
    # 'accept-encoding':'gzip, deflate, br',
    # 'accept-language':'en-US,en;q=0.9',
    # 'origin':'https://v.youku.com',
    # 'referer':'https://v.youku.com/v_show/id_XNTE3OTI5ODA5Mg==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dselectbutton_47&showid=ccdaa0c00a7f42d8a6a2',
    # 'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    # 'sec-ch-ua-mobile':'?0',
    # 'sec-ch-ua-platform':'"Linux"',
    # 'sec-fetch-dest':'empty',
    # 'sec-fetch-mode':'cors',
    # 'sec-fetch-site':'same-site',
    'cookie': '_m_h5_tk=7568aa7cb9b3288e6c547466a2139b2d_1660621911823; _m_h5_tk_enc=3e4f04d9aff0c3517a6de860287df2c7; cna=X7Y2G/GyKFACAd3jaGaxNnzE; __ysuid=1660617772277jKT; __ayft=1660617772278; __aysid=1660617772278A9I; __ayscnt=1; modalFrequency={"UUID":"10"}; xlly_s=1; youku_history_word=%5B%22%25E5%25A4%25A7%25E5%2586%25B3%25E6%2588%2598%22%5D; P_ck_ctl=6742C88E585A4C0610C07A015B434144; P_sck=VsHfhOYbnoWeXU2vf7Ijwf%2FZVJwik5NdOqr%2BMKvDjYTMWx7lQt38Kb0LeAeHd6FpWhjObh35lp%2BpSWp4M0HIXwP8uG8rexFlvme1sNJp3W0rJ06l9sGSHaA60ae%2FmzF7pcO8ynyRp5D4iVXBUGM22BcFxIwcFFrz0kugNvHzVEc%3D; P_gck=NA%7CZFfctmLGbS01R59myiHdaA%3D%3D%7CNA%7C1660617826978; P_pck_rm=nuggurV4d05d6b2eb8f4cbZBFhfT94lkMd3wwkrc1X%2F2NQnd07S1vLjbCnjXAIal9KR6ay0pUVpEL4%2FBMXrRyWiqvEutGsf33Gpm1dqpKCtkE6y7ZZojrrhgw141iIG1CRAkJwAGdzJRsg5wWHw6pCYUJ0lqVPsnbq3vo6hrZw048lBowifBQ3aG9Ms%3D%5FV2; disrd=52055; __arycid=dd-3-00; __arcms=dd-3-00; P_F=1; __arpvid=16606200449714O2ihj-1660620044994; __aypstp=12; __ayspstp=12; redMarkRead=1; __ayvstp=43; __aysvstp=43; tfstk=cx6FBwG_gjHsIL1V_d9zVtYNjsVGaTWlKA-JtrGgfNl8i0Seus2syh0mOh-xb4Ah.; l=eBP_a0v7Lq98M9QkBO5Zourza77t3Idb8sPzaNbMiInca6sCrFwH9NCHSUR6idtj_tCfNeKzeEszZdEJPQ45jyEtiTwGE3vtnxvO.; isg=BIqKW-uT3D49K1CSQB-X8vBC23ksew7VKVoXTRTCoF1oxyuB_Q9F5fF10zsbN4Zt',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
params = {
    'vid':'XNTE3OTI5ODA5Mg==',
    'type':'cmaf4hd2',
    'ups_client_netip':'79eb9399',
    'utid':'X7Y2G/GyKFACAd3jaGaxNnzE',
    'ccode':'0502',
    'psid':'7d9ea626e63283fc6b2310c61b2cf13941346',
    'ups_userid':'1753752055',
    'ups_ytid':'1753752055',
    'app_ver':'4.1.4',
    'duration':'2725',
    'expire':'18000',
    'drm_type':'19',
    'drm_device':'7',
    'drm_default':'16',
    'sm':'1',
    'nt':'1',
    'oss_file':'05007D000062A90A208BB78000000009E880E8-BE61-4AB4-AF85-7546530BC0E4',
    'media_type':'standard,subtitle',
    'dyt':'0',
    'ups_ts':'1660618517',
    'onOff':'16',
    'encr':'0',
    'ups_key':'0e82add3306d3b74a82653e7c8ae4f4f',
    'ckt':'5',
}
# res = requests.get(url=url,headers=headers,params=params)

# url1 = 'http://valipl10.cp31.ott.cibntv.net/6975AAC84F64271C982A54024/05007D000062A90A208BB78000000009E880E8-BE61-4AB4-AF85-7546530BC0E4_video.m3u8?ccode=0502&duration=2725&expire=18000&psid=7d9ea626e63283fc6b2310c61b2cf13941346&ups_client_netip=79eb9399&ups_ts=1660618517&ups_userid=1753752055&apscid=&mnid=&umt=1&type=cmaf4hd2&utid=X7Y2G%2FGyKFACAd3jaGaxNnzE&vid=XNTE3OTI5ODA5Mg%3D%3D&s=ccdaa0c00a7f42d8a6a2&iv=1&t=3b1140f811cb186&cug=2&bc=2&si=583&eo=1&ckt=5&vkey=Be19b2b5473d5a77199ab13acf4f49e38&fms=e0d1b29a11b92378&tr=2725&le=2263735605276b6b07e601dbf091094c'
# res = requests.get(url=url1,headers=headers)
# print(res.text)

url2 = 'http://valipl10.cp31.ott.cibntv.net/67756D6080932713CFC02204E/05007D000062A90A208BB78000000009E880E8-BE61-4AB4-AF85-7546530BC0E4_video_00001.mp4?ccode=0502&duration=2725&expire=18000&psid=7d9ea626e63283fc6b2310c61b2cf13941346&ups_client_netip=79eb9399&ups_ts=1660618517&ups_userid=1753752055&apscid=&mnid=&umt=1&type=cmaf4hd2&utid=X7Y2G%2FGyKFACAd3jaGaxNnzE&vid=XNTE3OTI5ODA5Mg%3D%3D&s=ccdaa0c00a7f42d8a6a2&iv=1&t=3b1140f811cb186&cug=2&bc=2&si=583&eo=1&ckt=5&fms=e0d1b29a11b92378&tr=2725&le=2263735605276b6b07e601dbf091094c&vkey=B74b967c90c812ba88469e2944dd69dbf'
# url2 = 'http://valipl10.cp31.ott.cibntv.net/67756D6080932713CFC02204E/05007D000062A90A208BB78000000009E880E8-BE61-4AB4-AF85-7546530BC0E4_video_00001.mp4'
res = requests.get(url=url2,headers=headers)
print(res)
print(res.content)
with open('1.mp4','wb') as f:
    f.write(res.content)
    
