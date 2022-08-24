import requests

url = 'https://weibo.com/ajax/statuses/mymblog'

params = {
    'uid':'2928660442',
    'page':'1',
    'feature':'0'
}
headers = {
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.9',
    'client-version':'2.34.74',
    'cookie':'SINAGLOBAL=9471380264253.81.1656472017890; UOR=,,login.sina.com.cn; _s_tentry=login.sina.com.cn; Apache=4633245049073.32.1659319796433; ULV=1659319796464:7:1:1:4633245049073.32.1659319796433:1658883960377; XSRF-TOKEN=3X0WgjIIO1c4XZIYHwLhauTR; SCF=Ak4SrzpffHhwK3ME58sR9LKcENQ8EYAre2ELWgco4CnXimqxjb9otTEyGG1c8gAyfDzo9P-H98VwSbLl95hWXhM.; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWqgvVUwh09uuICfXdsH6Rz5JpVF0201K5pSK20eo.4; SUB=_2AkMVu-zidcPxrAZZkfgVzG_raYlH-jymboUUAn7uJhMyAxh87nQCqSVutBF-XELsdeB1zqXq2XMq4fpcPCQZ4V1D; login_sid_t=33cf558aa58e5eaf7927d764ed16b9d0; cross_origin_proto=SSL; wb_view_log=1280*10241; WBPSESS=Dt2hbAUaXfkVprjyrAZT_F8TjtW1Mnh-ovDHVItKM0da7QMB6c3SnWN9fIwkyPVsqFMIX-IOVSnI6hxbe3i6JW9C4lbRrAIfCFl0ZSQlMEtk7JHxe1-DmF4rukXFp-uCtthXk7oYvNqB7j8dV8En8w==',
    'referer':'https://weibo.com/u/2928660442',
    'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'server-version':'v2022.07.27.1',
    'traceparent':'00-5b543571ec5ee70b581ef22a1822663b-c2168dea1e1b7a69-00',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
    'x-xsrf-token':'3X0WgjIIO1c4XZIYHwLhauTR'
}

res = requests.get(url=url,headers=headers,params=params)
print(res.text)