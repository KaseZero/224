#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/20 11:09
# Author    : smart
# @File     : login.py
# @Software :{PRODUCT_NAME}
import time
from common.com import common
class zentao():
    c = common("F")
    def login(self,user,ps,i):
        self.c.open('http://192.168.55.40')
        self.c.click('id','zentao')
        time.sleep(1)
        self.c.send('id','account',user)
        time.sleep(1)
        self.c.send('name','password',ps)
        time.sleep(1)
        self.c.click('id','submit')
        time.sleep(1)
        if i ==0:
            return self.c.dr.title
        else:
            t=self.c.alter().text
            self.c.alter().accept()
            return t
    def addbug(self,build,title,i):
        #点测试
        self.c.click("xpath",".//*[@id='menuMainNav']/li[6]/a")
        #点击bug
        time.sleep(5)
        # st = self.c.local_ele('ID', "appIframe-qa")
        self.c.frame('id', "appIframe-qa")
        time.sleep(3)
        self.c.click('xpath', ".//*[@id='navbar']/ul/li[3]/a")
        #点击提交bug
        time.sleep(1)
        self.c.click('xpath', ".//*[@id='mainMenu']/div[3]/div[2]/a")
        #选择影响版本
        if build==0:
            self.c.click('xpath', ".//*[@id='buildBox']/div[1]/div")
            time.sleep(1)
            self.c.click('xpath', ".//*[@id='pk_openedBuild-item-dHJ1bms--option']/div/label")
         #输入标题
        self.c.send('id','title',title)
        time.sleep(1)
         #点击提交
        self.c.click('id','submit')
        if i == 1:
            ls = self.c.local_eles('css','.text-danger.help-text')
            t=''
            for i in ls:
                t += i.text
                return t
        else:
            return self.c.text('css','.popover-content')
    def logout(self):
        self.c.click('xpath',".//*[@id='userDropDownMenu']/a/div/span")
        time.sleep(1)
        self.c.click('xpath',".//*[@id='userDropDownMenu']/ul/li[14]/a")
if __name__ == '__main__':
    zt=zentao()
    zt.login('admin','Qwe123',0)
    print(zt.addbug(0, '123', 0))