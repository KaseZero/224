#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/20 8:56
# Author : xiaowei
# @File : 简单的get请求.py
# @Software : PyCharm
import requests
# 简单的get请求
url='http://www.baidu.com'
req = requests.get(url)
# 设置编码格式
req.encoding='utf-8'

print(req.status_code) # 打印状态码
print(req.url) # 打印请求 url
print(req.headers) # 打印头信息
print(req.cookies) # 打印 cookie 信息
print(req.text) # 以文本形式字符串打印网页源码
print(req.content) # 以字节流形式打印

#带参数的get请求
# req1 = requests.get(url=url)
# print(req1.text)