import uiautomator2 as ui2
import os,time
from uiautomator2 import Direction




class ProScript:
    def __init__(self,IP):
        device=ui2.connect(IP)
        self.d=device
        # self.d.implicitly_wait(60)
        print(self.d.info)
        print(self.d.window_size())
        # self.d.watcher('')
    def install(phone,ve):
        d = os.popen(cmd='adb shell pm list packages')
        r = d.read()
        if 'com.speedstae.dcbox' in r:
            os.popen(cmd='adb uninstall com.speedstae.dcbox')
            print('清空安装过的包')
            time.sleep(2)

        else:
            print('没有发现已安装的包')
        print('安装')
        os.popen(cmd=r'adb install C:\Users\janti\Downloads\%s'%ve)
        print('安装中。。。')
        phone.d.wait_activity('com.speedstae.dcbox.MainActivity')
        print('安装结束')
        os.popen(cmd=r'adb shell am start  com.speedstae.dcbox/com.speedstae.dcbox.MainActivity ')
        print('启动app')

        phone.d.app_wait('com.speedstae.dcbox')
        print('app已启动，立即进入')
        try:
            phone.d(text="立即进入").click()
            print('第一次登录')
            phone.c = 1
        except:
            pass

        os.popen('adb shell pm grant com.speedstae.dcbox android.permission.READ_EXTERNAL_STORAGE')

    def click_login(self):
        self.d(text='钱包余额 (USDT)\n点击登入\n账单 登录后查看').click()

    def Back_uplevel(self):
        self.d(text='Back').click()
    def first_passwd_login(self,phnoenumber):
        self.d(text='密码登录').click()

        self.d(text='请输入你的手机号码').click()
        self.d.send_keys(phnoenumber)
        self.d(text='+86').click()
        self.d(text='搜索').click()
        self.d.send_keys('63')
        self.d.press('enter')
        self.d(text='+63\n菲律宾').click()
        self.d(text='请输入密码').click()
        self.d.send_keys(text='a1111111')
        self.d(text='登录').click()
        #第一次登录需要验证码
        if self.c==1:
            self.d(text='获取验证码').click()
        else:
            pass
        #build 考虑输入错误
        for i in range(3):
            c = input('请手动输入验证码，并按回车键确认:')
            if len(c)==6:
                self.d(text='请输入验证码').click()
                self.d.send_keys(c)
                self.d(text='登录').click()



                break
            elif len(c)!=6 and 2-i>0:
                print('请输入完整的验证码，剩余次数:%d'%(2-i))
            elif 2-i==0:
                print('3次机会用完了,请重新启动脚本')
                break

        if self.d(text='收款').wait()==True:
            print('登录成功')

        else:
            print('登录失败，卸载应用')
            os.popen(cmd='adb uninstall com.speedstae.dcbox')
    def pawd_login(self):
        self.d(text='密码登录').click()
        self.d(text='请输入密码').click()
        self.d.send_keys(text='a1111111')
        self.d(text='登录').click()
        if self.d(text='收款').wait() == True:
            print('密码登录成功')

        else:
            self.d.screenshot('./passlogin_fail.png')
            pass
    def verify_login(self):

        # print(self.d.watch_context().)
        print('------------')
        print(self.d(text='下一步').get_text())
        self.d(text='下一步').click(timeout=10)
        v=input('手动输入验证码:')
        self.d.send_keys(v)
        if self.d(text='收款').wait()==True:
            print('验证码登录成功')

        else:
            self.d.screenshot('./verifylogin_fail.png')
            pass
    def forgot_pswd(self):
        self.d(text='密码登录').click()
        self.d(text='忘记密码').click()
        self.d(text='获取验证码').click()
        self.d(text='请输入验证码').click()
        v=input('请输入验证码:')
        self.d.send_keys(v)
        self.d(text='提交').click()
        self.d(text='请输入您的新密码').click()
        self.d.send_keys('a1111111')
        self.d(text='请再次输入您的新密码').click()
        self.d.send_keys('a1111111')
        self.d(text='提交').click()
        self.d(text='登录').click()
        self.pawd_login()


    def logout(self):
        self.d(text='我的\n第 2 个标签，共 2 个').click()
        print(type(self.d.window_size()))
        size=self.d.window_size()
        width=0.16*size[0]
        height=0.16*size[1]
        self.d.click(width,height)
        print(self.d(text='登出').wait())
        self.d(text='登出').click()
        if self.d(text='注册').wait() == True:
            print('登出成功')
        else:
            print('登出失败')
        # try:
        #  self.d(text='登出').click()
        #  self.d(text='登出').click()
        #  self.d(text='登出').click()
        #  if self.d(text='注册').wait()==True:
        #     print('登出成功')
        #  else:
        #     print('登出失败')
        # except:
        #     self.d(text='登出').click()
        #     print('第一次登出失败，再次执行登出')
    def receiver(self):
        self.d(text='收款').click()
        # self.assertappear(name='进入收款界面', actual=self.d(text='选择币种').get_text(), expect='选择币种')

        self.d(text='保存收款码').click()
        self.assertappear(name='保存收款码', actual=self.d.toast.get_message(), expect='保存成功')

        self.Back_uplevel()

    def transfer(self):
        """
         常用联系人转账
                    """
        self.d(text='转账').click()
        print(self.d(text='转账').wait())
        self.assertappear(name='进入转账页面', expect=self.d(text='转账').get_text(), actual='转账')
        self.d(text='常用联系人').click()
        self.d.xpath('//android.view.View/android.view.View[2]/android.widget.ImageView[1]').click()

        self.d(text='下一步').click()
        self.d(text='转账金额').click()
        self.d.send_keys('1')
        self.d(text='货币切换').click()
        #需要传入当前计价货币参数
        #传参
        self.assertappear(name='转账货币切换', expect=self.d(text='PHP').get_text(), actual='PHP')
        self.d(text='下一步').click()
        self.d(text='立即付款').click()
        # 分支补充忘记支付密码
        self.d.send_keys(text='000000')
        self.assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
        self.d(text='返回').click()

        """
        直接输入金库号转账
        """
        self.d(text='转账').click()
        self.d.send_keys(text='VM636547')
        self.d(text='下一步').click()
        self.d(text='转账金额').click()
        self.d.send_keys('1')
        self.d(text='货币切换').click()
        self.assertappear(name='转账货币切换', expect=self.d(text='PHP').get_text(), actual='PHP')
        self.d(text='下一步').click()
        self.d(text='立即付款').click()
        # 分支补充忘记支付密码
        self.d.send_keys(text='000000')
        self.assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
        self.d(text='返回').click()

        """
                    链上地址转账
                    """
        self.d(text='转账').click()
        # self.d.send_keys(text='0xCa7B7887522BF4dB10c9F9646FC326483779017c')#880
        self.d.send_keys(text='0x9565E9eCB64338B0cb98950A229ab33A83dB9D0c')  # 7627
        self.d(text='下一步').click()
        self.d(text='转账金额').click()
        self.d.send_keys('1')
        self.d(text='货币切换').click()
        self.assertappear(name='转账货币切换', expect=self.d(text='PHP').get_text(), actual='PHP')
        self.d(text='下一步').click()
        self.d(text='立即付款').click()
        # 分支补充忘记支付密码
        self.d.send_keys(text='000000')
        self.assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
        self.d(text='返回').click()

    def personal1(self,friendnumber):
        """

        更换头像
        :return:
        """
        self.d(text='收款').wait()
        self.d(text='我的\n第 2 个标签，共 2 个').click() # 逍遥模拟器
        # self.d.click(0.737, 0.897)#nokia
        self.d(text='常用联系人').wait()
        #点击首个
        size = self.d.window_size()
        width = 0.16 * size[0]
        height = 0.16 * size[1]
        self.d.click(width, height)

        self.d(text='更改个人头像').wait()
        #头像中心点
        self.d.xpath("//android.widget.FrameLayout/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]").click()
        self.d.press('BACK')






        """
        昵称修改
        """
        self.d(text='登出').wait()
        self.d(text='昵称\n90295').click()
        self.d(text='90295, 请输入昵称').click()
        self.d(text='确定').click()
        self.Back_uplevel()

        """
        常用联系人
        """
        self.d(text="常用联系人").wait()
        self.d(text='常用联系人').click()

        if self.d(text='没有联系人').wait(timeout=5) == True:
            """
            金库号添加好友
            """

            #添加好友小控件
            self.d(className='android.widget.ImageView',instance=1).click()
            size = self.d.window_size()
            width = 0.25 * size[0]
            height = 0.25 * size[1]
            print(int(width),int(height))
            self.d.click(int(width),int(height))
            self.d.click(int(width),int(height))
            # self.d(className='android.widget.EditText',instance=0).send_keys(text='VM636547')
            # self.d.click(106, 208)
            self.d.send_keys(text='VM636547')
            # self.d(focused=True).set_text('VM636547')
            self.d(text='确定').click()

            """
            删除第一个好友
            """
            print(self.d(text='最近').wait())
            self.d(className='android.widget.ImageView',instance=3).click()
            # self.d.click(100, 180)
            # self.d.click(100, 180)
            # self.d.click(100, 180)
            # self.d.click(100, 180)
            # self.d.click(100, 180)
            # self.d.click(100, 180)
            self.d(text='删除').wait()
            self.d(text='删除').click()
            self.d(text='常用联系人').wait()
            """
            手机号添加好友
            """
            self.d(className='android.widget.ImageView',instance=1).click()
            self.d(text='添加联系人').wait()
            self.d.swipe(fx=500, fy=500, tx=100, ty=500)

            # self.d(text='手机号码').click()
            self.d(text='请输入手机号码').click(timeout=2)
            # self.d.click(106, 208)
            self.d.send_keys(text=friendnumber)
            self.d(text='+86').click()
            self.d(text='搜索').click()
            self.d.send_keys('63')
            self.d.press('enter')
            self.d(text='+63\n菲律宾').click()
            self.d(text='确定').click()
            self.Back_uplevel()
        elif self.d(text='没有联系人').wait(timeout=5) == False:

            """
                                                删除第一个好友
                                                """
            self.d.xpath('//android.view.View/android.view.View[2]/android.widget.ImageView[1]').click()
            self.d(text='删除').wait()
            self.d(text='删除').click()
            # self.d(text="常用联系人").wait()

            """
                            添加好友
                            """
            self.d(text="没有联系人").wait()
            self.d.xpath('//android.view.View/android.widget.ImageView[2]').click()
            self.d.click(680, 50)
            self.d.click(680, 50)
            self.d.click(680, 50)

            width = 0.25 * size[0]
            height = 0.25 * size[1]
            print(int(width), int(height))
            self.d.click(int(width), int(height))
            self.d.click(int(width), int(height))
            # self.d(text='请输入金库号').click(timeout=2)
            # self.d.click(106, 208)
            self.d.send_keys(text='VM636547')
            self.d(text='确定').click()
            self.d(text='常用联系人').wait()
            self.Back_uplevel()

        """
        消息通知
        """
        self.d(text='消息通知').click()
        self.d(text='消息通知').wait()
        # asserNOTexception(actual=self.d.toast.get_message(), expect='', name='消息通知页面')
        self.Back_uplevel()

        """
        安全

        修改登录密码
        """
        self.d(text='安全').click()
        self.d(text='密码设置').wait()
        self.d(text='密码设置').click()
        self.d(text='修改登陆密码').wait(timeout=5)
        self.d(text='修改登录密码').click()
        self.d(text='请输入当前登录密码').wait()
        self.d(text='请输入当前登录密码').click()
        self.d.send_keys(text='a1111111')
        self.d(text='请输入新登录密码').click()
        self.d.send_keys(text='a1111111')
        self.d(text='提交').click()
        self.assertappear(name='修改登录密码', actual=self.d(text='密码已重设').wait(), expect=True)
        self.d(text='返回').click()
        self.d(text='密码设置').wait()
        self.Back_uplevel()

        self.d(text='常用联系人').wait()
        size = self.d.window_size()
        width = 0.16 * size[0]
        height = 0.16 * size[1]
        self.d.click(width, height)
        self.d.click(width, height)
        self.d(text='登出').wait()
        self.d(text='登出').click()
        self.pawd_login()


        self.assertappear(name='验证码登录', actual=self.d(text='收款').get_text(), expect='收款')

        """
        修改支付密码
        """
        print(self.d(text='收款').wait())
        self.d(text='我的\n第 2 个标签，共 2 个').click()

        print(self.d(text='安全').get_text())
        print(self.d(text='安全').exists)
        try:
           self.d(text='安全').click()
        except:
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

        if self.d.toast.get_message()!=None:
           totast = self.d.toast.get_message()
           self.assertappear(name='重设支付密码', expect='', actual=totast)
        else:
            self.assertappear(name='重设支付密码', expect=True, actual=self.d(text='密码已重设').wait())

        """"
        以下未调试，遇到bug：修改支付密码失败
        """
        self.d(text='返回').click()
        self.d(text="密码设置").wait()
        self.Back_uplevel()
        self.d(text='首页\n第 1 个标签，共 2 个').click()
        # 优化一下
        self.d(text='转账').click()
        print(self.d(text='转账').wait())
        self.assertappear(name='进入转账页面', expect=self.d(text='转账').get_text(), actual='转账')
        self.d(text='常用联系人').click()
        self.assertappear(name='进入常用联系人', expect=self.d(text='常用联系人').get_text(), actual='常用联系人')
        self.d.xpath('//android.view.View/android.view.View[2]/android.widget.ImageView[1]').click()

        self.d(text='下一步').click()
        self.d(text='转账金额').click()
        self.d.send_keys('1')
        self.d(text='货币切换').click()
        self.assertappear(name='转账货币切换', expect=self.d(text='PHP').get_text(), actual='PHP')
        self.d(text='下一步').click()
        self.d(text='立即付款').click()
        # 分支补充忘记支付密码
        self.d.send_keys(text='000000')
        self.assertappear(name='进入转账成功页面', expect=self.d(text='已经成功转账').get_text(), actual='已经成功转账')
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

    def personal2(self, version):
        self.d(text='我的\n第 2 个标签，共 2 个').click()
        """
        设置
        """
        self.d(text='设置').click()
        self.d(text='语言\n简体中文').click()

        self.d(text='English').click()
        self.d(text='Language').wait()
        self.Back_uplevel()

        t = self.d(text='Settings').wait()
        # assertappear(name='英文设置', expect=True, actual=t)
        self.d(text='Language\nEnglish').click()

        self.d(text='简体中文').click()
        self.d(text='语言').wait()
        self.Back_uplevel()

        self.d(text='计价货币\n港币 (HKD)').click()
        self.d(text='美元 (USD)').click()
        self.d(text='比索 (PHP)').click()
        self.d(text='港币 (HKD)').click()
        self.Back_uplevel()
        self.Back_uplevel()

        """
        常见问题
        """
        print('常见问题')
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
        # self.d(text='我的客服').wait()
        # self.d(text='我的客服').click()
        # t = self.d(text='小金库客户支援').wait()
        # # assertappear(name='进入客服页面', expect=True, actual=t)
        #
        # self.d(text='Type a message').click()
        # self.d.send_keys('你好')
        # self.d(resourceId='com.speedstae.dcbox:id/freshchat_conv_detail_send_reply_button').click()
        # d = self.d(text='你好').wait()
        # # assertappear(name='客服对话', actual=d, expect=True)
        # self.d(description='转到上一层级').click()

        """
        版本检查
        """
        print('检查版本')
        self.d.swipe(fx=200,fy=900,tx=200,ty=400,duration=1)
        self.d.drag(sx=200,sy=900,ex=200,ey=400,duration=1)
        self.d(text='检查版本\n%s' % version).wait()
        self.d(text='检查版本\n%s' % version).click()

        if self.d(text='当前已是最新版本').wait():

            self.d(text='确定').click()
        else:
            pass
            # 补充在线升级

    def assertappear(self,name, actual, expect):
        if actual == expect:
            print("%s成功" % name)
        else:
            print('%s失败' % name)

