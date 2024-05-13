# a)查看所有图书的信息
# 根据选择的功能，来查看当前所有添加进文件中的图书信息
# b)图书添加
#     根据选择的功能，来添加图书的信息。包括图书的名称，编号，作者，位置和是否出借信息
# c)图书查询
#     根据输入的图书名称，在文件中查询出此图书的所有信息
# d) 图书出借
# 根据选择的图书名称，更新图书的出借信息
# e) 图书归还
# 根据选择的图书名称，更新图书的出借信息
class book:
    def add(self):
        name = input("请输入图书名称:")
        number = input("请输入图书编号：")
        writer = input("请输入图书作者：")
        id = input("请输入图书位置：")
        # jie = input("请输入是否出借：")

        return '请输入图书名称:{},请输入图书编号：{},请输入图书作者：{},请输入图书位置:{}.'.format(
            name, number, writer, id)
    def write(self):
        with open('./shijian.txt', 'a', encoding='UTF-8') as f:
            f.write(self.add())
            f.write("\n")
    def checkstu(self,name):
            with open('shijian.txt', 'r', encoding="utf-8") as p:
                cl = p.readlines()
                name = '请输入图书名称:' + name
                for i in cl:
                    if i.startswith(name):
                        print(i)
                        return i
                else:
                    print("查无此书！")

    def jie(self, bk_name):
        import re
        with open('shijian.txt', 'r', encoding='utf-8') as kan:
            suo = kan.read()
            name = re.findall(r'(?<=图书名称：).+(?=, 图书编号)', suo)
            if [bk_name] == name:
                pan_name = re.findall(r'(?<=已借出：).+(?=.)', suo)
                if pan_name == ['0']:
                    with open('shijian.txt', 'r', encoding='utf-8') as cun:
                        c = cun.read()
                        chu = re.search(r'(?<=图书名称：).+(?=,)', c)
                        pattern = re.compile(r'(?<=图书名称：).+(?=,)')
                        result = pattern.search(c)
                        t = result.group()
                        with open('shijian.txt', 'w', encoding='utf-8') as gai:
                            gai.write("图书名称：")
                            gai.write(t)
                            gai.write(',')
                            gai.write("已借出：1.")
                            gai.write('\n')
                            print("成功借出这本书！")
                            print("图书名称：", t, "已借出：1.")
                else:
                    print("这本书已经借出！")
            else:
                print("没有这本书！")

    def huan(self, huan_name):
        import re
        with open('shijian.txt', 'r', encoding='utf-8') as kan:
            suo = kan.read()
            name = re.findall(r'(?<=图书名称：).+(?=, 图书编号)', suo)
            if [huan_name] == name:
                pan_name = re.findall(r'(?<=已借出：).+(?=.)', suo)
                if pan_name == ['1']:
                    with open('shijian.txt', 'r', encoding='utf-8') as cun:
                        c = cun.read()
                        chu = re.search(r'(?<=图书名称：).+(?=,)', c)
                        pattern = re.compile(r'(?<=图书名称：).+(?=,)')
                        result = pattern.search(c)
                        t = result.group()
                        with open('shijian.txt', 'w', encoding='utf-8') as gai:
                            gai.write("图书名称：")
                            gai.write(t)
                            gai.write(',')
                            gai.write("已借出：0.")
                            gai.write('\n')
                            print("归还成功！")
                            print("图书名称：", t, "已借出：0.")
                else:
                    print("这本书还没有被借出！")
            else:
                print("没有这本书！")
    def readstu(self):
        f = open("shijian.txt", encoding="UTF-8")
        print(f.read())
        f.close()

if __name__ == '__main__':
    stu = book()
    while True:
        print('''
        ***********************************************************************
                                    1,查看所有图书的信息
                                    2,图书添加
                                    3,查询具体图书详情
                                    4,借书
                                    5,图书归还
                                    6,退出系统
        ***********************************************************************
              ''')
        n = input("请选择系统编号: ")
        if n == '1':
            stu.readstu()
        elif n == '2':
            stu.write()
        elif n == '3':
            name = input("请输入需要查询的图书名称: ")
            stu.checkstu(name)
        elif n == '4':
            bk_name=input("请选择你需要的功能编号:")
            stu.jie(bk_name)
        elif n=='5':
            huan_name = input("请选择你需要的功能编号:")
            stu.huan(huan_name)
        elif n == 6:
            print('感谢使用！')
            break