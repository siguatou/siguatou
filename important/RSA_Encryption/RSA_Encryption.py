''''''
import base64
from binascii import hexlify, a2b_hex, b2a_hex

from Crypto.Util.number import bytes_to_long

'''
    Python的加密方式:RSA加密
    
    RSA加密是一種非對稱加密，通常使用公钥加密，私钥解密，私钥签名，公钥验签。
    
    在公开密钥密码体制中，加密密钥(即公开密钥)PK是公开信息，而解密密钥(即秘密密钥)SK是需要保密的。
    RSA算法通常是先生成一对RSA密钥，其中之一是保密密钥，由用户保存;另一个为公开密钥，可对外公开，甚至可在网络服务器中注册;
    
    RSA是一种公钥密码算法，加密算法是将明文m(m<n是一个整体)加密成密文c，
    即明文数字m的E次方求mod N，也就是将明文与自己相乘E次，然后结果除以N求余数，余数就是 密文c，E和N组合就是公钥。
    
    解密算法为将密文c解密为明文m，即密文数字c的D次方求mod N，也就是将密文与自己相乘D次，然后结果除以N求余数，余数就是明文m，
    D和N组合就是私钥;
'''

''' 1.生成公钥和私钥 '''
from Crypto import Random
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_generator = Random.new().read

# RSA算法生成实例
rsa = RSA.generate(1024,random_generator)

# 私钥的生成
private_pem = rsa.exportKey()
with open('private.pem','wb') as f:
    f.write(private_pem)

# 公钥的生成
public_pem = rsa.public_key().exportKey()

with open('public.pem','wb') as f:
    f.write(public_pem)
# ----------------------------------------------------------------------------


''' 2.加密(使用公钥加密) '''
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5, PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import ChaCha20_Poly1305

# 加密
message = 'Hello,This is RSA加密'
publickey = RSA.importKey(open('public.pem').read())
cipher = Cipher_pkcs1_v1_5.new(publickey)   # 创建用于执行pkcs1_v1_5加密或解密的密码
cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
print(cipher_text.decode('utf-8'))
cipher_text = cipher_text.decode('utf-8')
'''
    这里每次使用公钥加密后的结果都不一致，跟对数据的padding即填充有关。
    
    加密时支持的最大字节数与证书有一定关系。
    加密时支持的最大字节数:证书位数/8-11，(比如:2048位的证书，支持的最大加密字节数:2048/8 -11 =245)
    1024位的证书，加密时的最大支持117个字节，解密时为128;
    2048位的证书，加密时的最大支持245个字节，解密时为256。
    
    如果需要加密的字节数超出证书能加密的最大字节数，此时就需要进行分段加密。
'''

''' 3.解密(使用私钥解密)'''
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

# 解密
# cipher_text = 'Rl77SXECfzqXci1/ii8Zkl7wd8CUJ6txOImEwUYt99f/Be831VKBQX/Zz//Ynpfwtzu3pmtxDz+mkLdEtMvovESkMu2bQFtw5aG16iZsY8aqh3onHR6OQp0JrdvVa32M6HFKWyPNC9u3TGeFaQqH/4YTF3GXSyqeBjSX/gfTWX4='
encrypt_text = cipher_text.encode('utf-8')
rsakey = RSA.importKey(open('private.pem').read())
cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
text = cipher.decrypt(base64.b64decode(encrypt_text),'解密失败')
print(text.decode('utf-8'))


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
    a = int(hexlify(a[::-1].encode()),16) # 这里做了一个倒序,然后编码，然后转成16进制整形
    b = int(b,16)
    c = int(c,16)
    C = pow(a , b, c)
    result = hex(C)[2:]
    return result
result = make_c(message,'010001',"008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f")
print(result)

import rsa

#方法二
def encrypt_with_modulus(content, modulus=None):
    content = int(hexlify(content.encode()), 16)
    # content = int(hexlify(content[::-1].encode()), 16)
    e = '010001'
    e = int(e,16) # 16进制指数
    n = int(modulus,16) # 16进制模值
    rsa_key = RSA.construct((n, e)) # 指数和模值的组合，构成公钥
    # generate/export public key
    public_key = rsa_key.publickey()
    cipher = PKCS1_v1_5.new(public_key)
    content = cipher.encrypt(str(content).encode('utf-8'))
    content = b2a_hex(content)
    return str(content.decode())

result = encrypt_with_modulus(message,"008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f")
print(result)

