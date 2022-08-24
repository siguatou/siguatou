import json

import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Crypto.Util.Padding import pad,unpad

# 密钥(key) ， 密斯偏移量(iv) ， CBC模式加密
# AES加密
def AES_Encrypt(key,data):
    vi = '0102030405060708'
    # pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    # 用户数据补位之前，要进行字符串->字节串的转换(utf-8)
    data = pad(data.encode('utf8'),16)
    # 字符串补位(在数据进行加密之前进行)
    cipher = AES.new(key.encode('utf8'),AES.MODE_CBC,vi.encode('utf8'))
    # encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 这里加密的数据，一定是补位过后的字节串数据
    encryptedbytes = cipher.encrypt(data)
    # 加密后得到的是bytes类型的数据 b'\xb2\x8a\xb1z>\xe5\x18#\x92\xa6@j\xcf\xdeN\x08'
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码，返回byte字节串
    enctext = encodestrs.decode('utf8')
    # 对byte字节串按utf-8进行解码

    return enctext

# AES解密
def AES_Decrypt(key,data):
    vi = '0102030405060708'
    data = data.encode('utf8')
    encodebytes = base64.b64decode(data)
    # 将加密数据转换为bytes类型数据
    cipher = AES.new(key.encode('utf8'),AES.MODE_CBC,vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    # unpad = lambda s:s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted,16)
    # 去补位(在数据解密之后进行)
    text_decrypted = text_decrypted.decode('utf8')

    return text_decrypted

key = '0CoJUm6Qyw8W8jud' #自己密钥
data = 'asdasfsafsadf' #需要加密的内容
enctext = AES_Encrypt(key,data)
print(enctext)
text_decrypted = AES_Decrypt(key,enctext)
print(text_decrypted)

