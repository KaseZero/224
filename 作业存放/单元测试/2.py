#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/24 9:26
# Author : xiaowei
# @File : arithmetic.py
# @Software : PyCharm

class ari():
    def add(self,a,b):
        return a+b
    def jian(self,a,b):
        return a-b
    def chen(self,a,b):
        return a*b
    def chu(self,a,b):
        if b!=0:
            return a/b
        else:
            return None