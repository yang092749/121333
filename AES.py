# from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
#
# key = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F"
# print(len(key))
# #key = a2b_hex('ey=U2FsdGVkX1/nSQN+hoHL8OwV9iJB/mSdKk5dmusulz4=')
# #'密钥/密文 长度可以为128、192或256位',不够要补齐
# #text =b"\x32\xBA\xCE\x43\x59\xAC\x1E\xFA\x1D\x5D\xBD\x34\xED\x48\x8C\x5B\x9D\xF9\xDE\x5B\x6E\x17\x20\xB5\xBB\x59\x36\x72\x25\x31\xB9\x5B"
# text = a2b_hex('667B33376C3034386131353967323630')
# print(len(text))
# cryptos = AES.new(key, AES.MODE_ECB)#密钥
# #print(cryptos.decrypt(text))# 解密密文
# en_text = cryptos.encrypt(text) #加密明文
# print(en_text)
import base64
from Crypto.Cipher import AES
#text =b'Salted__\xe7I\x03~\x86\x81\xcb\xf0\xec\x15\xf6"A\xfed\x9d*N]\x9a\xeb.\x97>'
#text=text.decode("base64")
#text = b'CCGandGulu\x00\x00\x00\x00\x00\x00'
#pass = b'Tokyo\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
text=b'\xed+\x10Zfy\xdb\x88\xbf\xc9U\xa81\xe0\x08$'
password = b'weigongcun\x00\x00\x00\x00\x00\x00'
aes = AES.new(password,AES.MODE_ECB) #创建一个aes对象
n_text = aes.decrypt(text) # 解密密文
print(n_text)


import base64
from Crypto.Cipher import AES
s=base64.b64decode(b'BxLHc1KruiH31I94W171oal+9olDzgBIjnK/J1Db0IUyi+MbI38+nw62ejCPShRB')
# f=open(r'enc','rb')
# buf=f.read()
# f.close()
# dump=[]
# for i in range(len(buf)):
#     dump.append(buf[i]^52)
# f=open(r'dump.dex','wb')
# f.write(bytes(dump))
# f.close()
key=b'r3v3rs3car3fully'
iv=base64.b64decode(b'2Aq7SR5268ZzbouE')
aes=AES.new(b'FV8aOaQiak6txP09',AES.MODE_CBC,b'2Aq7SR5268ZzbouE')
ans=aes.decrypt(s)
print(ans)


from Crypto.Cipher import AES
import os
# 加密函数
def encrypt(text, key, iv):
    # 将key和iv转为二进制格式
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    # 补齐text的长度为16的倍数
    length = 16 - (len(text) % 16)
    text = text + chr(length) * length
    # 创建AES加密器
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 加密
    ciphertext = cipher.encrypt(text.encode('utf-8'))
    # 返回加密后的结果
    return ciphertext.hex()
# 测试
if __name__ == '__main__':
    # 待加密的文本
    text = 'hello world'
    # 密钥
    key = '1234567890123456'
    # 初始向量
    iv = 'abcdef1234567890'
    # 加密
    ciphertext = encrypt(text, key, iv)
    print(ciphertext)