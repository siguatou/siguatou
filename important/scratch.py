import requests
import json

url = 'https://weibo.com/ajax/statuses/mymblog?uid=2928660442&page=1&feature=0'
headers = {
'accept':'application/json, text/plain, */*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'client-version':'2.34.74',
'cookie':'SINAGLOBAL=9471380264253.81.1656472017890; UOR=,,login.sina.com.cn; _s_tentry=login.sina.com.cn; Apache=7471260230476.229.1658883960374; ULV=1658883960377:6:5:4:7471260230476.229.1658883960374:1658799972221; XSRF-TOKEN=P5en9RcVMly6TQU_PDNt8hDD; SCF=Ak4SrzpffHhwK3ME58sR9LKcENQ8EYAre2ELWgco4CnXd1crYvy3ktCrZwd3HnbHcDrJLEt0W3vfDHl4uFwZbZg.; SUB=_2A25P5_gwDeRhGeNG4lIR8CrFzjiIHXVslW74rDV8PUNbmtANLRPukW9NSxAq7BXqC7hFipV53dmQv0_whWZBICO2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqgvVUwh09uuICfXdsH6Rz5JpX5KzhUgL.Fo-R1K57ehB4SKB2dJLoIEBLxK-L12zLBKBLxK-LBK-L12zLxKML1-2L1hBLxKML1KeL1-et; ALF=1690614749; SSOLoginState=1659078752; WBPSESS=Dt2hbAUaXfkVprjyrAZT_F8TjtW1Mnh-ovDHVItKM0dHkP2Wqod3maPL6ERpEK9C8ogWX794RntjIO3eeI6p0_ys3FEtqrMeH_a0rPhgevPJJJevO_9EtVzWtIwAjdraqZ6vjKitEEcvYPU4vSdY_waBVGpbVG1j1nZdqV3_9KbztXwuxndYNLtvIxF1dcANMw9LNiqwHhaZgfA_jdZWSA==',
'referer':'https://weibo.com/u/2928660442',
'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'server-version':'v2022.07.27.1',
'traceparent':'00-aea0e7edfca3f0c9de7a4ac308d271b1-c891a6fa34188902-00',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'x-xsrf-token':'P5en9RcVMly6TQU_PDNt8hDD',
}

res = requests.get(url=url,headers=headers)
print(res.text)