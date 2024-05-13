# 2．完成出勤管理系统的基本编写
# a)查看所有出勤的信息
# 根据选择的功能，来查看当前所有已经签到的人员信息
# b)签到
#     根据选择的功能，来添加签到的信息。包括签到者的名称，编号，性别，职务和签到时间信息
# c)签到查询
#     根据输入的签到名称，在文件中查询出此签到的所有信息
# d) 签到时间更新
# 根据选择的签到名称，更新签到的时间信息
class student:
    def add(self):
        import time
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        age = input("请输入年龄：")
        major = input("请输入职务：")
        number=input("请输入编号：")
        localtime = time = time.strftime("%Y-%m-%d %H:%M:%M",time.localtime())
        print("签到时间为：", localtime)
        str1='姓名：'+name+',性别：'+sex+',年龄：'+age+',职务：'+major+',编号：'+number+',时间：'+time+'.'+'\n'
        print('签到成功')
        return str1
    def write(self):
        with open('./10.19.txt','a',encoding='utf-8') as f:
            f.write(self.add())
    def readstu(self):
        with open('./10.19.txt','r',encoding='utf-8') as f:
           fr=f.readlines()
           for i in fr:
               print(i)
    def checkstu(self,name):
        with open('./10.19.txt','r',encoding='utf-8') as f:
           fl=f.readlines()
           name = '姓名：' + name
           for i in fl:
               if i.startswith(name):
                   print(i)
                   return
           else:
               print('此人未签到!')
if __name__=='__main__':
    st=student()
    # st.write()
    # st.readstu()
    # st.checkstu('')
    # st.checkstu('aa')
stu = student()
while True:
    print('''***********************
              出勤管理系统
            1、查看所有出勤信息
            2、签到
            3、签到查询
            4、签到时间更新
            5、退出系统
    *************************************''')
    n = input("请选择您需要的功能:")
    if n == '1':
        stu.readstu()
    elif n == '2':
        stu.write()
    elif n == '3':
        name = input("请输入员工姓名:")
        stu.checkstu(name)
    elif n == '4':
        name =input("请输入员工姓名:")
        import time
        localtime = time = time.strftime("%Y-%m-%d %H:%M:%M", time.localtime())
        print("签到时间为：", localtime)
    elif n == '5':
        print(input("感谢使用，欢迎下次再来!"))
        break
    else:
        print(input("错误，没有该员工的签到记录以及信息！"))



