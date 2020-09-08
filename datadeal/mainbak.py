import unittest
from dcbox198appium import androidConnectAppium, backto_previous, clicklogin, logout,getxy
import os, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = androidConnectAppium()

        cls.driver.implicitly_wait(90)
        os.popen('adb shell pm grant com.speedstae.dcbox android.permission.READ_EXTERNAL_STORAGE')
    # def test01_coverinstall(self):

    # print(self.driver.find_element_by_xpath("//android.view.View[@text='立即进入']").get_property('id'))

    def test02_firstlogin(self):

        if self.driver.find_element_by_xpath("//android.view.View[@text='立即进入']").is_displayed():
            self.driver.find_element_by_xpath("//android.view.View[@text='立即进入']").click()
            print('第一次执行')
        else:
            print('不是第一次')
        clicklogin(self)

    def test03_enteruat(self):
        self.driver.find_element_by_class_name('android.widget.Button').click()
        for i in range(15):
            self.driver.find_element_by_xpath("//android.view.View[@text='钱包']").click()

        backto_previous(self)
        backto_previous(self)
        clicklogin(self)

        # print(self.driver.find_elements_by_class_name('android.view.View').count())

        # self.driver.execute()
        # self.close()

    #     pass
    #
    def test04_verifylogin(self):
        self.driver.find_element_by_class_name('android.widget.EditText').click()
        self.driver.press_keycode('8')
        self.driver.press_keycode('14')
        self.driver.press_keycode('14')
        self.driver.press_keycode('15')
        self.driver.press_keycode('15')
        self.driver.press_keycode('7')
        # self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入你的手机号码']")
        self.driver.find_elements_by_class_name('android.widget.Button')[1].click()
        if self.driver.find_element_by_xpath("//android.view.View[@text='请查看短信并输入验证码']").get_attribute(
                'text') == '请查看短信并输入验证码':
            # self.driver.set_value('000000')
            self.driver.press_keycode('7')
            self.driver.press_keycode('7')
            self.driver.press_keycode('7')
            self.driver.press_keycode('7')
            self.driver.press_keycode('7')
            self.driver.press_keycode('7')
        else:
            print('还没进入输入页面')
        logout(self)

    def test05_passwdlogin(self):
        time.sleep(1)
        print(self.driver.find_elements_by_class_name('android.view.View'))
        print(self.driver.find_elements_by_class_name('android.view.View')[0].get_attribute('text'))
        self.driver.find_element_by_xpath("//android.view.View[@text='密码登录']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入密码']").click()
        self.driver.press_keycode('29')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        logout(self)
        # print(self.driver.find_elements_by_class_name('android.widget.Button').count())

    #
    def test06_forgetpasswd(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.view.View[@text='密码登录']").click()
        self.driver.find_element_by_xpath("//android.view.View[@text='忘记密码']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入验证码']").click()
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入您的新密码']").click()
        self.driver.press_keycode('29')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请再次输入您的新密码']").click()
        self.driver.press_keycode('29')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        try:
           print(self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").get_attribute('text'))
           self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        except:
            self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()

        self.driver.find_element_by_xpath("//android.view.View[@text='密码登录']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入密码']").click()
        self.driver.press_keycode('29')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()

    def test07_receive(self):
        self.driver.find_element_by_xpath("//android.view.View[@text='收款']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='USDT']").click()
        self.driver.find_element_by_xpath("//android.view.View[@text='保存收款码']").click()
        print(len(self.driver.find_elements_by_class_name("android.view.View")))
        self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.View[7]").click()
        backto_previous(self)
        backto_previous(self)

    def get_toast_text(self, text, timeout=5, poll_frequency=0.01):
        """
        ########################################
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        ########################################
        """
        toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
        toast = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_element))
        return toast.text

    def test08_transfer_Ec20(self):
        self.driver.find_element_by_xpath("//android.view.View[@text='转账']").click()
        self.driver.find_element_by_class_name("android.widget.EditText").click()#输入框
        self.getEC20keycode()
        self.driver.find_element_by_class_name("android.widget.Button").click()#下一步
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='转账金额']").click()
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='货币切换']").click()
        self.driver.find_element_by_class_name("android.widget.Button").click()  # 下一步
        self.driver.find_element_by_xpath("//android.widget.Button[@text='立即付款']").click()
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='返回']").click()
        # self.driver.find_element_by_xpath("//android.view.View[@text='忘记支付密码']").click()

        #
        # self.driver.find_element_by_class_name("android.widget.Button").click()#下一步
        #
    def test09_transfer_id(self):
        self.driver.find_element_by_xpath("//android.view.View[@text='转账']").click()
        for i  in range(45):

           self.driver.press_keycode('67')
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='对方账号\n请输入金库号或Erc20资产地址']").click()
        self.driver.press_keycode('47',metastate=1)
        self.driver.press_keycode('41',metastate=1)
        self.driver.press_keycode('16')
        self.driver.press_keycode('7')
        self.driver.press_keycode('8')
        self.driver.press_keycode('16')
        self.driver.press_keycode('15')
        self.driver.press_keycode('15')
        self.driver.find_element_by_class_name("android.widget.Button").click()  # 下一步

        self.driver.find_element_by_xpath("//android.widget.EditText[@text='转账金额']").click()
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='货币切换']").click()
        self.driver.find_element_by_class_name("android.widget.Button").click()  # 下一步
        self.driver.find_element_by_xpath("//android.widget.Button[@text='立即付款']").click()
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='返回']").click()
    def test10_transfer_contrace(self):
        self.driver.find_element_by_xpath("//android.view.View[@text='转账']").click()
        self.driver.find_element_by_xpath("//android.view.View[@text='常用联系人']").click()  # 常用联系人
        self.driver.find_element_by_class_name("android.widget.ImageView").click()  # 第一个联系人
        self.driver.find_element_by_class_name("android.widget.Button").click()  # 下一步
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='转账金额']").click()

        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='货币切换']").click()
        self.driver.find_element_by_class_name("android.widget.Button").click()  # 下一步
        self.driver.find_element_by_xpath("//android.widget.Button[@text='立即付款']").click()
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='返回']").click()


    def test11_personal1(self):
        self.driver.find_element_by_xpath("//android.view.View[@text='我的\n第 2 个标签，共 2 个']").click()
        getxy(self)
        print(self.driver.find_elements_by_class_name('android.widget.ImageView'))
        self.driver.find_elements_by_class_name('android.widget.ImageView')[1].click()
        self.driver.find_element_by_xpath("//android.view.View[@text='本地相册']").click()
        self.driver.press_keycode('4')
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='昵称\n880']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='880, 请输入昵称']").click()
        self.driver.press_keycode('67')
        self.driver.press_keycode('7')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='确定']").click()
        backto_previous(self)
    def test12_announcement(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='消息通知']").click()
        backto_previous(self)

    def test13_resetpw(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='安全']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='密码设置']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='修改登录密码']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入当前登录密码']").click()
        self.driver.press_keycode('29')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')

        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入新登录密码']").click()
        self.driver.press_keycode('29')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.press_keycode('8')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='提交']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text='返回']").click()

    def test14_restpament(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='密码设置']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='修改支付密码']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入当前支付密码']").click()
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')
        self.driver.press_keycode('7')

        self.driver.find_element_by_xpath("//android.widget.EditText[@text='请输入新支付密码, 6位数字组成']").click()
        self.driver.press_keycode("7")
        self.driver.press_keycode("7")
        self.driver.press_keycode("7")
        self.driver.press_keycode("7")
        self.driver.press_keycode("7")
        self.driver.press_keycode("7")
        self.driver.find_element_by_xpath("//android.widget.Button[@text='保存']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text='返回']").click()
        backto_previous(self)
    def test15_set(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='设置']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='语言\n简体中文']").click()
        self.driver.find_element_by_xpath("//android.view.View[@text='English']").click()
        backto_previous(self)
        backto_previous(self)
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='Settings']").click()
        self.driver.find_element_by_xpath("//android.widget.ImageView[@text='Language\nEnglish']").click()
        self.driver.find_element_by_xpath("//android.view.View[@text='简体中文']").click()
        backto_previous(self)
        backto_previous(self)

    def getEC20keycode(self):

        self.driver.press_keycode('7')
        self.driver.press_keycode('52')
        self.driver.press_keycode('14')
        self.driver.press_keycode('32',metastate=1)
        self.driver.press_keycode('33')
        self.driver.press_keycode('14')
        self.driver.press_keycode('34')
        self.driver.press_keycode('30')
        self.driver.press_keycode('12')
        self.driver.press_keycode('12')
        self.driver.press_keycode('29',metastate=1)
        self.driver.press_keycode('11')
        self.driver.press_keycode('9')
        self.driver.press_keycode('32',metastate=1)
        self.driver.press_keycode('32',metastate=1)
        self.driver.press_keycode('34')
        self.driver.press_keycode('9')
        self.driver.press_keycode('31')
        self.driver.press_keycode('15')
        self.driver.press_keycode('29',metastate=1)
        self.driver.press_keycode('34',metastate=1)
        self.driver.press_keycode('32')
        self.driver.press_keycode('10')
        self.driver.press_keycode('33')
        self.driver.press_keycode('12')
        self.driver.press_keycode('14')
        self.driver.press_keycode('9')
        self.driver.press_keycode('14')
        self.driver.press_keycode('34')
        self.driver.press_keycode('33')
        self.driver.press_keycode('12')
        self.driver.press_keycode('14')
        self.driver.press_keycode('16')
        self.driver.press_keycode('31',metastate=1)
        self.driver.press_keycode('33')
        self.driver.press_keycode('30',metastate=1)
        self.driver.press_keycode('34',metastate=1)
        self.driver.press_keycode('15')
        self.driver.press_keycode('16')
        self.driver.press_keycode('33')
        self.driver.press_keycode('29')
        self.driver.press_keycode('31')


    def close(self):
        self.driver.close_app()


    @classmethod
    def tearDownClass(cls):

        pass


if __name__ == '__main__':
    unittest.main()
