__author__ = 'shikun'
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("..")

import time
import unittest
import re_unittest, server
import common
from multiprocessing import  Pool
import test_demo
import operateYaml

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

def get_yaml_config():
    #get data from the file of appium_config.yaml
    return operateYaml.getYaml(PATH("./appium_config.yaml"))

def yaml_driverInfo():
    #得到yaml中：UDID，平台，平台版本，端口号
    #这些信息作为配置信息，最终会注入到driver
    #yaml_driverInfo包括N个list1，list1中是配置字典（driver配置需要的一部分）
    driver_partly = []
    the_driverConfig_num=len(yaml_config["appium"])
    print(the_driverConfig_num)
    for i in range(0,the_driverConfig_num):
        list1 = []
        t = {}
        t["deviceName"] = yaml_config["appium"][i]["devices"]
        devices=yaml_config["appium"][i]["devices"] #UDID
        s=common.get_phone_info(devices)
        t["platformVersion"] = s['release']
        t["platformName"] = yaml_config["appium"][i]["platformName"]
        t["port"] = yaml_config["appium"][i]["port"]
        list1.append(t)
        driver_partly.append(list1)
    print('我是driver_partly: %s' %driver_partly)
    return driver_partly

def runnerPool(yaml_config):
    #建立Driver的进程，N个Driver建立N个进程。
    #这个函数是并行测试的关键
    pool = Pool(len(yaml_config)) #Pool(进程池）,个数由devices个数决定
    #pool.map(func.,iterable) iterable inject func.
    pool.map(runnerCaseApp,yaml_config)  #runnerCaseApp是Case，devices_Pool是参数
    pool.close()
    pool.join()

def runnerCaseApp(yaml_config):
    suite = unittest.TestSuite()
    suite.addTest(re_unittest.TestInterfaceCase.parametrize(test_demo.testL, l_devices=yaml_config))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    yaml_config = get_yaml_config()
    if common.attached_devices(): #如果adb devices 可以查找到设备
        appium_server = server.Appium_server(yaml_config)
        appium_server.start_server()
        while not appium_server.is_runnnig():
           time.sleep(3)
        else:
            print('Appium_Server_is_Running')
        driver_partly=yaml_driverInfo()
        time.sleep(10)
        runnerPool(driver_partly)  #多进程的Driver方法
        appium_server.stop_server()
    else:
            print(u"设备不存在")


