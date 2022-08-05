import os
import unittest

from appium import webdriver

import warnings



class AppiumTest(unittest.TestCase):
    option = {}
    driver = None

    def setUp(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self.option['app'] = os.getcwd()+"/eribank.apk"
            self.option['appPackage'] = "com.experitest.ExperiBank"
            self.option['appActivity'] = ".LoginActivity"
            self.option['platformName'] = 'Android'
            self.option['deviceName'] = 'emulator-5554'
            self.driver = webdriver.Remote("http://35.169.17.173:4723/wd/hub",self.option)

    def testFirstAutomationTest(self):
        print(self.driver.mobile.DATA_NETWORK)
        #if len(self.driver.find_elements("//*[@text='OK']")) > 0: self.driver.find_element( "//*[@text='OK']").click()
        #self.driver.find_element("//*[@text='Username']").send_keys("company")
        #self.driver.find_element("//*[@text='Password']").send_keys("company")
        #self.driver.find_element("//*[@text='Login']").click()

    def tearDown(self): self.driver.quit()


