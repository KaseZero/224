from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class Commonshare(object):
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
            # try:
           el=self.dr.find_element(By.ID,value)
            # except:
            #     self.dr.get_screenshot_as_file('./9090.jpg')
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
    def sele(self,type,value,ty,va):
        el=self.locate(type,value)
        if ty=='index':
            Select(el).select_by_index(va)
        if ty=='value':
            Select(el).select_by_value(va)
        if ty=="text":
            Select(el).select_by_visible_text(va)
    def alert(self):
        return self.dr.switch_to.alert
    def scro(self):
        js="window.scrollTo(0,1000)"
        self.dr.execute_script(js)
    def windo(self,i):
        print(self.dr.current_window_handle)
        jk=self.dr.window_handles
        print(jk)
        self.dr.switch_to.window(jk[i])
    def __del__(self):
         time.sleep(5)
         self.dr.quit()
if __name__=='__main__':
    pass


