# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2023/10/16 16:08
# Author        : smart
# @File         :224660834 刘涛 10.18.py
# @Software     :PyCharm
'''
1、创建一个学生类
2、学生类中有个注册方法
3、要求输入学生的 姓名、性别、年龄、专业和班级
4、并把输入的学生信息 保存在当前目录下的stu.txt文件中
5、每个学生信息独占一行 并且用‘，’分割 以.结尾
'''
 #
# 1、将写入stu.txt文件中的所有信息 全部查看
# 2、检测学生姓名是否已经存在 如果存在 则显示此学生的信息 如果不存在 则提示            


class student:
    def add(self):
        name=input('请输入名称：')
        sex=input('请输入编号：')
        age=input('请输入价格：')
        major=input('请输入库存：')
        cl=input('请输入是否在库：')
        # str1='姓名：'+name+',性别：'+sex+',年龄：'+age+',专业：'+major+',班级：'+cl+'.'
        str1='姓名：%s,性别：%s,年龄：%s' %(name,sex,age)
        str1='名称：{}，编号：{}，价格：{}，库存：{}，是否在库：{}.'.format(name,sex,age,major,cl)
        return str1
    def write(self):
        with open('./goods.txt','a',encoding='utf-8') as f :
            f.write(self.add())
            f.write('\n')
    def showall(self):
        with open('./goods.txt', 'r', encoding='utf-8') as f:
            fl =f.readlines()
            for i in fl:
                print(i)

    # 1、将写入stu.txt文件中的所有信息 全部查看

    # 2、检测学生姓名是否已经存在 如果存在 则显示此学生的信息 如果不存在 则提示

    def checkstu(self,name):

        with open('./goods.txt', 'r', encoding='utf-8') as f:
            # 方法一：使用列表来获取
            # fl =f.readlines()
            # for i in fl:
            #     lname=i.split('，')[0][3:]
            #     if lname==name:
            #         print(i)
            #         return i
            # 方法二：使用字符串来获取
            fl=f.read()
            fl_index= fl.find(name)
            if fl_index > 0:
                end =fl.find('.',fl_index)

                print(fl[fl_index-3:end])
            # 方法三：
            # fl=f.read()
            # fname = re.findall(r'(?<=姓名：).+(?=.)',fl)
            # # print(fname)
            # for i in fname:
            #     if i.startswith(name):
            #         print(i)
            #         return i

            else:
                print('没有此商品！')


if __name__ == '__main__':
    stu=student()
    # stu.write()
    # stu.showall()
    stu.checkstu('43')
#
while True:
    print('''
        学生管理系统
        1、查询当前所有商品信息
        2、新增商品信息
        3、搜索商品信息
        4、退出系统
        ''' )
    n=input('请选择你所需要的功能编号：')
    if n=='1':
        stu.showall()
    elif n=='2':
        stu.write()
    elif n=='3':
        name=input('请输入需要查询的商品编号：')
        stu.checkstu(name)
    elif n=='4':
        print('退出系统')
        break
    else:
        print('谢谢')





