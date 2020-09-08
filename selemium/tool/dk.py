import websocket,requests,os,time, unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pymysql
class Unittest01(unittest.TestCase):
      def test01(self):
        drvierpath=r"C:\Users\janti\driver\chromedriver.exe" # 81.0.4044
        wc=webdriver.Chrome(executable_path=drvierpath)

        # wc.get("http://miletest.com/home")
        # js = "var q=document.body.scrollTop=60000"
        #
        #
        # # js = "window.scrollTo(0,document.body.scrollHeight)"
        #
        # wc.execute_script("window.scrollBy(0,500)" )
if __name__=="__main__":
    unittest.main()
    suit=unittest.TestSuite()
    suit.addTest(Unittest01('test01'))
    print('dfdfs')
    result=unittest.TestResult()
    suit.run(result)
    print(suit)