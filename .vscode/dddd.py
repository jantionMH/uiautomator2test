d = {"s1": "s", "s2": "s", "s3": {'a': '1', 'a1': '1', 'a2': '3'}, "s4": "s"}
c = {'a': '1', 'a1': '1', 'a2': '3'}
l = {"s1": "s", "s2": "s",
     "s3": {'a': '1', 'a1': '', 'a2': {'a': '1', 'a1': {'a': '1', 'a1': '1', 'a2': '3'}, 'a2': '3'}}, "s4": "s"}
l2 = {"s1": "s", "s2": "s",
      "s3": {'a': '1', 'a1': '', 'a2': {'a': '1', 'a1': {'a': ['1', 'iam list'], 'a1': '1', 'a2': '3'}, 'a2': '3'}},
      "s4": "s"}
data = {'phone': '177880', 'phone_code': '63', 'sms_code': '000000', 'nonce': '1', 'client_type': 'andriod',
        'captcha_id': '',
        'password': 'a1111111', 'device_id': '9c30691f-35a1-48da-8ed3-ae0b03f7b3f5'}
request = {'appid': 'BITOLLWALLETDEMO', 'sign': '', 'sign_type': 'SHA256WithRSAClient', 'retrieve': 'login',
           'data': data, 'seq': '6'}


# print(type(d))
# 分类字典和字符串
# 字符串 key1=value1&key2=value2
# 字典，继续分解key0=map[key1:value1 key2:value2 key3:value3 key4=map[k1:v1 k2:v2]]

def datatrack(r={}):
    p = []
    r1 = sorted(r)
    for i in r1:
        if type(r[i]) != dict:
            p.append(i + ':' + r[i])
        else:
            print('继续追踪', i)
            c = datatrack(r[i])
            p.append(i + ":" + c)
    p1 = ' '.join(p)
    conrdi = "map[" + p1 + "]"
    return conrdi


def d1(r={}):
    p = []
    for i in sorted(r):
        if dict == type(r[i]):
            print('继续追踪', i)
            c = datatrack(r[i])
            p.append(i + '=' + c)
        else:
            p.append(i + "=" + r[i])
    pp = '&'.join(p)
    print(pp)

# 3层
# d1(l)
