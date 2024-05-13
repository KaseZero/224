from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class Testcase(unittest.TestCase):
   dr = webdriver.Firefox()
   @classmethod
   def setUp(self):

        self.dr.implicitly_wait(3)
        self.dr.maximize_window()
        self.dr.get("https://www.baidu.com")
   @classmethod
   def tearDown(self):
        time.sleep(3)
        self.dr.quit()

   def test_001(self):
        self.dr.find_element(By.ID, "kw").send_keys("Selenium")
        self.dr.find_element(By.Id,"su").click()

   def test_002(self):
        self.dr.find_element(By.Id,"kw").send_keys("Postman")
        self.dr.find_element(By.ID,"su").click()

if __name__=='__main__':
        unittest.main()
