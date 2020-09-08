import unittest,time
from unit.login.loginYY import Unittest01
from HTMLTestRunner import HTMLTestRunner

testsuit = unittest.TestSuite()
list = [Unittest01('testA01'), Unittest01('testA02'), Unittest01('testA03'), Unittest01('testA04')]
testsuit.addTests(list)
now=time.strftime("%Y%m%d-%H_%M_%S_",time.localtime(time.time()))
print(now)
filepath='C:\\Users\\janti\\PycharmProjects\\webselemium\\unit\\result\\report'+now+'report.html'
with open(file=filepath,mode='wb') as f:
   runner=HTMLTestRunner(stream=f,title='UI测试报告',description='测试用例执行情况')
   runner.run(testsuit)