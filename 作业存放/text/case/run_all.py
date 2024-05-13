#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/22 9:51
# Author    : smart
# @File     : run_all.py
# @Software :{PRODUCT_NAME}
import os
import time
import unittest

from common.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    fp=open('../report/'+now+'report.html','wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='',
        description='',
        verbosity=2
    )
    suit = unittest.defaultTestLoader.discover(os.getcwd(),'test*.py')
    runner.run(suit)
    fp.close()