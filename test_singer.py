import unittest
import time
from appium import webdriver
from random import  randint
from HTMLTestRunner import  HTMLTestRunner


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps={}   #新建一个Desired caps的字典  Desired capability
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='7.0'
        desired_caps['deviceName']='0080f03c'
        desired_caps['UDID'] ='0080f03c'
        #Q
        # desired_caps['appPackage']='com.google.android.calculator'
        # desired_caps['appActivity']='com.android.calculator2.Calculator'
        #M
        desired_caps['appPackage']='com.android.calculator2'
        desired_caps['appActivity']='.Calculator'
        # desired_caps ['automationName']= "Uiautomator2"
        # desired_caps['unicodeKeyboard']='True' #利用uicode申明 更好的中文化(使用unicode编码方式发送字符串)
        # desired_caps['resetKeyboard']='True' #是将键盘隐藏起来
        self.driver=webdriver.Remote('http://127.0.0.1:4729/wd/hub',desired_caps)
        #self.driver=webdriver.Remote('http://0.0.0.0:4724/wd/hub',desired_caps)
    def test_calculator(self):
        print('\n-----start testing-----')
        self.driver.keyevent(3)
        print('111111111111111111111111111')
        time.sleep(2)
        self.driver.keyevent(3)
        time.sleep(2)
        time.sleep(15)
        self.driver.keyevent(4)
        time.sleep(2)
        print('111111111111111111111111111')
        self.driver.tap([(100,845)])
        time.sleep(2)
        print('1')
        self.driver.tap([(260,1111)])
        time.sleep(2)
        print('1')
        self.driver.tap([(155,325)])
        print('1')
        for i  in  range(1000):
            time.sleep(randint(15,26))
            self.driver.swipe(500,800,100,800,200)

    def tearDown(self):
        self.driver.quit()
        print('-----testing finished-----')

if __name__ == '__main__':
    mysuite =unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(mysuite)
    #or unittest.main()
