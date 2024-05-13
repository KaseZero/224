#比较运算符
print("89是否大于100:",89 > 100)
print("24*5是否大于等于76:", 24*5 >= 76)
print("86.5是否等于86.5:",86.5 == 86.5)
print("34是否等于34.0:", 34 == 34.0)
print("False是否小于True:", False < True)
print("True是否等于True:", True < True)

import time
t1 = time.gmtime()
t2 = time.gmtime()
print(t1 == t2)
print(t1 is t2)

#逻辑运算符
age = int(input("请输入年龄:"))
hegit = int(input("请输入身高:"))
if 18 <= age <= 30 and hegit >= 170 and hegit <= 185 :
    print("恭喜，你符合报考条件")
else:
    print("抱歉您不符合条件")


print(100 and 200)
print(45 and 0)
print("" or "https://python.org/")
print(18.5 or "https://www.python.org/")

url = "http://www.oschina.net"
print("----False and xxx------")
print(False and print(url))
print("True and XXx-----")
print(True and print(url))
print("--- False or XXX----")
print( False or print(url))
print("---True or XXX----")
print(True or print(url))
#三目运算符
a = int(input("Input a: "))
b = int(input("Input b: "))
print("a大于b") if a > b else ( print("a小于b")) if a < b else print("a等于b")

#成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5]
if (a in list):
    print("1 - 变量a 在给定德列表中 list 中")
else:
    print("1 - 变量 a 不在给定德列表 list 中")
    if (b not in list):
        print("2 - 变量 b 不在给定德列表 list 中")
    else:
        print("2 - 变量 b 在给定德列表中 list 中")
a = 2
if (a in list):
    print("3 - 变量 a 不在给定的列表list 中")
else :
    print("3 - 变量 a 不在给定的列表 list 中")

#身份运算符
a = 20
b = 20
if (a is b):
    print("1 - a 和 b 有相似标识")
else:
   print("1 - a 和 b 没有相同的标识")
if (id(a) == id(b)):
   print("2 - a 和 b有相同的标识")
else:
    print("2 - a 和b 没有相同标识")

b = 30
if (a is b):
   print("3 - a 和 b 没有相同的标识")
else:
   print("3  a 和 b ，没有相同的标识")
if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同标识")

#is===区别
a = [1, 2, 3]
b = a
print(b is a)
print(b == a)

b = a[:]
print(b is a)
print(b == a)

#运算符优先级和结合性
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a+b) * c / d
print("(a+b) * c / d 运算结果为:", e)
e = ((a+b) * c) / d
print("((a+b) * c) / d 运算结果为:",e)
e = (a+b) * (c / d)
print("(a+b) * (c / d) 运算结果为:",e)
e = a + (b * c) / d
print("a + (b * c) / d 运算结果为:",e)

#and 拥有更高优先级
x = True
y = False
z = False
if x or y and z:
    print("yes")
else:
    print("no")