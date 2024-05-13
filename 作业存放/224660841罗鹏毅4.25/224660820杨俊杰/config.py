#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 15:04
# Author    : zhangqi
# @File     : config.py
# @Software : PyCharm
import logging
import os

#项目路径
prj_path = os.path.dirname(os.path.abspath(__file__))
data_path = prj_path
test_path = prj_path
log_file = os.path.join(prj_path,'log.txt')
report_file = os.path.join(prj_path,'report.html')

#log文件配置
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',#log格式
    datefmt = '%Y-%m-%d %H:%M:%S',#日期格式
    filename='log.txt',#日志输出文件
    # encoding='utf-8',
    filemode='a'
)
#数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_ps = 'root'
db = 'xzs'

#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '3194551377@qq.com'
smtp_ps = 'wyzzqdsyqeopdeea'
sender = smtp_user
receiver = '3194551377@qq.com'
subject = '接口测试报告'


if __name__ == '__main__':
    logging.info("接口测试")















