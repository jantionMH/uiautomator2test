import websocket,requests,os,time,random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



class Youtube:
    def __init__(self):
        drvierpath = r"C:\Users\janti\driver\geckodriver-v0.26.0-win64\geckodriver.exe"
        self.wc = webdriver.Firefox(executable_path=drvierpath)

    def openbrowse(self):
        self.wc.maximize_window()

    def enterweb(self):
        self.wc.get("http://youtube.com")

    def openfirstpage(self):
        self.wc.save_screenshot('../data/login.png')
        self.wc.set_page_load_timeout(2)
        if self.wc.find_element_by_xpath("(//paper-button[@id='button'])[2]").text=='登录':
            print('打开首页成功')
        else:
            print('打开首页失败')

    def socll_down(self,x,y):
        js='window.scrollTo(%d,%d)'%(x,y)
        self.wc.execute_script(js)

    def hover(self):
        target=self.wc.find_element_by_xpath("(//a[@id='endpoint']/paper-item/yt-formatted-string)[6]")
        ActionChains(self.wc).move_to_element(target).perform()
        time.sleep(2)

    def typetext(self):
        self.wc.find_element_by_name('search_query').send_keys('巴夏',Keys.ENTER)

    def __del__(self):
        time.sleep(4)
        self.wc.quit()


if __name__ == '__main__':
    Y=Youtube()
    Y.openbrowse()
    Y.enterweb()
    Y.openfirstpage()
    Y.socll_down(500,500)
    Y.hover()
    Y.typetext()
