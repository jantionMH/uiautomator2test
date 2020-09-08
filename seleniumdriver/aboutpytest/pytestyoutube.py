import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.keys import Keys



class TestYoutube:
    # @pytest.fixture()
    def test_enterweb(self):
        global wc
        drvierpath = r"C:\Users\janti\driver\geckodriver-v0.26.0-win64\geckodriver.exe"
        wc = webdriver.Firefox(executable_path=drvierpath)
        wc.maximize_window()
        wc.get("http://youtube.com")
        assert wc.find_element_by_xpath("//a[@id='endpoint']/paper-item/yt-formatted-string").text=='首页'
    def test_openfirstpage(self):
        global wc
        wc.save_screenshot('../data/login.png')
        wc.set_page_load_timeout(2)
        # assert  wc.find_element_by_xpath("(//paper-button[@id='button'])[2]").text=='登录'
        if wc.find_element_by_xpath("(//paper-button[@id='button'])[2]").text=='登录':
            print('打开首页成功')
            wc.get_screenshot_as_file('./login.ping')
        else:
            print('打开首页失败')
    def test_socll_down(self):
        global wc
        js='window.scrollTo(%d,%d)'%(500,500)
        wc.execute_script(js)

    # @pytest.fixture(scope='function')
    def test_hover(self):
        global wc
        target=wc.find_element_by_xpath("(//a[@id='endpoint']/paper-item/yt-formatted-string)[6]")
        ActionChains(wc).move_to_element(target).perform()
        time.sleep(2)

    # @pytest.fixture(scope='function')
    def test_typetext(self):
        global wc
        wc.find_element_by_name('search_query').send_keys('巴夏',Keys.ENTER)
        time.sleep(3)
        print(wc.find_element_by_xpath("(//a[@id='video-title']/yt-formatted-string)[2]").text)
        assert '巴夏' in  wc.find_element_by_xpath("(//a[@id='video-title']/yt-formatted-string)[2]").text

    # @pytest.fixture(scope='class')
    def test_del(self):
        global wc
        time.sleep(4)
        wc.quit()

