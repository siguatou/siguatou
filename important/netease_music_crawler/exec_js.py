import base64
import random

import requests
from Crypto.Cipher import AES
import rsa
from Crypto.PublicKey import RSA
from binascii import hexlify  # 将二进制数转化为十六进制数

# 使用Python实现js的加密

# RSA加密函数
def make_c(a, b, c):
    '''
        a 相当于M : 明文
        b 相当于e : 公钥指数
        c 相当于n : 模值
        C = M^e mod n
        Python中有一个函数pow(M,e,n)
    '''
    # d = new RSAKeyPair(b,"",c),
    # e = encryptedString(d, a)
    # 将字符串转为二进制，再将二进制转化为十六进制
    a = int(hexlify(a[::-1].encode()),16)
    b = int(b,16)
    c = int(c,16)
    C = pow(a, b, c)
    result = hex(C)[2:]
    return result

# AES加密函数
def make_b(a, b):
    # var c = CryptoJS.enc.Utf8.parse(b)
    c = b.encode() # b->c，作为AES加密函数的key值
    # , d = CryptoJS.enc.Utf8.parse("0102030405060708")
    d = '0102030405060708'.encode()
    # , e = CryptoJS.enc.Utf8.parse(a)

    aes = AES.new(key=c,mode=AES.MODE_CBC,iv=d)
    # , f = CryptoJS.AES.encrypt(e, c, {
    #   iv: d,
    #   mode: CryptoJS.mode.CBC}）

    # a,明文补齐16位
    num = 16 - len(a) % 16  # num为最终需要补齐的位数
    text = (a + num * chr(num)).encode()

    # 对表单信息a,进行加密
    en_text = aes.encrypt(text)
    b64_txt =  base64.b64encode(en_text).decode()
    return b64_txt


# 生成随机字符串的函数
def make_a(a):
    b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    c = ''
    for i in range(a):
        c += random.choice(b)
    return c

# 获取密文数据主函数
def make_d(d, e, f, g):
    i = make_a(16)
    encText = make_b(d, g)
    encText = make_b(encText, i)
    encSecKey =make_c(i, e, f)
    return {
        'params':encText,
        'encSecKey':encSecKey
    }
def get_formdata(ids):
    '''

    :return:
    '''
    d = '{"ids":"[%s]","level":"standard","encodeType":"aac","csrf_token":""}'%ids
    # d = '{"logs":"[{\"action\":\"mobile_monitor\",\"json\":{\"meta._ver\":2,\"meta._dataName\":\"pip_lyric_monitor\",\"action\":\"render\",\"userAgent\":\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36\",\"chromeVersion\":103,\"resourceId\":%s,\"resourceType\":\"song\"}}]","csrf_token":"6056374d9e4de8cf87dd6bfd7c00bce4"}'%ids
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'
    data =  make_d(d, e, f, g)
    # print(data)
    return data

# 获取音乐下载的链接
def get_music_url(data):
    '''
    :param data:
    :return:
    '''
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=6056374d9e4de8cf87dd6bfd7c00bce4'
    headers = {
        'accept': '*/*',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '510',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_ntes_nnid=53052bfbac9782f73b88695f4e113a47,1655689790783; _ntes_nuid=53052bfbac9782f73b88695f4e113a47; NMTID=00OZ4aZg3TZmG3MuU6Ps1FclyqAatEAAAGBfs1HvA; WEVNSM=1.0.0; WNMCID=ooieid.1655689792915.01.0; WM_TID=KynPVVpLrN9FABVQARfQUj6pseYiMDrY; __snaker__id=414Kle2j79AkKnD2; _9755xjdesxxd_=32; MUSIC_U=764b5c9cff5b08ac77e84a253de5205067d0414a19035eb43b534ca6c743dba2c84e8a4f4ba4f13e5259911f744f69c596f14e1f8ca0f9bc152ed44d224a52b1e91570495928db00d4dbf082a8813684; __remember_me=true; __csrf=6056374d9e4de8cf87dd6bfd7c00bce4; ntes_kaola_ad=1; gdxidpyhxdE=ux88zqS%2B30UJY9w%2F346B2h568wfNpGm%2BAY1xrP5YbKAqt9%2FHoY83e0rS6U1SHvH%2FVYjl8Rrtt0MQiaCkbCzNi7kTU47EQJJ%2FmrZpr7Trr%2By1w3MQ6me49lqUNmrRc05qblQ1NhXcI0ugktIlrLk0%5Cpoakl60P%5C6pCNXKgXGU8YWDUZ%2B4%3A1655720144306; _iuqxldmzr_=32; WM_NI=cPjSCNTsHTGR2n%2B3iCrLgZ8MFTXSG6d9cm8Y60IrwRZJxHv1iCsoeEmKEceBdkT45lCYxsr%2FdGpqVAOycfc4yQ6TlCywVwXCTNyWoaLys9Xz9rvOl5vUuAXsuTYwVuLrWGE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1f36ead938ad9ef63878a8ab6c85e839b8e86c15eb19dc0b9d87c8589a3d6b82af0fea7c3b92aa190a6b4c24698ad88b5c65af2b2e5d4ec49b294a9bbbb47868c98b4c63ea8e7ad8ebb53f6f08793f65a9a96b8a9f53bab9dbd90e84faf958b84e84aa8b59cd5b8688187b894f125a899c092d54b8da7ad87e240bb8ffab5ef49bba99a98db499892b7b8ee6b90a7bddadb72fbaebab0ef3fb68bbba2db79b78c9798d57f90ae99a8c837e2a3; playerid=78445525; JSESSIONID-WYYY=NsfEUHnq3zPDOHZEcPZH2RxWfVWH4eI4WvRHy65szVDEFHFT7OBlli9pdactPqCXp4pxqhhI4o63otcKgtZDN%2FHByichoKIXh3fz7tQdHOmOh%2B8%2Fvm9B7DDYAP%5CrgpTpE6F%5Cwg4pDF%2FsXXJKqaQnKibCprY7J%5CDRnJCYlkVH3%2Beaxaxw%3A1655954479163',
        'origin': 'https://music.163.com',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    res = requests.post(url,headers = headers,data=data)
    print(res)
    print(res.content)

if __name__ == '__main__':
    ids = '1410647903'
    data =  get_formdata(ids)
    get_music_url(data)




