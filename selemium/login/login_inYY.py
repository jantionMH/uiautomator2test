import websocket,requests,os,time,random
from selenium import webdriver
from selenium.webdriver import ActionChains
# os.system('taskkill /F /IM Chorme.exe')
class Login:
    def __init__(self):
        # drvierpath=r"C:\Users\janti\driver\chromedriver.exe" # 81.0.4044
        drvierpath=r"C:\Users\janti\driver\geckodriver-v0.26.0-win64\geckodriver.exe"
        self.wc=webdriver.Firefox(executable_path=drvierpath)

    def dologin(self):
        #打开平台
        self.wc.maximize_window()
        self.wc.get("http://miletest.com/home")
        time.sleep(5)
        self.wc.find_element_by_xpath("//div[5]/span").click()
        time.sleep(1)
        self.wc.find_element_by_xpath("(//img[@alt='img'])[10]").click()

        #输入用户名
        # self.wc.find_element_by_css_selector("input.el-input__inner").click()
        # self.wc.find_element_by_css_selector("input.el-input__inner").clear()
        self.wc.find_element_by_xpath("(//input[@type='text'])[2]").click()
        self.wc.find_element_by_css_selector("input.el-input__inner").send_keys("jantion001")
        time.sleep(1)
        #输入密码
        self.wc.find_element_by_css_selector("div.seek-top-password-input.el-input > input.el-input__inner").click()
        # self.wc.find_element_by_css_selector("div.seek-top-password-input.el-input > input.el-input__inner").clear()
        self.wc.find_element_by_css_selector("div.seek-top-password-input.el-input > input.el-input__inner").send_keys("jantion001")

        #登录
        time.sleep(2)

        # self.wc.find_element_by_xpath("//div[4]/button").click()
        print(self.wc.find_element_by_css_selector("button.el-button.login-register-container__submit.el-button--primary.main-button.main-button--big").click())
        #点击小广告
        time.sleep(2)
        self.wc.find_element_by_css_selector("#app > section > div.el-dialog__wrapper.global-activity > div > div.el-dialog__body > div.global-activity__main > div.comfirm-btn").click()
        # time.sleep(1)


        # self.wc.find_element_by_xpath("//div[@id='app']/section/div/div/div[2]/div/div[4]/div/div/div/div/img").click()
        # time.sleep(1)
        # self.wc.find_element_by_xpath("//ul/div/li/span").click()

    def dologout(self):
        #点击退出登录
        last_height = self.wc.execute_script("return document.body.scrollHeight")
        self.wc.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Avtor = self.wc.find_element_by_xpath("//div[@id='app']/section/div/div/div[2]/div/div[4]/div/div/div/div/img")
        ActionChains(self.wc).move_to_element(Avtor).perform()
        self.wc.find_element_by_xpath("//ul/div/li/span").click()



    def bet5starSSC(self):
        time.sleep(2)
        self.wc.find_element_by_xpath("//div[@id='app']/section/div/div/div/div[2]/div[5]/span").click()
        time.sleep(2)
        self.wc.find_element_by_xpath("(//img[@alt='img'])[10]").click()


        k=self.wc.find_element_by_css_selector('img[title="M6体育"]')
        ActionChains(self.wc).move_to_element(k).perform()
        time.sleep(7)

        self.wc.switch_to.frame('iframe')
        time.sleep(1)
        self.wc.find_element_by_xpath("//div[@id='']").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[12]").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[23]").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[35]").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[46]").click()
        self.betinto()

        # self.wc.execute_script("window.scrollBy(0,400)")
        # self.wc.find_element_by_xpath("(//button[@type='button'])[2]").click()
        #
        # time.sleep(1)
        # self.wc.find_element_by_css_selector("button.el-button.bet-confirm-btn.el-button--primary").click()
        # # self.wc.switch_to.alert.accept()
        # time.sleep(2)
        # self.wc.find_element_by_css_selector("i.el-message-box__close.el-icon-close").click()
    def bet5starSSC2(self):
        # self.wc.switch_to.frame('iframe')
        time.sleep(2)
        #五星组合
        self.wc.find_element_by_xpath("//div[2]/div[3]").click()
        time.sleep(1)
        #选号
        #万
        self.wc.find_element_by_xpath("(//div[@id=''])[3]").click()
        #千
        self.wc.find_element_by_xpath("(//div[@id=''])[20]").click()
        #百
        self.wc.find_element_by_xpath("(//div[@id=''])[21]").click()
        #十
        self.wc.find_element_by_xpath("(//div[@id=''])[31]").click()
        #个
        self.wc.find_element_by_xpath("(//div[@id=''])[50]").click()
        self.betinto()
        # self.wc.execute_script("window.scrollBy(0,400)")
        # self.wc.find_element_by_xpath("(//button[@type='button'])[2]").click()
        # time.sleep(1)
        # self.wc.find_element_by_css_selector("button.el-button.bet-confirm-btn.el-button--primary").click()
        # # self.wc.switch_to.alert.accept()
        # time.sleep(2)
        # self.wc.find_element_by_css_selector("i.el-message-box__close.el-icon-close").click()
    def bet5starSSC3(self):
        time.sleep(2)
        # 组选60
        self.wc.find_element_by_xpath("//div[2]/div[2]/div[2]").click()
        time.sleep(1)
        #选号
        self.wc.find_element_by_xpath("(//div[@id=''])[5]").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[14]").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[16]").click()
        self.wc.find_element_by_xpath("(//div[@id=''])[17]").click()
        self.betinto()
        # self.wc.execute_script("window.scrollBy(0,400)")
        # self.wc.find_element_by_xpath("(//button[@type='button'])[2]").click()
        # time.sleep(1)
        # self.wc.find_element_by_css_selector("button.el-button.bet-confirm-btn.el-button--primary").click()
        # time.sleep(2)
        # self.wc.find_element_by_css_selector("i.el-message-box__close.el-icon-close").click()

    def bet5starSSC4(self):
        r=random.randint(2,3)
        time.sleep(1)

        # 龙虎和
        self.wc.find_element_by_xpath("//div[3]/div[2]/div").click()
        time.sleep(1)
        #选字
        self.wc.find_element_by_xpath("(//div[@id=''])[%d]")%r.click()
        self.betinto()

    def betinto(self):
        # 下注
        self.wc.execute_script("window.scrollBy(0,400)")
        self.wc.find_element_by_xpath("(//button[@type='button'])[2]").click()
        time.sleep(1)
        self.wc.find_element_by_css_selector("button.el-button.bet-confirm-btn.el-button--primary").click()
        time.sleep(2)
        self.wc.find_element_by_css_selector("i.el-message-box__close.el-icon-close").click()
if __name__=="__main__":
    L=Login()
    L.dologin()
    # L.dologout()
    L.bet5starSSC()
    L.bet5starSSC2()
    L.bet5starSSC3()