# coding: utf-8
import unittest
from appium import webdriver

def appium_testcase(l_devices):
    desired_caps = {}
    desired_caps['platformName'] = l_devices["platformName"]
    desired_caps['platformVersion'] = l_devices["platformVersion"]
    desired_caps['deviceName'] = l_devices["deviceName"]
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['udid'] = l_devices["deviceName"]
    #desired_caps['automationName'] = 'UIAutomator2'
    # desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    remote = "http://127.0.0.1:" + str(l_devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver



class TestInterfaceCase(unittest.TestCase):

    def __init__(self, methodName='runTest', l_devices=None):
        #super(TestInterfaceCase,self).__init__(methodName)
        unittest.TestCase.__init__(self,methodName)
        self.l_devices = l_devices

    def setUp(self):
        self.driver = appium_testcase(self.l_devices)

    def tearDown(self):
        self.driver.quit()


    #下面的静态和上面TestInterfaceCase类基本没有关联，TestInterfaceCase中没有方法引用了parametrize
    #这个静态方法。这里用静态主要是省了句：（class test(unittest.TestCase):）
    @staticmethod
    def parametrize(testcase_klass, l_devices=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, l_devices=l_devices[0]))
        return suite

