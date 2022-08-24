import requests
import execjs
import hashlib
import base64


user = input('請輸入手機號:')
pwd = input('請輸入密碼:')

pwd = pwd.encode('utf-8') # 生成密碼的字節碼
# 實例化md5加密算法對象
# r.createHash("md5").update(e).digest("base64").slice(0, -2)
md5 = hashlib.md5()
md5.update(pwd)  # pwd 這裡字符串必須是bytes
pwd = md5.digest()
print(type(pwd))
base_s = base64.b64encode(pwd)[:-2]
print(type(base_s))

url = 'https://open.shiguangkey.com/api/udb/login/standard'
data = {
'account': user,
'password': base_s,
'inviteLinkId':'',
'ticketLogin':'1',
'imageCode':'5813',
'uniqueId':'5ffd1caa99ec4437b6cd0f4c3e794495',
}
headers ={
'accept':'application/json',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'content-length':'136',
'content-type':'application/x-www-form-urlencoded',
'cookie':'Hm_lvt_7e8b931a9b138d095673181619178304=1656481689; token=; Hm_lpvt_7e8b931a9b138d095673181619178304=1656484679',
'origin':'https://open.shiguangkey.com',
'referer':'https://open.shiguangkey.com/?version&showClose=true&isRegister&bindPhone=false&wechat=false&token=&autoClose=true&systemId=0&inviteLinkId=&local=',
'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'terminaltype':'4',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
session = requests.session()
res = session.post(url=url,headers=headers,data=data)
print(res.text)


