import json, time,logging
import urllib
from requests.auth import HTTPDigestAuth, HTTPBasicAuth
import requests
import jiphy, execjs
import uuid
from datacenter.cryptoJS_PY import datadeal, prk, signature_body, verify_signature
from jpype import *
from Crypto.Cipher import AES
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256


class DcboxOpenApi:
    def __init__(self):
        self.session = requests.session()
        self.ListRespToken = []
        self.dict_userinfo = {}
        self.s = 33  # 新增用户的注册序列号，增大
        self.sn = -2
        logging.basicConfig(filename='log.text',filemode='w', level=logging.INFO)


    def register(self):
        deviceid = uuid.uuid1()
        deviceid = str(deviceid)
        self.dict_userinfo['device_id'] = deviceid
        with open(file=r'C:\Users\janti\public.pem') as f1:
            pub_key = f1.read()
        with open(file='./data', mode='a') as f2:  # 存入用户信息
            f2.write('{"phone":"17794%s","name":"tolle%s","nick_name":"tollefly%s","device_id":"%s"}\n' % (
                self.s, self.s, self.s, deviceid))
        with open(file='./data', mode='r') as f3:
            s_f = f3.readlines()
            # print(eval(s_f[-1])['nick_name'],eval(s_f[-1])['phone'])
        data = {'nick_name': eval(s_f[self.sn])['nick_name'], 'name': eval(s_f[self.sn])['name'],
                'phone': eval(s_f[self.sn])['phone'], 'phone_code': '86', 'sms_code': '000000',
                'captcha_id': '',
                'password': 'a1111111', 'device_id': eval(s_f[self.sn])['device_id'], 'public_key': pub_key,
                'pushid': ''}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "register_by_userno",
                   "seq": "6",
                   "data": data}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        body = {'appid': 'BITOLLWALLETDEMO', 'sign': sig, 'sign_type': 'SHA256WithRSAClient',
                'retrieve': 'register_by_userno',
                'data': data, 'seq': '6'}
        print(type(body), body)
        body = json.dumps(body)
        url = 'https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve'
        resp = self.session.post(url=url, data=body, verify=False)
        self.user_info(resp=resp)
        # print('状态码%s\n响应头%s\n响应正文%s' % (resp.status_code, resp.headers, resp.content))

    def update_userdevice(self):
        userid = str(uuid.uuid1())
        print(userid)
        with open(file=r'C:\Users\janti\public.pem') as f:
            pub_key = f.read()
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
            print(eval(s_f[self.sn])['nick_name'], eval(s_f[self.sn])['phone'])
        # data = {"device_id": "9c30691f-35a1-48da-8ed3-ae0b03f7b3f5", "public_key": pub_key, "sms_code": "000000",
        #         "pushid": ""}
        data = {"device_id": userid, "public_key": pub_key, "sms_code": "000000",
                "pushid": ""}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient",
                   "phone": "",
                   "phone_code": "", "retrieve": "update_user_device", "seq": "6",
                   "data": data}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "phone": "",
                "phone_code": "", "retrieve": "update_user_device", "seq": "6",
                "data": data}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)
        print(re.text)

    # 2
    def login(self, phone, phone_code, sms_code, nonce, client_type, password, device_id, appid, sign_type,
              rertieve, seq):
        """
       参数示例
       :param phone: 177880
       :param phone_code: 86
       :param sms_code: 000000
       :param nonce: 1
       :param client_type: android
       :param password: a1111111
       :param device_id: 9c30691f-35a1-48da-8ed3-ae0b03f7b3f5
       :param appid: BITOLLWALLETDEMO
       :param sign_type: SHA256WithRSAClient
       :param rertieve: login
       :param seq: 6
       :return:
       """

        data = {"phone": phone, "phone_code": phone_code, "sms_code": sms_code, "nonce": nonce,
                "client_type": client_type,
                "captcha_id": "",
                "password": password, "device_id": device_id}
        request = {"appid": appid, "sign_type": sign_type, "retrieve": rertieve, "data": data,
                   "seq": seq}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        # verify_signature(message=request, signature=sig, pub_rsa_path=r'C:\Users\janti\public.pem')
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "login",
                "data": data, "seq": "6"}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,
                               verify=False)
        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 2.1
    def login_by_phone_password(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()

        data = {"phone": eval(s_f[self.sn])['phone'], "phone_code": "86", "sms_code": "000000", "nonce": "1",
                "client_type": "android",
                "captcha_id": "", "password": "a1111111", "device_id": eval(s_f[self.sn])['device_id']}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient",
                   "retrieve": "login_by_phone_password", "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "retrieve": "login_by_phone_password", "data": data, "seq": "6"}
        body = json.dumps(body)
        # print(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)
        self.user_info(resp=re)
        # print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))
        re_json=json.loads(re.content)
        print(re_json)
        self.balance = re_json["assets"][0]["balance"]
        logging.info("当前登录的是:"+re_json["nick_name"])
        logging.info("当前U余额"+self.balance)




    # 2.2
    def login_by_userno_password(self):
        # 请求数据签名阶段
        with open(file=r'C:\Users\janti\public.pem') as f:
            pub_key = f.read()
        data = {"name": "", "phone": "", "phone_code": "", "email": "", "password": "", "sms_code": "", "nonce": "",
                "client_type": "", "captcha_id": "", "device_id": "", "open_id": "", "user_no": "", "pin_code": "",
                "public_key": pub_key, "pushid": "", "google_code": ""}

        request = {"appid": "", "sign": "", "sign_type": "", "retrieve": "", "data": data, "seq": ""}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "retrieve": "login_by_userno_password", "data": data, "seq": "6"}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 3
    def refresh_token(self):
        # 请求数据签名阶段
        data = {}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "name": "880", "phone": "177880",
                   "phone_code": "86",
                   "token": self.ListRespToken[0], "retrieve": "refresh_token", "data": data, "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "name": "880",
                "phone": "177880",
                "phone_code": "86",
                "token": self.ListRespToken[0], "retrieve": "refresh_token", "data": data, "seq": "6"}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,
                               verify=False)
        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 4
    def send_sms(self):
        # 请求数据签名阶段
        data = {"usage": 9, "phone_code": "86",
                "phone": "177880"}  # 0:register, 1:change password, 2:change telephone, 3:transfer, 4:withdraw, 5:frozen, 6:upate device, 7:without password payment, 8:change pincode, 9:Login, 10:deposit
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "send_sms", "seq": "6",
                   "data": data}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "send_sms",
                "seq": "6", "data": data}
        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)
        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 4.6
    def change_pin_code(self):
        # 请求数据签名阶段
        with open(file='./data', mode='r') as f3:
            s_f = f3.readlines()
        data = {"sms_code": "000000", "new_pin_code": "000000", "google_code": ""}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "phone": "86",
                   "phone_code": eval(s_f[self.sn])['phone'], "token": self.ListRespToken[0],
                   "retrieve": "change_pin_code", "seq": "6", "data": data}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段

        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "phone": "86",
                "phone_code": eval(s_f[self.sn])['phone'], "token": self.ListRespToken[0],
                "retrieve": "change_pin_code",
                "seq": "6", "data": data}

        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)
        # self.user_info(resp=re)
        print('状态码%s，响应正文%s' % (re.status_code, re.content))

    def get_captcha(self):
        re = self.session.get(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha')
        print(re.text)

    # 9
    def transfer(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"asset_name": "USDT", "order_id": "",
                "to_phone": "177890", "to_phone_code": "86",
                "to_user": "", "amount": "1", "pin_code": "000000"}

        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "transfer",
                   "name": eval(s_f[self.sn])["name"], "phone": "177880", "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "transfer",
                "name": eval(s_f[self.sn])["name"], "phone": "177880", "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}
        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,
                               verify=False)
        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 10
    def assets_list(self):
        # 请求数据签名阶段
        data = {}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient",
                   "name": "880", "phone": "177880", "phone_code": "86",
                   "token": self.ListRespToken[0], "retrieve": "assets_list", "data": data,
                   "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "name": "880", "phone": "177880", "phone_code": "86",
                "token": self.ListRespToken[0], "retrieve": "assets_list", "data": data,
                "seq": "6"}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,
                               verify=False)
        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 11
    def deposit(self):

        with open(file='data', mode='r')as f:
            s_f = f.readlines()

        # 请求数据签名阶段
        data = {"asset_name": "USDT", "from": "", "to": "", "amount": "1000000000000"}

        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0], "retrieve": "deposit", "data": data,
                   "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0], "retrieve": "deposit", "data": data,
                "seq": "6"}
        body = json.dumps(body)
        print('这是body', body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body)
        self.user_info(resp=re)
        # print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # 13
    def assets_gen(self):
        # 请求数据签名阶段
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        data = {"asset_name": "USDT"}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "assets_gen",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "assets_gen",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,
                               verify=False)
        self.user_info(resp=re)

        # print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    #  f.1
    def card_list(self):
        # print(self.ListRespToken[0])
        # 请求数据签名阶段
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        data = {}
        # data = {"id": "", "merchantid": "", "name": "", "asset_name": "", "start_time": "", "end_time": "",
        #         "logoid": "", "display_interest_intro": "", "rate_percentage": "", "display_rate_intro": "",
        #         "access_value": "", "display_access_intro": "", "balance": ""}
        # request = {"balance": data, "cumulative_earn": "", "profit_earn": "",
        #            "last_earn": "", "rate": ""}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "card_list",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "card_list",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0], "data": {}, "seq": "6"}
        body = json.dumps(body)
        # print(type(body), body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/app', data=body)
        # print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

        dict_response = re.json()
        # print(dict_response["demand_list"])
        # print("产品列表:", dict_response["demand_list"])
        plist=dict_response["demand_list"]

        if len(plist)==0:
            self.pid_1 = False
            print("当前没有产品",self.pid_1)
        elif len(plist)>=1:
            print("第一个产品", dict_response["demand_list"][0])
            first = dict_response["demand_list"][0]
            self.pid_1=first["id"]
            logging.info('产品id'+self.pid_1)
            # with open(file='./personalinfo.text', mode='a') as f:
            #     f.write(str(first)+'\n')

    #  f.2
    def amount_list(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "amount_list",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        #
        # # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "amount_list",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)
        # print(body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/app', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    # f.2
    def get_card(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"id": "5f842cfada15e100073c5df3"}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "get_card",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        #
        # # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "get_card",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)
        # print(body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/app', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    def deal_list(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"json": "TYPE_ALL", "card_type": "TYPE_ALL"}  # default:TYPE_ALL,TYPE_BUY,TYPE_SELL,TYPE_INTEREST
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "deal_list",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        #
        # # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "deal_list",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/app', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    def buy(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"card_id": self.pid_1, "asset_name": "USDT", "amount": "1000", "pin_code": "000000",
                "sms_code": "000000", "google_code": ""}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "buy",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        #
        # # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "buy",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)

        try:
           re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/app', data=body)
           print('接口名称:buy，状态码%s,响应正文%s' % (re.status_code, re.content))
        except:
            print("请检查产品状态",self.pid_1)
            print('playload检查',body)


    def sell(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"card_id": "5f843541addf0100070158d9", "asset_name": "USDT", "amount": "1", "pin_code": "000000",
                "sms_code": "000000", "google_code": ""}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "sell",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0],
                   "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        #
        # # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "sell",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/iapp', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    def get_card_logo(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"id": "5f72d68f2db5c0000653039b"}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "get_card_logo",
                   "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                   "token": self.ListRespToken[0], "data": data, "seq": "6"}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient",
                "retrieve": "get_card_logo",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/app', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    def upload_wealth_logo(self):
        with open(file='data', mode='r')as f:
            s_f = f.readlines()
        # 请求数据签名阶段
        data = {"json": "body"}
        request = {"appid": "GZWallet", "sign_type": "SHA256WithRSAClient",
                   "name": eval(s_f[self.sn])['name'], "token": self.ListRespToken[0], "method": "upload_wealth_logo",
                   "data": data}

        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')
        #
        # # 请求发送阶段
        body = {"appid": "GZWallet", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "upload_wealth_logo",
                "name": eval(s_f[self.sn])['name'], "phone": eval(s_f[self.sn])['phone'], "phone_code": "86",
                "token": self.ListRespToken[0],
                "data": data, "seq": "6"}

        body = json.dumps(body)
        print(body)
        re = self.session.post(url='https://w2xfoobdd4.execute-api.ap-east-1.amazonaws.com/dev/manager', data=body)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    def post_expample(self):
        # 请求数据签名阶段
        data = {"": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": ""}
        request = {"appid": "BITOLLWALLETDEMO", "sign_type": "SHA256WithRSAClient", "retrieve": "expample",
                   "data": data, "seq": "6"}
        sig = signature_body(message=request, rsa_path=r'C:\Users\janti\private.pem')

        # 请求发送阶段
        body = {"appid": "BITOLLWALLETDEMO", "sign": sig, "sign_type": "SHA256WithRSAClient", "retrieve": "expample",
                "data": data, "seq": "6"}
        body = json.dumps(body)
        re = self.session.post(url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve', data=body,
                               verify=False)

        print('状态码%s\n响应头%s\n响应正文%s' % (re.status_code, re.headers, re.content))

    def user_info(self, resp):
        str_re = resp.content.decode()
        dict_re = eval(str_re)
        # print(dict_re)
        if dict_re['comment'] == 'success':
            if 'token' in list(dict_re.keys()):
                print('方法:' + dict_re['retrieve'], "成功", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                token = dict_re['token']
                self.ListRespToken.append(token)
            else:
                print('方法:' + dict_re['retrieve'], "成功", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        else:
            print('方法:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), dict_re)


if __name__ == '__main__':
    # 小金库API
    d = DcboxOpenApi()
    # d.update_userdevice()
    # d.login(phone=input('请输入电话:'), phone_code=input('请输入区号:'), sms_code=input('请输入短信验证码:'),
    #         nonce=input('请输入nonce:'), client_type=input('请输入客户端类型:'), password=input("请输入用户密码:"),
    #         device_id=input('请输入设备id:'), appid=input("请输入appid:"), sign_type=input('请输入签名类型:'),
    #         rertieve=input('请输入子接口名'), seq=input("请输入seq："))
    # d.refresh_token()
    # d.send_sms()
    # d.get_captcha()  #失败 get message : internal server error
    # d.assets_list()

    # d.register()

    # 登录
    d.login_by_phone_password()
    # 转账
    # d.transfer()
    # 设置账户
    # d.assets_gen()
    # 充值
    # d.deposit()#已废除的接口
    # 修改支付密码
    # d.change_pin_code()

    # 理财模块
    d.card_list()
    # d.amount_list()
    # d.get_card()
    # d.deal_list()#失败，开发未回复
    d.buy()
    # d.sell()
    # d.get_card_logo()#失败，开发未回复
    # d.upload_wealth_logo()#失败，开发未回复
