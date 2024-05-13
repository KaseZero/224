from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import ddt

@ddt.ddt
class Testcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

        @ddt.data("Selenium","Appium","Postman")
        def test_001(self,value):
            self.driver.find_element(By.ID,"kw").send_keys(value)
            self.driver.find_element(By.ID,"su").click()

    if __name__=='__main__':
        unittest.main