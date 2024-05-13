#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/21 15:08
# Author : xiaowei
# @File : post请求.py
# @Software : PyCharm
import requests

# 方法一：
# 1.先定义一个字典 格式: data = {"表单参数 1":"对应的值","表单参数 2":"对应的值",...} （表单参数就是请求传入的参数）
# 2.让定义的字典与请求产生关联 response = requests.post(url,data=data) #底层会自动将请求的数据
# 变成 application/x-www-form-urlencoded 格式
url ='http://localhost:8082/p2p_management/login'
# data={
#     'username':'tom',
#     'password':'tom'
# }
# r = requests.post(url,data)
# print(r.text)

# 方法二：字符串的格式传输请求数据
data='username=tom&password=tom'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
}

r1 = requests.post(url,headers=headers,data=data)
print(r1.text)
print(r1.status_code)
print(r1.headers)
print(r1.cookies)
print(r1.encoding)
print(r1.url)
