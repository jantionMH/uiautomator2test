import unittest,time
from youtube.unittestweb import unittestyoutube
from HTMLTestRunner import HTMLTestRunner

testsuit = unittest.TestSuite()
list = [unittestyoutube('test_01_setwindow'), unittestyoutube('test_02_enterweb'), unittestyoutube('test_03_openfirstpage'),
        unittestyoutube('test_04_socll_down'),unittestyoutube('test_05_hover'),unittestyoutube('test_06_typetext')]
testsuit.addTests(list)
now=time.strftime("%Y%m%d-%H_%M_%S_",time.localtime(time.time()))

filepath='C:\\Users\\janti\\PycharmProjects\\seleniumdriver\\testreport\\'+now+'report.html'
with open(file=filepath,mode='wb') as f:
   runner=HTMLTestRunner(stream=f,title='UI测试报告',description='测试用例执行情况')
   runner.run(testsuit)