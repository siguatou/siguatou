import base64

import requests
import re
from fontTools.ttLib import TTFont
# 264fPC3iU6n2OKMUe3p\/b2tT6EaCn6GbtpEcsk1pAfH+YTmj0q+wHkXyNPdMPCGWZNem
url = 'https://cs.58.com/ershouche/'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'f=n; commontopbar_new_city_info=414%7C%E9%95%BF%E6%B2%99%7Ccs; commontopbar_ipcity=wx%7C%E6%97%A0%E9%94%A1%7C0; userid360_xml=CDF1833D347476777994CFBE9AAD6D10; time_create=1658638769751; f=n; id58=CocHiGK1RK0RD16GA/KYAg==; fzq_h=a176ac2c139d08fbd88c65115a46ff75_1656046765494_b4d644526f0a4710b9c3b35c46ecd405_643001862; sessionid=f0021f64-bc60-4196-81da-596e599c4c19; fzq_js_usdt_infolist_car=e22b58acf20f811abe72ca0a6d00fecc_1656046767319_7; 58tj_uuid=af1de997-eb8a-48b1-b2ed-d7bb145d2c28; new_session=1; new_uv=1; utm_source=; spm=; init_refer=; wmda_uuid=02f42a83515ca49b31684817bc78493b; wmda_new_uuid=1; wmda_session_id_1732038237441=1656046768799-599c1016-34b0-74a0; wmda_visited_projects=%3B1732038237441; 58home=wx; als=0',
    'Host':'cs.58.com',
    'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
res = requests.get(url=url,headers=headers)
print(res)

with open('58tc.html', 'w', encoding='utf8') as f:
    f.write(res.text)
with open('58tc.html', 'r') as f:
    html = f.read()

price = re.findall('<b class="info_price fontSecret">(.*?)</b>',html)
# print(price)

# 保存字体库文件
# ttf是一个二进制的数据
ttf = re.findall("base64,(.*?)'",html)[0] # base64编码后的数据
with open('58tc.ttf','wb') as f:
    f.write(base64.b64decode(ttf))

# 通过TTFont打开字体库文件
font = TTFont('58tc.ttf')
font.saveXML('58tc.xml')

'''  &#xa5;.&#x65f6; 5.1 '''
BestCmap = font.getBestCmap()  # unicode与图形编号的对应关系
print(BestCmap)
GlyphMap = font.getReverseGlyphMap() # 具体的值和编号的关系
print(GlyphMap)

str1 = '&#xa5;.&#x65f6;'

# 获取真实的价格函数
def get_price(str1):
    s1 = str1.replace('&#','0').split(';')[:-1]
    money = ''
    for s2 in s1:
        # print(s2)
        if '.' in s2:
            money += '.'
            s2 = s2.replace('.','')
            # print(int(s2,16))
        # print(int(s2, 16))
        s21 = int(s2, 16)
        m1 = GlyphMap[BestCmap[s21]]
        m1 -= 1
        money += str(m1)
    return money

list1 = []
for data in price:
    price = get_price(data)
    list1.append(price)

print(list1)