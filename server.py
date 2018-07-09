#coding: utf-8
from multiprocessing import Process
import threading
import os
import urllib
import urllib.request
from urllib.error import URLError

class Run_Server(threading.Thread):
    #Run_server类用于支撑下面的Appium_server类
    def __init__(self,cmd):
        threading.Thread.__init__(self)
        self.cmd =cmd

# Run_Server继承了父类threading.THread的属性
# 但是，也重写了 父类的run方法：
    def run(self):
        os.system(self.cmd)
        print('os.system')

class Appium_server():
    def __init__(self, l_devices):
        #l_devices = DICT: yaml_appium_config
        self.l_devices = l_devices

    def start_server(self):
        """start the appium server
        :return:
        """
        for i in range(0, len(self.l_devices["appium"])):
            t1 = Run_Server(self.l_devices["appium"][i]["config"])
            #因为子类RunServer重写了run()方法，所以下面到start()实际调用的是子类的run方法
            p = Process(target=t1.start())
            #下面的start()方法是Process里的方法，与threading.Thread类中到start()无关
            p.start()


    def stop_server(self):
        os.system("taskkill -F -im 'node.exe'")

    def restart_server(self):
        self.start_server()
        self.stop_server()

    def is_runnnig(self):

        for i in range(0, len(self.l_devices["appium"])):
            url = " http://127.0.0.1:"+str(self.l_devices["appium"][i]["port"])+"/wd/hub"+"/status"
            try:
                response = urllib.request.urlopen(url, timeout=5)

                if str(response.getcode()).startswith("2"):
                    return True
                else:
                    return False
            except URLError:
                return False