def main():

        # se=expr.device_detect()
        # se = '127.0.0.1:21503'
        se = 'YGC6R19122004060'
        pack='dcbox-3.1.19.203.apk'
        ph='9618990295'
        friendnum = '9155837627'
        ps = ProScript(IP=se)
        ps.install(ve=pack)
        ps.click_login()
        ps.first_passwd_login(phnoenumber=ph)
        ps.logout()
        ps.verify_login()
        ps.logout()
        ps.forgot_pswd()
        ps.pawd_login()
        ps.receiver()
        ps.transfer()
        ps.personal1(friendnumber=friendnum)
        ve = '3.1.17.203'
        ps.personal2(version=ve)
if __name__ == '__main__':
    # d = os.popen('adb devices')
    # dev = d.read()

    # seril = dev.split(' ')[3].split('\n')[1].split('\t')[0]
    # s=input('请输入设备地址:%s'%seril)

    se = 'YGC6R19122004060'
    pack = 'dcbox-3.1.19.203.apk'
    ph = '9618990295'
    friendnum='9155837627'
    ps = ProScript(IP=se)
    #卸载和安装
    ps.install(ve=pack)
    #首次登录
    ps.click_login()
    ps.first_passwd_login(phnoenumber=ph)
    ps.logout()

    #验证码登录
    ps.verify_login()
    ps.logout()


    #忘记密码
    ps.forgot_pswd()
    ps.pawd_login()
    #收款转账
    ps.receiver()
    ps.transfer()
    #我的
    ps.personal1(friendnum)
    ve = '3.1.19.203'
    ps.personal2(version=ve)