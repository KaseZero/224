#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/11/20 9:41
# Author : xiaowei
# @File : 异常处理.py
# @Software : PyCharm
import requests
from requests.exceptions import Timeout
try:
    response = requests.get('https://www.testwo.com', timeout=0.1)
    print(response.status_code)
except Timeout:
    print("请求超时,请重试。")