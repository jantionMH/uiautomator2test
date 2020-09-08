import  uiautomator2
import os,time
from dcboxandroid.assertment import *

"""
#流程1
#测试准备： 上传chrome浏览器包安装和游戏包
#安装测试和覆盖安装测试：打开浏览器，跳转到下载android页面，下载并安装，安装上传的游戏包
#公共动态场景：1短信验证码获取
         2谷歌验证码获取
         
#公共静态场景：指纹验证必须处于关闭的状态
  
#测试场景一:UAT和pro都遵循场景
          登录测试：场景1验证码登录测试
                  场景2密码登录测试
                  场景3谷歌验证码登录测试
                  场景4忘记登录密码 转 登录
测试场景二 优先级低：uat环境独有
         注册测试:
         
下周工作:
  分离pro场的测试
  远程机器无sim卡无法真场测试，短信验证码
          
"""

class dcboxtest:
        def __init__(self,devicesIP):
            print('连接设备')
            device = uiautomator2.connect(devicesIP)
            if device.info != None:
                print(device.info)
            else:
                print('连接失败')
            self.d = device
            self.d.implicitly_wait(60)
            self.d.watcher
        def inittest(driver):

                    # print('传送测试包和chrome包到android')

                    # print('指定用chrome浏览器打开官网')
                    # os.popen("adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main -a android.intent.action.VIEW -d 'https://wwww,xxxxxx.com'")

                    d = os.popen(cmd='adb shell pm list packages')
                    r = d.read()
                    print(type(r))
                    if 'com.speedstae.dcbox' in r:
                        os.popen(cmd='adb uninstall com.speedstae.dcbox')
                        print('清空安装过的包')
                        time.sleep(2)
                    else:
                        print('没有发现已安装的包')
                    print('安装')
                    os.popen(cmd=r'adb install C:\Users\janti\Downloads\dcbox-3.1.17.198.apk')
                    print('安装中。。。')
                    driver.d.wait_activity('com.speedstae.dcbox.MainActivity')
                    print('安装结束')
                    os.popen(cmd=r'adb shell am start  com.speedstae.dcbox/com.speedstae.dcbox.MainActivity ')
                    print('启动app')



                    driver.d.app_wait('com.speedstae.dcbox')
                    print('app已启动，立即进入')
                    try:
                       driver.d(text="立即进入").click()
                       print('第一次登录')
                       driver.UATenter()

                       driver.Back_uplevel()
                       driver.Back_uplevel()
                       driver.cilcklogin()
                    except:
                        driver.UATenter()
                        driver.Back_uplevel()
                        driver.Back_uplevel()
                        driver.cilcklogin()


        def UATenter(driver):

            # driver.d(text='钱包余额\000(USDT)\n点击登\n账单\000登录后查看').click()
            driver.d.click(400,250)
            driver.d.click(400,250)
            driver.d.click(400,250)
            driver.d.click(400,250)
            driver.d(text="注册").click()

            for i in range(20):
                    time.sleep(0.1)
                    driver.d(text="钱包").click()

        def Back_uplevel(self):
            self.d(text='Back').click()
        def cilcklogin(self):
            self.d.click(0.298, 0.242)




        def verifycode_login(self,num):
            self.d.send_keys(text=num)
            self.d(text="下一步").click()
            self.d.sleep(2)
            self.d.send_keys(text='000')
            self.d.sleep(1)
            self.d.send_keys(text='000')
            assertappear(name='验证码登录',actual=self.d(text='收款').get_text(),expect='收款')

        def password_login(self):
            self.d(text='密码登录').wait()
            self.d(text='密码登录').click()
            self.d(text='密码登录').click()

            # self.d.send_keys('177880')
            self.d(text='请输入密码').click()
            self.d.send_keys('a1111111')
            self.d(text="登录").click()
            # try:
            #     self.d(text='请输入验证码').click()
            #     self.d.send_keys(text='000000')
            #     self.d(text="登录").click()
            # except:
            #     print('不是第一次登录')
            assertappear(name='密码登录', actual=self.d(text='收款').get_text(), expect='收款')

        def forget_passwd(self):
            self.d(text='密码登录').wait()
            # self.d(text='密码登录').clear_text()
            self.d(text='密码登录').click()
            self.d(text='忘记密码').click()
            # self.d.send_keys(text='177880')
            self.d(text='请输入验证码').click()
            self.d.send_keys(text='000')
            self.d.sleep(1)
            self.d.send_keys(text='000')
            self.d(text='提交').click()
            self.d(text='请输入您的新密码').click()
            self.d.send_keys(text='a1111111')
            self.d(text='请再次输入您的新密码').click()
            self.d.send_keys(text='a1111111')
            self.d(text='提交').click()
            assertappear(name='(忘记密码)重新设置登录密码',actual=self.d(text='密码已重设').get_text(),expect='密码已重设')
            self.d(text='登录').click()




        def check_homepage(self):
            """
            页面元素检查

            """
            self.d.click(75,80)
            self.d.click(75,80)
            self.d.click(75,80)
            self.d(text="扫一扫").wait()
            assertappear(name='扫一扫',actual=self.d(text='扫一扫').get_text(),expect='扫一扫')
            self.Back_uplevel()

            self.d.click(60, 340)
            self.d.click(60, 340)
            self.d.click(60, 340)
            self.d(text='账单').wait()
            assertappear(name='进入账单页面',actual=self.d(text='账单').get_text(),expect='账单')
            self.Back_uplevel()

            self.d.click(60, 265)
            self.d.click(60, 265)
            self.d.click(60, 265)
            self.d(text='资产').wait()
            assertappear(name='进入资产页面',actual=self.d(text='资产').get_text(),expect='资产')
            self.d(text='编辑钱包').click()
            self.d(text='主要').wait()
            assertappear(name='编辑钱包',actual=self.d(text='编辑钱包').get_text(),expect='编辑钱包')
            self.d(text='确定').click()
            self.Back_uplevel()


            self.d(text='小金库公开资产验证').click()
            assertappear(name='进入资产验证界面',actual=self.d(text='小金库公开资产验证').get_text(),expect='小金库公开资产验证')
            self.Back_uplevel()

        def received_payment(self):
            self.d(text='收款').click()
            assertappear(name='进入收款界面',actual=self.d(text='选择币种').get_text(),expect='选择币种')
            self.d(text='USDT').click()
            assertappear(name='进入币种选择界面',actual=self.d(text='USDT收款').get_text(),expect='USDT收款')
            self.d(text='保存收款码').click()
            assertappear(name='保存收款码',actual=self.d.toast.get_message(),expect='保存成功')
            self.Back_uplevel()
            self.Back_uplevel()

        def transfer(self):
            """
             常用联系人转账
                        """
            self.d(text='转账').click()
            print(self.d(text='转账').wait())
            assertappear(name='进入转账页面',expect=self.d(text='转账').get_text(),actual='转账')
            self.d(text='常用联系人').click()
            assertappear(name='进入常用联系人',expect=self.d(text='常用联系人').get_text(),actual='常用联系人')
            self.d.click(50,180)
            self.d.click(50,180)
            self.d(text='下一步').click()
            self.d(text='转账金额').click()
            self.d.send_keys('1')
            self.d(text='货币切换').click()
            assertappear(name='转账货币切换',expect=self.d(text='CNY').get_text(),actual='CNY')
            self.d(text='下一步').click()
            self.d(text='立即付款').click()
            #分支补充忘记支付密码
            self.d.send_keys(text='000000')
            assertappear(name='进入转账成功页面',expect=self.d(text='已经成功转账').get_text(),actual='已经成功转账')
            self.d(text='返回').click()

            """
            直接输入金库号转账
            """
            self.d(text='转账').click()
            self.d.send_keys(text='SM901988')
            self.d(text='下一步').click()
            self.d(text='转账金额').click()
            self.d.send_keys('1')
            self.d(text='货币切换').click()
            assertappear(name='转账货币切换', expect=self.d(text='CNY').get_text(), actual='CNY')
            self.d(text='下一步').click()
            self.d(text='立即付款').click()
            # 分支补充忘记支付密码
            self.d.send_keys(text='000000')
            assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
            self.d(text='返回').click()
            #专项验证，用户名


            """
            链上地址转账
            """
            self.d(text='转账').click()
            # self.d.send_keys(text='0xCa7B7887522BF4dB10c9F9646FC326483779017c')#880
            self.d.send_keys(text='0x7De7fb55A42DDf2c8AFd3e5727fe579CeBF89eac')#890
            self.d(text='下一步').click()
            self.d(text='转账金额').click()
            self.d.send_keys('1')
            self.d(text='货币切换').click()
            assertappear(name='转账货币切换', expect=self.d(text='CNY').get_text(), actual='CNY')
            self.d(text='下一步').click()
            self.d(text='立即付款').click()
            # 分支补充忘记支付密码
            self.d.send_keys(text='000000')
            assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
            self.d(text='返回').click()

        def personal1(self):
            """

            更换头像
            :return:
            """
            self.d(text='收款').wait()
            self.d.click(500, 1240)#逍遥模拟器
            # self.d.click(0.737, 0.897)#nokia
            self.d(text='常用联系人').wait()
            self.d.click(200, 163)
            self.d(text='更改个人头像').wait()
            self.d.click(360,150)
            self.d(text='本地相册').click()
            self.d.click(100,180)
            self.d.click(100,180)
            self.d.click(100,180)



            """
            昵称修改
            """
            self.d(text='登出').wait()
            self.d(text='昵称\n880').click()
            self.d(text='880, 请输入昵称').click()
            self.d(text='确定').click()
            self.Back_uplevel()
            #
            """
            常用联系人
            """
            self.d(text="常用联系人").wait()
            self.d(text='常用联系人').click()


            if self.d(text='没有联系人').wait()==True:
                """
                金库号添加好友
                """
                self.d.click(680,50)
                self.d.click(680,50)
                self.d.click(680,50)

                self.d(text='请输入金库号').click(timeout=2)
                self.d.click(106,208)
                self.d.send_keys(text='SM901988')
                self.d(text='确定').click()


                """
                删除第一个好友
                """
                print(self.d(text='最近').wait())
                self.d.click(100,180)
                self.d.click(100,180)
                self.d.click(100,180)
                self.d.click(100,180)
                self.d.click(100,180)
                self.d.click(100,180)
                self.d(text='删除').wait()
                self.d(text='删除').click()
                self.d(text='常用联系人').wait()
                """
                手机号添加好友
                """
                self.d.click(680, 50)
                self.d.click(680, 50)
                self.d.click(680, 50)
                self.d(text='添加联系人').wait()
                self.d.swipe(fx=500,fy=500,tx=100,ty=500)

                # self.d(text='手机号码').click()
                self.d(text='请输入手机号码').click(timeout=2)
                self.d.click(106, 208)
                self.d.send_keys(text='177890')
                self.d(text='确定').click()
                self.d(text='最近').wait()
                self.Back_uplevel()
            elif self.d(text='最近').wait()==True:
                """
                                                    删除第一个好友
                                                    """

                self.d.click(100, 180)
                self.d.click(100, 180)
                self.d.click(100, 180)
                self.d(text='删除').wait()
                self.d(text='删除').click()
                # self.d(text="常用联系人").wait()


                """
                                添加好友
                                """
                self.d(text="没有联系人").wait()
                self.d.click(680, 50)
                self.d.click(680, 50)
                self.d.click(680, 50)
                self.d.click(680, 50)


                self.d(text='请输入金库号').click(timeout=2)
                self.d.click(106, 208)
                self.d.send_keys(text='SM901988')
                self.d(text='确定').click()
                self.d(text='常用联系人').wait()
                self.Back_uplevel()



            """
            消息通知
            """
            self.d(text='消息通知').click()

            asserNOTexception(actual=self.d.toast.get_message(),expect='',name='消息通知页面')
            self.Back_uplevel()

            """
            安全
            
            修改登录密码
            """
            self.d(text='安全').click()
            self.d(text='密码设置').wait()
            self.d(text='密码设置').click()
            self.d(text='修改登陆密码').wait(timeout=20)
            self.d(text='修改登录密码').click()
            self.d(text='请输入当前登录密码').wait()
            self.d(text='请输入当前登录密码').click()
            self.d.send_keys(text='a1111111')
            self.d(text='请输入新登录密码').click()
            self.d.send_keys(text='a1111111')
            self.d(text='提交').click()
            assertappear(name='修改登录密码',actual=self.d(text='密码已重设').wait(),expect=True)
            self.d(text='返回').click()

            # self.Back_uplevel()
            self.Back_uplevel()

            self.d(text='常用联系人').wait()
            self.d.click(200, 163)
            self.d.click(200, 163)
            self.d.click(200, 163)
            self.d(text='登出').wait()
            self.d(text='登出').click()


            self.d(text="下一步").wait()
            self.d(text="下一步").click()
            self.d.sleep(2)
            self.d.send_keys(text='000')
            self.d.sleep(1)
            self.d.send_keys(text='000')
            assertappear(name='验证码登录', actual=self.d(text='收款').get_text(), expect='收款')


            """
            修改支付密码
            """
            print(self.d(text='收款').wait())
            self.d.click(500, 1240)
            self.d.click(500, 1240)
            self.d.click(500, 1240)

            self.d(text='安全').wait()
            self.d(text='安全').click()
            self.d(text='密码设置').wait()
            self.d(text='密码设置').click()
            self.d(text='修改支付密码').wait()
            self.d(text='修改支付密码').click()
            self.d(text='请输入当前支付密码').wait()
            self.d(text='请输入当前支付密码').click()
            self.d.send_keys(text='000000')
            self.d(text='请输入新支付密码, 6位数字组成').click()
            self.d.send_keys(text='000000')
            self.d(text='保存').click()
            assertappear(name='重设支付密码',expect=True,actual=self.d(text='密码已重设').wait())
            self.d(text='返回').click()
            self.Back_uplevel()
            self.d.click(200,1240)
            self.d.click(200,1240)
            self.d.click(200,1240)
            #优化一下
            self.d(text='转账').click()
            print(self.d(text='转账').wait())
            assertappear(name='进入转账页面', expect=self.d(text='转账').get_text(), actual='转账')
            self.d(text='常用联系人').click()
            assertappear(name='进入常用联系人', expect=self.d(text='常用联系人').get_text(), actual='常用联系人')
            self.d.click(50, 180)
            self.d(text='下一步').click()
            self.d(text='转账金额').click()
            self.d.send_keys('1')
            self.d(text='货币切换').click()
            assertappear(name='转账货币切换', expect=self.d(text='CNY').get_text(), actual='CNY')
            self.d(text='下一步').click()
            self.d(text='立即付款').click()
            # 分支补充忘记支付密码
            self.d.send_keys(text='000000')
            assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
            self.d(text='返回').click()
            self.d.click(500, 1240)
            self.d.click(500, 1240)
            self.d.click(500, 1240)
            #
            # """
            # """
            # self.d(text='')
            # self.d(text='')
            # self.d(text='')
            # self.d(text='')





        def personal2(self,version):
            self.d.click(500, 1240)
            self.d.click(500, 1240)
            self.d.click(500, 1240)
            """
            设置
            """
            self.d(text='设置').click()
            self.d(text='语言\n简体中文').click()

            self.d(text='English').click()
            self.Back_uplevel()
            t=self.d(text='Settings').wait()
            assertappear(name='英文设置',expect=True,actual=t)
            self.d(text='Language\nEnglish').click()

            self.d(text='简体中文').click()
            self.Back_uplevel()
            self.d(text='计价货币\n人民币 (CNY)').click()
            self.d(text='美元 (USD)').click()
            self.d(text='比索 (PHP)').click()
            self.d(text='港币 (HKD)').click()
            self.Back_uplevel()
            self.Back_uplevel()

            """
            常见问题
            """

            self.d(text='常见问题').wait()
            self.d(text='常见问题').click()
            self.d(text='小金库收款').click()
            self.d(text='如何收款?').click()
            self.d(description='转到上一层级').click()
            self.d(description='转到上一层级').click()
            self.d(description='转到上一层级').click()

            """
            我的客服
            """
            self.d(text='我的客服').wait()
            self.d(text='我的客服').click()
            t=self.d(text='小金库客户支援').wait()
            assertappear(name='进入客服页面',expect=True,actual=t)

            self.d(text='Type a message').click()
            self.d.send_keys('你好')
            self.d(resourceId='com.speedstae.dcbox:id/freshchat_conv_detail_send_reply_button').click()
            d=self.d(text='你好').wait()
            assertappear(name='客服对话',actual=d,expect=True)
            self.d(description='转到上一层级').click()


            """
            版本检查
            """
            self.d(text='检查版本\n%s'%version).wait()
            self.d(text='检查版本\n%s'%version).click()

            if self.d(text='当前已经是最新版本').wait():
                print(True,'这是最新版本%s'%version)
                self.d(text='确定').click()
            else:
                pass
                #补充在线升级


            self.d.click(200, 163)
            self.d.click(200, 163)
            self.d(text='登出').wait()
            self.d(text='登出').click()








        def logout(self):
            self.d(text='收款').wait()
            self.d(text='我的\n第 2 个标签，共 2 个').click()
            # self.d.click(500, 1240)
            self.d(text='常用联系人').wait()
            # self.d.click(200,163)
            self.d(text='我的\n昵称:880\n金库号:\000WA564777')
            self.d(text='登出').wait()
            self.d(text='登出').click()
            #补充成功登出断言

        def switch_acount(self):
            """
            切换账户，验证码登录
            """
            self.d.clear_text()
            self.d.send_keys(text='177890')
            self.d(text="下一步").click()
            self.d.sleep(2)
            self.d.send_keys(text='000')
            self.d.sleep(1)
            self.d.send_keys(text='000')



        def tear_down(self):
            self.d.app_clear('com.speedstae.dcbox')
            self.d.uiautomator.stop()
            self.d.app_stop_all()



if __name__ == '__main__':
    IP='127.0.0.1:21503'
    # IP='emulator-5554'
    # IP='D0AA002219J90702603'
    d=dcboxtest(IP)
    d.inittest()

    number='177880'
    d.cilcklogin()
    # d.verifycode_login(number)
    # d.logout()
    #
    # d.cilcklogin()
    # d.password_login()
    # d.logout()
    #
    # d.cilcklogin()
    # d.forget_passwd()
    # d.password_login()
    # #
    # #
    # d.check_homepage()
    # d.received_payment()
    # # #
    # d.transfer()
    # d.personal1()
    # v='3.1.17.198'
    # d.personal2(version=v)



    d.tear_down()


