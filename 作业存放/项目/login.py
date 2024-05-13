import time
from selenium.webdriver.support.select import Select
from common.common import Commonshare

class Login(Commonshare):
    def login(self,user,pwd):
        self.open_url('https://ww192.168.55.67')
        self.click('xpath',html/body/div[2]/div[1]/div/div/div[3]/ul/a[2])