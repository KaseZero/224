#创建一个学生类
#学生类中有个注册方法
#要求输入学生的 姓名、性别、年龄、专业和班级
#并把输入的学生信息 保存在当前目录下的stu.txt文件中
#每个学生信息独占一行 并且用‘，’分割 以.结尾
class student:
    def addstu(self):
        self.name=input('请输入学生姓名：')
        age=input('请输入年龄：')
        sex=input('请输入性别：')
        major=input('请输入所学专业：')
        cl=input('请输入所在班级：')
        return '姓名：{},年龄：{},性别：{},专业：{},班级：{}.'.format(self.name,age,sex,major,cl)

    def write(self):
        with open('./stu.txt','a+',encoding='utf-8')as f :
            stu = self.addstu()
            f.write(stu)
            f.write('\n')

    def checkstu(self,name):
        with open('./stu.txt','r',encoding='utf-8')as f :
            file = f.readlines()
        for i in file:
            if i.find(name) !=-1:
                print(i)
                return i

        else:
            print('用户不存在！')
            return None
    def showall(self):
        with open('./stu.txt', 'r', encoding='utf-8')as f:
            file = f.readlines()
        for i in file:
            print(i)
if __name__ == '__main__':
    st=student()
    st.write()
    st.showall()
    # st.checkstu('q')