''''''
'''
    数据的加载分为很多种，常见的是:
    1.随网页返回
    2.xhr，异步请求
    3.js
'''
import requests
import json

'''
https://oss.guazi.com/gzim/bd208ce8-20ff-4200-ba8c-58ca7b70fd38.woff2
https://oss.guazi.com/gzim/bd208ce8-20ff-4200-ba8c-58ca7b70fd38.woff2

'''
font_url = 'https://oss.guazi.com/gzim/eb7b7a67-fd00-4607-9ff0-8b7613272e41.woff2'
html_url = 'https://mapi.guazi.com/api/home/pageIndex?osv=Android%2F5.0+(X11&moduleKeys=quick_select&platfromSource=wap&versionId=0.0.0.0&sourceFrom=wap&deviceId=b6e0c608-f490-491f-ae0d-437558c5a66b'

headers = {
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.9',
    'anti-token':'1277105907',
    'client-time':'1656305087',
    'client-timestamp':'1656305087',
    'cookie':'uuid=b6e0c608-f490-491f-ae0d-437558c5a66b; cainfo=%7B%22ca_s%22%3A%22seo_google%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%22b6e0c608-f490-491f-ae0d-437558c5a66b%22%7D; sessionid=7b53dc00-272d-41b0-ae38-b3b27205b897; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D',
    'origin':'https://www.guazi.com',
    'referer':'https://www.guazi.com/',
    'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-site',
    'szlm-id':'D2dxrCB807aoSOUhDuoz7SCLixvO8F8z7J5GfpqciZwsEX23',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
res = requests.get(url=html_url,headers=headers)
data_dict = json.loads(res.text)
cars_data_list = data_dict['data']
print(cars_data_list)

res = requests.get(url=font_url).content
# with open('./guazi_ershouche/gz.woff2','wb') as f:
with open('gz.woff2','wb') as f:
    f.write(res)

from fontTools.ttLib import TTFont
'''
   &#58928;&#60146;.&#59537;&#59854;万  83.40万 
'''
font = TTFont('gz.woff2')
font.saveXML('gz.xml')
# names = font.getGlyphNames()
# print(names)
bestCmap = font.getBestCmap()
# print(bestCmap)

glyphmap = font.getReverseGlyphMap()
# print(glyphmap)


str1 = '&#58928;&#60146;.&#59537;&#59854;万  83.40万 '
# 58928-> 0xe630 -> 9
# 60146-> 0xeaf2 -> 13
# 59537-> 0xe891 -> 11
# 59854-> 0xe9ce -> 12

str1 = str1.replace('&#','')
# print(str1) # 58928;58397;.59537;59854;万
list1 = str1.split(';')
# print(list1) # ['58928', '58397', '.59537', '59854', '万 ']
# real_price = ''
# for l in list1[:-1]:
#     if '.' in l:
#         real_price += '.'
#         l = l[1:]
#     l = int(l)
#     s1 = str(glyphmap[bestCmap[l]]-6)
#     real_price += s1
# real_price += '万'
# print(real_price)
def Sample():
    font = TTFont('gz.woff2')
    print(font.getGlyphNames())
    names = font.getGlyphNames()[3:-2]
    names.remove('uniE4D9')
    for name in names:
        # 获取glyf节TTGlyph字体x、y坐标信息
        print(name)
        aa = font['glyf'][name].coordinates
        print(aa)
        bb = font['glyf'][name].flags  # flags是指纹
        print(bb)
        print()

# sample字典的构建，需要在windows中通过fontcreator确定每个指纹信息对应的数字
sample ={
'\x01\x01\x01\x00\x01\x00\x01\x00\x01\x00\x01\x01\x00\x00\x01\x00\x00\x01\x00\x01\x00\x01\x00\x01\x01\x00\x01\x00\x01\x00\x00\x01\x00\x00\x01\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x01':4,
}

Sample()