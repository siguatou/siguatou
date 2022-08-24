import base64
import binascii
import json
import re

import requests
import rsa

username = '13901513299'
password = 'sigua93718'


session = requests.session()
url_prelogin = 'https://login.sina.com.cn/sso/prelogin.php'
url_login = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'

headers =  {
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://weibo.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
params = {
    'entry' :'weibo',
    'callback' :'sinaSSOController.preloginCallBack',
    'su' :'MTM5MDE1MTMyOTk =',
    'rsakt' :'mod',
    'checkpin' :'1',
    'client' :'ssologin.js(v1.4.19)',
    '_' :'1658803696148',
}

resp = session.get(url_prelogin ,headers = headers ,params=params)
# print(resp.text)
json_data = re.findall(r'(?<=\().*(?=\))', resp.text)[0]
# print(json_data)
data = json.loads(json_data)
#
servertime = data['servertime']
nonce = data['nonce']
pubkey = data['pubkey']
rsakv = data['rsakv']
print('servertime:' ,servertime ,'nonce:' ,nonce ,'pubkey:' ,pubkey ,'rsakv:' ,rsakv)

# 1658803714
# servertime = str(time.time())[0:10]
#
# calculate su
# print(urllib.parse.quote(self.username))
su = base64.b64encode(username.encode(encoding="utf-8"))
#
# calculate sp
rsaPublickey = int(pubkey, 16)
key = rsa.PublicKey(rsaPublickey, 65537)
message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
sp = binascii.b2a_hex(rsa.encrypt(message.encode(encoding="utf-8"), key))
postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'qrcode_flag': 'false',
    'useticket': '1',
    'pagerefer': 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F',
    'pcid': 'gz-32d491fa97459667fbdb17604bb2976f3254',
    'door': 'RCFh3',
    'vsnf': '1',
    'su': su,
    'service': 'miniblog',
    'servertime': servertime,
    'nonce': nonce,
    'pwencode': 'rsa2',
    'rsakv': rsakv,
    'sp': sp,
    'sr': '1280*1024',
    'encoding': 'UTF-8',
    'prelt': '579',
    'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META',
}
headers1 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-length': '812',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://weibo.com',
    'referer': 'https://weibo.com/',
    # 'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Linux"',
    # 'sec-fetch-dest': 'iframe',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'cross-site',
    # 'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
resp = session.post(url_login ,headers=headers1 ,data=postdata)
# print resp.headers
print(resp.text)
print('*'*100)

url = 'https://weibo.com/ajax/statuses/mymblog?uid=2928660442&page=1&feature=0'
res = session.get(url=url)
print(res.text)
