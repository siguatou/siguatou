''''''
import requests

'''
from: zh
to: en
query: 自由
transtype: enter
simple_means_flag: 3
                                            sign: 752482.1022035
token: 74e4059467d60a0f1e8a4b88a91130c4
domain: common

from: zh
to: en
query: 平静
transtype: realtime
simple_means_flag: 3
                                            sign: 569233.806048
token: 74e4059467d60a0f1e8a4b88a91130c4
domain: common

'''

import execjs
import json

word = input('输入你想要查询的单词:')
with open('js_file.js','r') as f:
    js = f.read()

js_obj = execjs.compile(js)
js_result = js_obj.call('e',word)
print(js_result) # 232427.485594  752482.1022035

'''
320305.131321201

'''
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data = {
'from':'auto',
'to':'auto',
'query':'',
'transtype':'realtime',
'simple_means_flag':'3',
'sign':'',
'token':'74e4059467d60a0f1e8a4b88a91130c4',
'domain':'common'
}
data['sign'] = js_result

data['query'] = word
print('data:',data)
headers = {
'Accept':'*/*',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'en-US,en;q=0.9',
# 'Acs-Token':'1655881208798_1655975383577_8J+pQQrXloUvm0K8VG0IFP++uB5M3+FJcr40idDVAZuXBY2qyK3mxeKOon3mPCfldihDSD4iBCMjwYiAJyxGhE68K22X29XRKXyiEjxEjdyzyYNZcVSv5n6wQnD7WaM0AF3m14lvsiYX4EHMgUPQEYAAmqWidHETblkVBzIPx4sCZeGeI4UvQyh650Jnmy9YtwzuKdrc4xeiyO9v0Kwln/1drKjahnW6Wcka/40smVQtw1je208f5GvapZ7/usj1WJX2Zv+H9kZLRBxJUK41uKsNoO8C+yCWuAxFDLBdPDf9XHuEvhxKM6iPAq3hh4NN',
'Connection':'keep-alive',
# 'Content-Length':'135',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'BAIDUID_BFESS=CDD61DA64829C990DE1711436F787880:FG=1; RT="z=1&dm=baidu.com&si=r92nq2dzu8&ss=l4nvh8q1&sl=3&tt=ag7&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=fo0&ul=2cvf&hd=2cwm"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655968104; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1655975372; ab_sr=1.0.1_MzVkY2E3MzFjYWZmYTExYzcwNDk5NWU5YzdhMTAwZjI1YTBkZTE5YmZlMmNiMWQxMGEyZGI1OTkxYzFiZWNhMmMwYWZlMTNlYTkyODY0MWVjZjI0NjQ3M2I0YTQyYWI3ZGY3ZDQ5NmI3Y2ZlYWU2ZWJiNDdhODU0OWE1NTk4NWE5Nzk2NWE0ZGM2YWVlNzRiNGU1NDBkNmI0YTk4MmIxZQ==',
'Host':'fanyi.baidu.com',
'Origin':'https://fanyi.baidu.com',
'Referer':'https://fanyi.baidu.com/',
# 'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-ch-ua-platform':'"Linux"',
# 'Sec-Fetch-Dest':'empty',
# 'Sec-Fetch-Mode':'cors',
# 'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
res = requests.post(url=url,headers=headers,data=data)
# print(res.content.decode())
dict_result = res.content.decode()
dict_result =  json.loads(dict_result)
print(dict_result)
translate_res =  dict_result['trans_result']['data'][0]['dst']
print(translate_res)