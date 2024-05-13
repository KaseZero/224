import time
from selenium import webdriver
from selenium.webdriver.common.by import  By

class Browser(object):

    def __init__(self, brower):

     if brower =="F":
         self.driver =webdriver.firefox()
     elif brower == 'C':
         self.driver =webdriver.Chrome()
     self.dr.maximize_windows()

     def open(self,url):
         self.dr.get(url)
         self.dr.implicitly_wait(5)
    def ref(self):
        self.dr.refresh()

    def __del__(self):
        time.sleep(5)
        self.driver.quit()
if __name__=='__main__':
        web = Browser("Chrome")
        web.open_url('http://www.192.168.55.67')
        web.open_url('http://www.192.168.55.67:8082')









