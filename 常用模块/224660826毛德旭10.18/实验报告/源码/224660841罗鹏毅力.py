# 2．完成图书管理系统的基本编写
# a)查看所有图书的信息
# 根据选择的功能，来查看当前所有添加进文件中的图书信息
# b)图书添加
#     根据选择的功能，来添加图书的信息。包括图书的名称，编号，作者，位置和是否出借信息
# c)图书查询
#     根据输入的图书名称，在文件中查询出此图书的所有信息
# d) 图书出借
# 根据选择的图书名称，更新图书的出借信息
# e) 图书归还
# 根据选择的图书名称，更新图书出借信息
class book():
    def add(self):
        import time
        name = input("请输入图书名称：")
        number = input("请输入图书编号：")
        author = input("请输入图书作者：")
        site = input("请输入图书位置：")
        loan = input("已添加")
        str1='名称：'+name+',编号：'+number+',作者：'+author+'位置：'+site+'.'+'\n'
        return str1
    def write(self):
        with open('./stu1.txt','a',encoding='utf-8') as f:
            f.write(self.add())
    def readstu(self):
        with open('./stu1.txt','r+',encoding='utf-8') as f:
           fr=f.readlines()
           for i in fr:
               print(i)
    def checkbk(self,name):
        with open('./stu1.txt', 'r', encoding="utf-8") as p:
            bk = p.readlines()
            name = '名称:' + name
            for i in bk:
                if i.startswith(name):
                    print(i)
                    return
            else:
                print('没有这本书')
    def borrowed(self,name):
        with open('./stu1.txt', 'a+', encoding="utf-8") as f:
            import re
            pattern = re.compile(r'([a-z]+)([a-z]+)',re.I)
            result = pattern.match(f.name)
            if result == None:
                print('出借成功')
            else:
                print('没有这本书')
    def returnd(self):
        print('还书成功')



if __name__=='__main__':
    bk=book()
    # bk.write()
    # bk.readstu()
    # bk.checkstu('')
    # bk.checkstu('aa')
bk = book()
while True:
    print('''***********************
              图书管理系统
            1、查看所有图书信息
            2、新增图书信息
            3、搜索图书信息
            4、借书
            5、还书
            6、退出系统
    *************************************''')
    n = input("请选择您需要的功能:")
    if n == '1':
        bk.readstu()
    elif n == '2':
        bk.write()
    elif n == '3':
        name = input("输入查询图书名称：")
        bk.checkbk(name)
    elif n == '4':
        name = input('请输入借出的书名:')
        bk.borrowed(name)
    elif n == '5':
        name = input('请输入还书的书名:')
        bk.returnd()

    elif n == '6':
        print(input("退出系统!"))
        break
    else:
        print(input("请输入正确的值"))



