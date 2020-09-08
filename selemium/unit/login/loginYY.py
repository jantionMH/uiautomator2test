import unittest,time,random,os,sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from unittest import TestCase
from HTMLTestRunner import HTMLTestRunner
class Unittest01(unittest.TestCase):
    """"
    1.setup 跟进到彩票页面
    2.时时彩-A
    3.十一选五 -B  以此类推
    4.五星玩法-5star
    """
    drvierpath = r"C:\Users\janti\driver\geckodriver-v0.26.0-win64\geckodriver.exe"
    driver = webdriver.Firefox(executable_path=drvierpath)
    driver.maximize_window()

    now = time.strftime("%Y%m%d-%H_%M_%S_", time.localtime(time.time()))
    filepath = r'C:\Users\janti\PycharmProjects\YYtestUI\unit\result\screenpicture\%s'%now+'.png'

    @classmethod
    def setUpClass(self) :


        # 登录操作
        self.driver.get("http://miletest.com/")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@id='app']/section/div/div/div/div[2]/div[5]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//img[@alt='img'])[10]").click()
        time.sleep(3)
        #输入用户名
        # wc.find_element_by_css_selector("input.el-input__inner").click()
        # wc.find_element_by_css_selector("input.el-input__inner").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        self.driver.find_element_by_css_selector("input.el-input__inner").send_keys("jantion001")
        time.sleep(1)
        #输入密码
        self.driver.find_element_by_css_selector("div.seek-top-password-input.el-input > input.el-input__inner").click()
        self.driver.find_element_by_css_selector("div.seek-top-password-input.el-input > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.seek-top-password-input.el-input > input.el-input__inner").send_keys("jantion001")
        #登录
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(5)

        #点击广告
        self.driver.find_element_by_css_selector(
            "#app > section > div.el-dialog__wrapper.global-activity > div > div.el-dialog__body > div.global-activity__main > div.comfirm-btn").click()
        # self.assertTrue((self.is_element_present(By.XPATH,"//ul/div/li/span")))
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='app']/section/div/div/div/div[2]/div[5]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//img[@alt='img'])[10]").click()

        k = self.driver.find_element_by_css_selector('img[title="M6体育"]')
        ActionChains(self.driver).move_to_element(k).perform()
        time.sleep(7)

        # self.driver.switch_to.frame('iframe')
        # 登出

    @classmethod
    def tearDownClass(self):

        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollBy(0,0)")
        time.sleep(1)
        Avtor = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div[1]/div/div[2]/div/div[4]/div/div[1]/div/div/img")
        ActionChains(self.driver).move_to_element(Avtor).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("//ul/div/li/span").click()

    def testA01(self):

        self.driver.switch_to.frame('iframe')

        self.driver.find_element_by_xpath("//div[@id='']").click()

        self.driver.find_element_by_xpath("(//div[@id=''])[12]").click()
        self.driver.find_element_by_xpath("(//div[@id=''])[23]").click()
        self.driver.find_element_by_xpath("(//div[@id=''])[35]").click()
        self.driver.find_element_by_xpath("(//div[@id=''])[46]").click()
        self.betinto()
        self.driver.get_screenshot_as_file(filename=Unittest01.filepath)
        print('C:\\Users\\janti\\PycharmProjects\\webselemium\\unit\\result\\screenpicture')


    def testA02(self):
        # 五星组合
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[2]/div[3]").click()
        time.sleep(1)
        # 选号
        # 万
        self.driver.find_element_by_xpath("(//div[@id=''])[3]").click()
        # 千
        self.driver.find_element_by_xpath("(//div[@id=''])[20]").click()
        # 百
        self.driver.find_element_by_xpath("(//div[@id=''])[21]").click()
        # 十
        self.driver.find_element_by_xpath("(//div[@id=''])[31]").click()
        # 个
        self.driver.find_element_by_xpath("(//div[@id=''])[50]").click()
        self.betinto()
    def testA03(self):

        time.sleep(2)
        # 组选60
        self.driver.find_element_by_xpath("//div[2]/div[2]/div[2]").click()
        time.sleep(1)
        # 选号
        self.driver.find_element_by_xpath("(//div[@id=''])[5]").click()
        self.driver.find_element_by_xpath("(//div[@id=''])[14]").click()
        self.driver.find_element_by_xpath("(//div[@id=''])[16]").click()
        self.driver.find_element_by_xpath("(//div[@id=''])[17]").click()
        self.betinto()


    def testA04(self):
        r = random.randint(2, 3)
        time.sleep(2)

        # 龙虎和
        self.driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        time.sleep(1)
        # 选字
        self.driver.find_element_by_xpath("(//div[@id=''])[%d]"%r) .click()
        self.betinto()
    def is_element_present(self,how,what):
        try : self.driver.find_element(how,what)
        except NoSuchElementException : return False
        return True

    def betinto(self):
        self.driver.execute_script("window.scrollBy(0,400)")
        self.driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

        time.sleep(1)
        self.driver.find_element_by_css_selector("button.el-button.bet-confirm-btn.el-button--primary").click()
        # self.wc.switch_to.alert.accept()
        time.sleep(2)
        self.driver.find_element_by_css_selector("i.el-message-box__close.el-icon-close").click()

if __name__=="__main__":
    unittest.main()


    # now=time.strftime("%Y%m%d-%H_%M_%S_",time.localtime(time.time()))
    # print(now)
    # filepath='C:\\Users\\janti\\PycharmProjects\\webselemium\\unit'+now+'report.html'
    # with open(file=filepath,mode='wb') as f:
    #    runner=HTMLTestRunner(stream=f,title='UI测试报告',description='测试用例执行情况')
    #    runner.run(testsuit)