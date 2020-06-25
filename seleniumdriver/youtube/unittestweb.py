import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

drvierpath = r"C:\Users\janti\driver\geckodriver-v0.26.0-win64\geckodriver.exe"


class unittestyoutube(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wc = webdriver.Firefox(executable_path=drvierpath)
        print('初始化测试')

    def test_01_setwindow(self):
        self.wc.maximize_window()

    def test_02_enterweb(self):
        self.wc.get("http://youtube.com")

    def test_03_openfirstpage(self):
        self.wc.save_screenshot('../data/login.png')
        self.wc.set_page_load_timeout(2)
        if self.wc.find_element_by_xpath("(//paper-button[@id='button'])[2]").text == '登录':
            print('打开首页成功')
        else:
            print('打开首页失败')

    def test_04_socll_down(self, x=500, y=500):
        js = 'window.scrollTo(%d,%d)' % (x, y)
        self.wc.execute_script(js)

    def test_05_hover(self):
        target = self.wc.find_element_by_xpath("(//a[@id='endpoint']/paper-item/yt-formatted-string)[6]")
        ActionChains(self.wc).move_to_element(target).perform()
        time.sleep(2)

    def test_06_typetext(self):
        self.wc.find_element_by_name('search_query').send_keys('巴夏', Keys.ENTER)

    @classmethod
    def tearDownClass(cls) -> None:

        # cls.ws.close()
        print('测试结束')
        time.sleep(4)

        # cls.wc.quit()


if __name__ == '__main__':
    unittest.main()
