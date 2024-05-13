#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/20 11:02
# Author    : smart
# @File     : com.py
# @Software :{PRODUCT_NAME}
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class common(object):
    def __init__(self,brower):
        if brower == "C":
            self.dr = webdriver.Chrome()
        elif brower == "F":
            self.dr = webdriver.Firefox()
        self.dr.maximize_window()

    def open(self,url):
        self.dr.get(url)
        self.dr.implicitly_wait(5)
    def ref(self):
        self.dr.refresh()
    def wait(self,i=5):
        self.dr.implicitly_wait(i)
     # 元素的定位
    def local_ele(self,type,value):
        el = None
        if type == "id":
            try:
                el = self.dr.find_element(By.ID,value)
            except:
                self.dr.get_screenshot_as_file('./img/元素类型'+type+'-值'+value+'未定位到.jpg')
        elif type == "name":
            try:
                 el = self.dr.find_element(By.NAME,value)
            except:
                self.dr.get_screenshot_as_file('./img/元素类型'+type+'-值'+value+'未定位到.jpg')

        elif type == "nclass":
            try:
                el = self.dr.find_element(By.CLASS_NAME,value)
            except:
                self.dr.get_screenshot_as_file('./img/元素类型' + type + '-值' + value + '未定位到.jpg')
        elif type == "tag":
            try:
                el = self.dr.find_element(By.PARTIAL_LINK_TEXT,value)
            except:
                self.dr.get_screenshot_as_file('./img/元素类型' + type + '-值' + value + '未定位到.jpg')
        return el
    #元素的操作
    def click(self,type,value):
        self.local_ele(type,value).click()
    def send(self,type,value,data):
        self.local_ele(type,value).send_keys(data)
    def clear(self,type,value):
        self.local_ele(type,value).clear()
    def text(self,type,value):
        t = self.local_ele(type,value).text
        return t
    def get_at(self,type,value,at):
        a = self.local_ele(type,value).get_attribute(at)
        return a
    #下拉列表的操作
    def select(self,type,value,ty,val):
        el = self.local_ele(type,value)
        if ty == "index":
            Select(el).select_by_index(val)
        elif ty == "value":
            Select(el).select_by_value(val)
        elif ty == "text":
            Select(el).select_by_visible_text(val)
    #警告框操作
    def alter(self):
        return self.dr.switch_to.alert
    #滚动条的操作
    def scroll(self,x,y):
        js = 'window.scollTo('+x+','+y+')'
        self.dr.execute_script(js)

    #句柄操作
    def windowh(self,i):
        #获取所有的句柄
        h = self.dr.window_handles
        print(h)
        #当前的句柄
        print(self.dr.current_window_handle)
        self.dr.switch_to.window(h[i])
    def __del__(self):
        time.sleep(2)
        self.dr.quit()

if __name__ == '__main__':
    b = common("F")
