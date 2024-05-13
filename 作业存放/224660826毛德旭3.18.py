from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class browser(object):
    def __init__(self,brower):
        if brower=="Firefox":
            self.dr=webdriver.Firefox()
        elif brower=="Chrome":
            self.dr=webdriver.Chrome()
        self.dr.maximize_window()
    def delay(self):
        self.dr.implicitly_wait(5)
    def open(self,url):
        self.dr.get(url)
        self.delay()
        print("成功")
    def locate(self,type,value):
        el=None
        if type=='id':
            el=self.dr.find_element(By.ID,value)
        if type == 'name':
            el = self.dr.find_element(By.NAME, value)
        if type == 'class_name':
            el = self.dr.find_element(By.CLASS_NAME, value)
        if type == 'tag_name':
            el = self.dr.find_element(By.TAG_NAME, value)
        if type == 'link_text':
            el = self.dr.find_element(By.LINK_TEXT, value)
        if type == 'xpath':
            el = self.dr.find_element(By.XPATH, value)
        if type == 'css':
            el = self.dr.find_element(By.CSS_SELECTOR, value)
        if el is not None:
            return el
    def click(self,type,value):
        el=self.locate(type,value)
        el.click()
    def input(self,type,value,data):
        el=self.locate(type,value)
        el.send_keys(data)
    def back(self):
        self.dr.back()
        self.delay()
        print('后退到:%s'%self.dr.current_url)
    def dele(self):
        time.sleep(5)
        self.dr.quit()
if __name__=='__main__':
    web=browser('Firefox')
    web.open('http://192.168.55.68:8080/p2p_management')
    web.click('xpath',".//*[@id='login']/div[4]/input")
    web.click('xpath',"html/body/div[2]/div[2]/div[6]/div/div/div[1]/div[2]/div[1]/div/div")
    web.input('id','proNum',"5467576")
    web.input('id','proName',"admin")
    web.input('id','proLimit',"678")
    web.input('id','annualized',"80")
    web.click('id','saveBtn')
    web.delay()
    web.dele()
