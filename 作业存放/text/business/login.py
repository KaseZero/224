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
        self.c.send('id','account',user)
        self.c.send('name','password',ps)
        self.c.click('id','submit')
        time.sleep(1)
        if i ==0:
            return self.c.dr.title
        else:
            t=self.c.alter().text
            self.c.alter().accept()
            return t

if __name__ == '__main__':
    zt=zentao()
    zt.login('admin','Qwe123',0)

