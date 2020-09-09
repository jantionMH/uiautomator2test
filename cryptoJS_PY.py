import json

from Crypto import Signature
import uuid
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5, SHA256

# def sign(str):
#     with open(file='./data',mode='r')as f :
#         s=f.read()
#     key = RSA.import_key(s)
# sortdata = oprint(str,True)
# hSigVal = Signature.PKCS1_v1_5.new(key).sign(sortdata)
# hSigVal = Signature.PKCS1_v1_5.new(key).sign(str)
#     return base64.b64decode(hSigVal)
s = 'appid=BITOLLWALLETDEMO&data=map[captcha_id: client_type:andriod device_id: nonce:1 password:a1111111 phone:177880 phone_code:86 sms_code:]&retrieve=login&seq=6&sign_type=SHA256WithRSAClient'
prk = "MIIEpgIBAAKCAQEAruqz9+kW12YjNdCvwAsfhDhpvp8ylIDXZI8miW3k7U1/EwDT" \
      "MsDlvn5HiJ8eNOBJ0nj+tHYK1iHmB5reSXQ1hdOwGFc/KHJEIZGabC0+fw1ckQjM" \
      "gwTbIJUQYxANdb6yGHRXMlJl4BJXPDkEubIUSxztELr6+/q3vb5W4/Hjjx0sdfB7" \
      "MDcg0m2Fk7JV9NIBWAnwRPJtlTMuc8ASDABYm2oJ30KDE/BvtyMxY35Z2NwDDO23" \
      "d4P7OReTsuzWJSf8fRgpBw/irnJC6YjPqILJxHaFkbxlGeSnGKdBkO0F+MRdTHbm" \
      "b9nq/q4nduq6ADm3l0vRJgGO35gW34OU95f0YwIDAQABAoIBAQCMUv3OBNCuPOJC" \
      "agiUqFfAWwF6S3zoZfRmV/Eyj1b4iRNIy4CjVtz41ZXNpNk20jhnAWpUm95Vqxw/" \
      "PZ7WjsPheNHstRGWARVnWMfpwOJCSxXXxJdNBLhGi096KYaizzlRJQRO+ouAFzak" \
      "uZlw38wn9iy5H0f6nkiJkAllFMjaJdmQfYMX+i4P27RryfUEOLk0DTMkhjNXp/hh" \
      "18yBcuzklb83d00xQ8wQwccVAuLQIrQeUM7Z5ffTzu3MLqmfp3VxxT8xA2uOnf+j" \
      "yRLJvURZpcQD2as+ryYnK1Z26uXLFhMlAzNM9/oWRFeQGDC7wIftVD4FaWfjlkLy" \
      "PgRKJ2EBAoGBANzFEyi5WQboXVQis9tQlvnP777kyrhs1JOGg9Ay2nWxLgRchoj9" \
      "oOZ1hIN1z40wBYvYC60iiwSgH+sJADsbVHV3C86yLd8aXBLp1yz5/RECLDGXjQiJ" \
      "lsq4iEMLzRtVs+CbNpRzwZEL7OlMFoMu8Ci9THg0NKBej4DrmwI9C0sFAoGBAMrU" \
      "bulXkAJ+WWd4yua01etsViVKr3XAnwiSKX1myMvlZDPg5CdjCyW/cu+SBDl62KBW" \
      "DAuunoF08Rtdl+SrAlMD5Im++n5FWtTW/AEDNMlRvpNYnmHmB0ET1/SJexU4+eci" \
      "4rbfXuZr/BKYmZ/k1e1cvimbwX4ZlUCukTVbcm5HAoGBAMvld/x0srSehxPduR8l" \
      "H0s5sMMtq80JNovKAJOZZAquyUFd8yMynBg9EVYYyMgtQfIWZzJQZPSwrsn0VjJA" \
      "25BhkpYkGhmjzsXpEsKHYCMFTqu+vJLWAF7ab378t0I3tRoMQCx7fJrp2LTfgStH" \
      "fqchri6WiMRUkVUQROmcV4HBAoGBAL4RBYIJ+LwtdFAfBFve15tOIQe/Dd7VSvH4" \
      "LYMCn2VaJ2Tp+ELkcBzGY8kV1nmaoYbWO2FzF7uOPyX6tYylp37tZeqimQ9cpHpQ" \
      "n0O/omaJAIIJCBoLOX8FPlg7wKgphRzQNw1REhfw1v0CHOuVv9Y3E0fgWhh1lsRP" \
      "EWmjsP6fAoGBANPMCXFTTBGMhhB1npebJfqUF28vN4uWZ/X3ee6xqfYf1z8gRg1f" \
      "Mq087lb8ULck+3EyRRVtyFlnd9fU+lW+BYNF2aDwEOKO41MiYhhMM6ovIwmLBD9X" \
      "CL3tJx7XYdHhCDFy15HFAUZJhj7/CMSlh9ykPn7/NTu2sXO6RGlo5IwB"


#
# data = {'phone': 'VVA', 'phone_code': '852', 'sms_code': '00000', 'nonce': '1', 'client_type': 'andriod',
#         'captcha_id': '',
#         'password': 'Abcd1234', 'device_id': '51ceaca1-ba89-4922-ad1e-af18adecd24d'}
# request = {'appid': 'merchanttestvv', 'sign': '', 'sign_type': 'SHA256WithRSAClient', 'retrieve': 'login','seq': '6'}
#

def datadeal(r):
    print('原始字典{"":""}为：', r)
    for i in list(r.keys()):
        if not r.get(i):
            del r[i]
    sr = sorted(r)
    print("去掉值为空的键，并排序", sr)
    pre_d = []
    for j in sr:
        if r[j]:
            # pre_d+='%s=%s'%(j,r[j])
            pre_d.append('%s=%s' % (j, r[j]))

    newpred = '&'.join(pre_d)
    return newpred
    # return bytes(newpred,encoding='utf-8')


def hash_handle(d, hashtype):
    if hashtype == 'MD5':
        return MD5.new(d.encode('utf-8'))
    elif hashtype == 'SHA256':
        digest = SHA256.new()
        digest.update(d.encode('utf8'))
        return digest

    else:
        pass


def handle_private_key(key):
    start = '-----BEGIN RSA PRIVATE KEY-----\n'
    end = '-----END RSA PRIVATE KEY-----'
    result = ''
    # 分割key，每64位长度换一行
    divide = int(len(key) / 64)
    divide = divide if (divide > 0) else divide + 1
    line = divide if (len(key) % 64 == 0) else divide + 1
    for i in range(line):
        result += key[i * 64:(i + 1) * 64] + '\n'
    result = start + result + end
    # print(result)
    return result


def sign(p, re):
    # 导入私钥
    key = RSA.import_key(p)
    signer = Signature.PKCS1_v1_5.new(key)
    # 数据处理
    data = datadeal(r=re)
    print('格式化处理后的数据体:', data)
    d = SHA256.new()
    d.update(data.encode('utf8'))
    # 加签
    signed = signer.sign(d)
    print('密钥签名后',signed)
    final_sign = base64.b64decode(signed, '-_')


    print(final_sign)
    return final_sign




import rsa
def ras_easy():
     pub_pri=()
     pub_pri=rsa.newkeys(2048)
     print(pub_pri)


ras_easy()
