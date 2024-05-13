#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/21 14:42
# Author : xiaowei
# @File : 带参数的get请求.py
# @Software : PyCharm
import requests
# 方法一：直接在url地址上的参数
# response= requests.get("https://www.so.com/s?q=王心凌")
#
# with open('1.html','wb')as f:
#     f.write(response.content)
# kw = '笔记本电脑' # 定义搜索关键字
# url = 'https://www.so.com/s?ie=utf-8&q=' + kw # 先使用浏览器访问
# headers = { # 定义自定义请求头
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# response = requests.get(url, headers=headers) # 发送自定义请求头
# response.encoding = "utf-8"
# filename = kw + '.html' # 定义储存结果的文件名
# with open(filename, 'w', encoding='utf-8') as f: # 存储文件
#     f.write(response.text)
# print(filename, '保存成功')

#
'''
方法二:
1.先定义一个字典 格式: param={"查询参数 1":"对应的值","查询参数 2":"对应的值",...} (查询参数
就是值查询字符串参数 URL 中?后面接的就是查询字符串参数)
2.让定义的字典与请求产生关联 response = requests.get(url,params=p)
'''
# 使用 params 参数为格式为字典,当有多个数据时会自动拼接
kw = '笔记本电脑'
url = 'https://www.so.com/s?'
headers = { # 定义自定义请求头
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
params = { "ie": "utf-8","q": kw}
response = requests.get(url, headers=headers, params=params) # 发送自定义请求头和请求数据
response.encoding = "utf-8"
filename = kw + '.html' # 定义储存结果的文件名
with open(filename, 'w', encoding='utf-8') as f: # 存储文件
    f.write(response.text)
print(filename, '保存成功')