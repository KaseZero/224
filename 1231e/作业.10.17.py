#10.17
#1、将写入stu.txt文件中的所有信息 全部查看
#2、检测学生姓名是否已经存在 如果存在 则显示此学生的信息 如果不存在 则提示
f = open("stu.txt",encoding="utf-8")
content = f.read()
print(content)

students = []
f = open('stu.txt')
for line in f:
    line = line.replace('/n', '')
    student = tuple(line.split(''))
    students.append(student)
name = input('请输入学生姓名：')
found = False
for student in students:
    if (student[0]==name):
        found=True
        for i in range(len(student)):
            print(student[name],end='')
        break
        if not found:
            print('找不到此学生'.format(name))
