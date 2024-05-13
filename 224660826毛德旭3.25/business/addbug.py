#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/25 16:36
# Author    : zhe
# @File     : ztbug.py
# @Software : PyCharm
from common.com import common
import login
import time
class ztbug():
    def bug(self,i,value):
        d = common('C')

        d.click('link_text','测试')
        d.click('xpath',".//*[@id='subNavbar']/ul/li[1]/a")
        d.click('xpath',".//*[@id='mainMenu']/div[3]/a[3]")
        d.click('xpath',".//*[@id='openedBuild_chosen']/ul")
        d.click('xpath',".//*[@id='openedBuild_chosen']/div/ul/li")
        d.send_keys('xpath',".//*[@id='title']",'123')
        d.click('id','submit')
        time.sleep(2)
        if i == 0:
            return d.dr.title
        else:
            t = d.alter().text
            d.alter().accept()
            return t
if __name__ == '__main__':
    z = ztbug()
    z.login('admin','Qwe123',0)

