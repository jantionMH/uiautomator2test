import requests
import jiphy,execjs
from datacenter.cryptoJS_PY import sign
from jpype import  *
from Crypto.Cipher import AES
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
def ddd():
     # d=bytearray("SHA256withRSA",encoding='utf-8')
     # key=RSA.import_key(open(file='./data').read())
     # h=SHA256.new(d)
     # a=PKCS1_v1_5.new(key).sign(h)
     # print(h)
     print(getDefaultJVMPath())
     startJVM()
     # java.lang.System.out.printIn('success')
     shutdownJVM()

def deal_the_GAdata():
        c = 0
        with open(file='my_source', mode='r', encoding='utf-8') as s:
           f=s.readlines()
           print(f)
           lenth=len(f)
           for i in range(lenth):

               firstrow=f[i].strip().split(',')[0]
               sencodrow=f[i].strip().split(',')[1]
               thirdrow=f[i].strip().split(',')[2]
               if 'iPhone' not in firstrow:
                   print(firstrow)
                   c+=1
               # print(firstrow,sencodrow)
               # if thirdrow!='用户数':
               #     print(thirdrow)
               #     percent=('%.2f%%'%((int(thirdrow)/21726)*100))
               #     print(percent)
               # with open(file='./newsource1',mode='a+',encoding='utf-8') as d :
               #         d.writelines(firstrow+'\n')
          # print(c)



def wetest():
        dict_wetest={}

        with open(file='./wetest_model', mode='r',encoding='utf-8') as f:
            f_wetest=f.readlines()
            print(f_wetest)

            for i in f_wetest:
               list_wetest = []
               key=i.strip('\n').split('\t')[0].capitalize()

               if key in list(dict_wetest.keys()):
                   value = i.strip('\n').split('\t')[1]
                   dict_wetest[key].append(value)

               else:
                   value = i.strip('\n').split('\t')[1]
                   list_wetest.append(value)
                   dict_wetest[key] = list_wetest

        print(dict_wetest)
        with open(file='./dict_wetest',mode='a',encoding='utf-8')as dictwetest:
            dictwetest.write(str(dict_wetest))

def mysource():
    dict_wetest = {}

    with open(file='./my_source', mode='r', encoding='utf-8') as f:
        f_wetest = f.readlines()
        print(f_wetest)
    #
        for i in f_wetest:
            list_wetest = []
            key = i.strip('\n').split('\t')[2].capitalize()

            if key in list(dict_wetest.keys()):
                value1 = i.strip('\n').split('\t')[0]
                value2 = i.strip('\n').split('\t')[1]
                dict_wetest[key].append(value1)
                dict_wetest[key].append(value2)
    #
            else:
                value1 = i.strip('\n').split('\t')[0]
                value2 = i.strip('\n').split('\t')[1]
                list_wetest.append(value1)
                list_wetest.append(value2)
                dict_wetest[key] = list_wetest
    #
    print(dict_wetest)
    with open(file='./dict_mysoruce', mode='w', encoding='utf-8')as dictwetest:
        dictwetest.write(str(dict_wetest))



def uppper_set_list():
    list_wetest = []

    with open(file='./wetest_model', mode='r', encoding='utf-8') as f:
        f_wetest = f.readlines()
        print(f_wetest)
        for i in f_wetest:
            keys = i.strip('\n').split('\t')[0]
            list_wetest.append(keys)
        upper=[j.capitalize() for j in list_wetest]
        new_listwetest=list(set(upper))
        print(new_listwetest)
        with open(file='./list_wwtest',mode='a',encoding='utf-8') as l:
               l.write(str(new_listwetest))



def compare():
    with open(file='./dict_wetest',mode='r',encoding='utf-8') as w:
        str_file_1=w.readline()
        dict_wetest=eval(str_file_1)
    with open(file='./dict_mysoruce',mode='r',encoding='utf-8') as M:
            str_file_2=M.readline()
            dict_mysource=eval(str_file_2)
    commom_key=list(dict_mysource.keys()&dict_wetest.keys())
    k=0
    total_comon_value=[]
    for  i in commom_key:
        commom_value=list(set(dict_mysource[i]).intersection(set(dict_wetest[i])))
        k+=len(commom_value)
        print(i,commom_value)
        total_comon_value+=commom_value
    print(k)
    print(len(total_comon_value),total_comon_value)

    #共有的机型列表
    with open(file='./final_common_sytlephone',mode='w',encoding='utf-8') as f:
        f.write(str(total_comon_value))


def file_overview():
    with open(file='./final_common_sytlephone',encoding='utf-8',mode='r') as f :
        fl=f.readline()
        print(len(eval(fl)))

def xv():
    with open('./data', 'r')as d:
        print(type(d.read()))


def get_req():
        with open('./data','r')as d :
            s=d.read()
        with open("new_file.js", "r") as f:
            data_func = f.read()  # 读取js文件
        tk = execjs.compile(data_func)  # 编译执行js代码
        tk = tk.call('sign', s)  # 调用函数 token为js里面的函数  a为传的参数
        tk = str(tk)
        print('tk=', tk)

class dcboxapi:
    def __init__(self):
         self.session=requests.session()

    def dcboxapi_register(self,name):
        body = {'nick_name': '', 'name': '', 'phone': '电话号码', 'phone_code': '区号', 'sms_code': '000000', 'captcha_id': '/',
                'password': '', 'device_id': '', 'public_key': '', 'pushid': '/'}

        request={'appid':'','sign':'','sign_type':'','retrieve':'','data':body,'seq':''}
        url='https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve'
        resp=self.session.post(url=url,data=request,verify=False)
        print(resp.text)

    def dcboxapi_login(self):

        data = {'phone': '177880', 'phone_code': '86', 'sms_code': '', 'nonce': '1', 'client_type': 'andriod', 'captcha_id': '',
                'password': 'a1111111', 'device_id': ''}
        request={'appid':'BITOLLWALLETDEMO','sign':'','sign_type':'SHA256WithRSAClient','retrieve':'login','data':data,'seq':'6'}

        c=sign(request)
        print(c)
        # re=self.session.post(url=' https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve',data=request,verify=False)
        # print(re.text)


if __name__ == '__main__':
      # ddd()
      #
      d=dcboxapi()
      # d.dcboxapi_register()
      d.dcboxapi_login()
