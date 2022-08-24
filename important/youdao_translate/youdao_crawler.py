''''''
'''
i: 世界
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
                                           salt: 16559713412192
                                           sign: 439e989460d739d2e456aa4a7a2d7098
                                           lts: 1655971341219
bv: 5e787eef863a63d9379c54808ae61d46
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME


i: 自由
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
                                           salt: 16559713752125
                                           sign: 7f7e77e353c036d029bd43105b08ee92
                                           lts: 1655971375212
bv: 5e787eef863a63d9379c54808ae61d46
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''
import execjs
import requests

with open('js_file.js','r') as f:
    js = f.read()

js_obj = execjs.compile(js)
js_result = js_obj.call('good','世界')
print(js_result) # {'ts': '1655973269340', 'salt': '16559732693408', 'sign': '09af4af51fb9d6111891091447c0b7ba'}
headers ={
'Accept':'application/json, text/javascript, */*; q=0.01',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'en-US,en;q=0.9',
'Connection':'keep-alive',
'Content-Length':'261',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'OUTFOX_SEARCH_USER_ID=2076822304@10.108.162.133; OUTFOX_SEARCH_USER_ID_NCOO=1202618597.0501676; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcMi9NlUco208lNfLpgy; ___rl__test__cookies=1655973258087',
'Host':'fanyi.youdao.com',
'Origin':'https://fanyi.youdao.com',
'Referer':'https://fanyi.youdao.com/?keyfrom=dict2.index',
# 'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-ch-ua-platform':'"Linux"',
# 'Sec-Fetch-Dest':'empty',
# 'Sec-Fetch-Mode':'cors',
# 'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
data = {
'i':'',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'',
'sign':'',
'lts':'',
'bv':'5e787eef863a63d9379c54808ae61d46',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME',
}
word = input('请输入想要查询的单词：')
word = '''{}


'''.format(word)
js_result['i'] = word
js_result['lts'] =js_result.pop('ts')
data.update(js_result)
# print(data)
# url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
res = requests.post(url=url,headers=headers,data=data)
print(res.text)