#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/20 11:09
# Author    : smart
# @File     : login.py
# @Software :{PRODUCT_NAME}
import time

from common.com import common
class login(common):
    def login(self,user,ps):
        self.open('http://127.0.0.1')
        self.click('id','zentao')
        self.send('id','account',user)
        self.send('name','password',ps)
        self.click('id','submit')
        time.sleep(1)
        return self.dr.title

if __name__ == '__main__':
    l = login('F')
    l.login('admin','Qwe123')