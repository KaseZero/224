age = int(input("请输入你的年龄:"))
if age <18 :
    print("你还未成年请在家人的陪同下使用该软件")
    print("如果你已经得到了家长的同意，请忽略以上提示")
    print("软件正在使用中")

#if else 语句
import sys

age = int(input("请输入你的年龄:"))
if age < 18 :
   print("警告，你还未成年不能使用这个软件")
   print("请主动退出")
   sys.exit()
else:
    print("你已成年，可以使用该软件")
    print("时间宝贵切勿沉迷")
print("软件使用中")
#if elif else 语句
height=float(input('请输入身高（米）：'))
weight=float(input('请输入体重（千克）：'))
bmi=weight/(height*height)
if bmi<18.5:
    print('BMI指数为：'+str(bmi))
    print('体重过轻')
elif bmi>=18.5 and bmi<24.9:
    print('BMI指数为：' + str(bmi))
    print('正常范围，注意保持')
elif bmi>=24.9 and bmi<29.9:
    print('BMI指数为：' + str(bmi))
    print('体重过轻')
else:
    print('BMI指数为：' + str(bmi))
    print('肥胖')


# match subject:
#       case<pattern_1>:
#           <action_1>
#       case<pattern_2>:
#           <action_2>
#       case<pattern_3>:
#           <action_3>
# case_:
# <action_wildcard>
#if else 判断表达式是否成立
b = False
if b:
    print('b是True')
else:
    print('b是False')
n = 0
if n:
    print('n不是零值')
else:
    print('n是零值')
s = ""
if s:
    print('s不是空字符串')
else:
    print('s是空字符串')
l = []
if l:
    print('l不是空列表')
else:
    print('l是空列表')
d = {}
if d:
    print('d不是空字典')
else:
    print('d是空字典')


def func():
    print('函数被调用')
#循环嵌套
#
if func:
    print('func()返回值不是空')
else:
    print('func()返回值是空')

age = int(input('请输入你的年龄:'))
if age < 18:
    print('警告：你还未成年，不能使用该软件')
else:
    print('你已经成年，可以使用该软件')

proof = int(input('输入驾驶员每100ml血液酒精的含量：'))
if proof < 20:
    print('驾驶员不构成酒驾')
else:
    if proof < 80:
        print('驾驶员已构成酒驾')
    else:
        print('驾驶员已构成醉驾')

age = int(input('请输入你的年龄:'))
if age < 12:
    print('婴幼儿')
elif age >= 12 and age < 18:
    print('青少年')
elif age >= 18 and age < 30:
    print('成年人')
elif age >= 30 and age < 50:
  #TODO:成年人
else:
    print('老年人')
#assset断言
mathmark = input(())
assert  0 <= mathmark <=100
print("数学考试成绩为:",mathmark)