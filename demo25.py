#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/25 8:28
# Author : xiaowei
# @File : demo25.py
# @Software : PyCharm
'''
出勤管理系统的基本编写
a)查看所有出勤的信息
根据选择的功能，来查看当前所有已经签到的人员信息
b)签到
    根据选择的功能，来添加签到的信息。包括签到者的名称，编号，性别，职务和签到时间信息
c)签到查询
    根据输入的签到名称，在文件中查询出此签到的所有信息
d) 签到时间更新
根据选择的签到名称，更新签到的时间信息
'''
import time,re
class timecard:
    def showall(self):
        with open('./timecard.txt','r',encoding='utf-8')as f:
            return f.read()
    def add(self):
        name= input('请输入您的姓名：')
        id=input('请输入您的编号：')
        sex=input('请输入您的性别：')
        job=input('请输入您的职务：')
        lc=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        str1='姓名:{},编号:{},性别:{},职务:{},签到时间:{}'.format(name,id,sex,job,lc)
        return str1
    def sign_in(self):
        str2=self.add()
        with open('./timecard.txt','a',encoding='utf-8')as f:
            f.write(str2)
            f.write('\n')

    def search(self,name):
        name='姓名:'+name
        with open('./timecard.txt','r',encoding='utf-8')as f:
            li =f.readlines()
            for i in li:
                if i.startswith(name):
                    # print(i)
                    return i
            else:
                print('没有此人的考勤信息！')
    def update_time(self):
        name = input('请输入要更新的人员的姓名：')
        old =self.search(name)
        old_time= re.search('(?<=签到时间:).+',old).group()
        new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # 替换的考勤时间
        new = old.replace(old_time,new_time)
        all =self.showall()
        # 替换的是个人的所有信息
        alla=all.replace(old,new)
        with open('./timecard.txt','w',encoding='utf-8') as f:
            f.write(alla)
if __name__ == '__main__':
    tc=timecard()
    while True:
        print('''
        ***************************************************************************************
                                    出勤管理系统
                                1、查看所有出勤信息
                                2、签到
                                3、搜索签到信息
                                4、更新签到时间
                                5、退出
        ***************************************************************************************
        ''')
        n= input('请选择需要的服务：')
        if n =='1':
            print(tc.showall())
        elif n =='2':
            tc.sign_in()
        elif n=='3':
            name=input('请输入要查询的姓名：')
            print(tc.search(name))
        elif n=='4':
            tc.update_time()
            print('签到时间已经更新！')
        elif n=='5':
            print('感谢使用！下次再见！')
            break
        else:
            print('请输入正确的选项！')

