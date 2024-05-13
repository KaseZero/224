#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/20 9:37
# Author : xiaowei
# @File : 存储图片.py
# @Software : PyCharm
import requests

url='https://static.oschina.net/uploads/cooperation/index_channel_list_ad_between_gitee_jRqtJ.jpg'
r = requests.get(url)
content =r.content
with open('1.jpg','wb') as f:
    f.write(content)
print('图片下载成功！')