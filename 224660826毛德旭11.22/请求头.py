#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/21 14:40
# Author : xiaowei
# @File : 请求头.py
# @Software : PyCharm
import requests
url ='http://www.baidu.com/'
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
r =requests.get(url,headers)

print(r.text)