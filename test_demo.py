import time
from random import randint

import re_unittest


class testL(re_unittest.TestInterfaceCase):

    def setUp(self):
        super(testL, self).setUp()

    def Settings_search(self):
        self.driver.keyevent(3)
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

    def test_home(self):
        self.Settings_search()




