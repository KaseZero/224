# 将字面量 复制给 变量
n1 = 100
f1 = 47.5
s1 = "http://www.baidu.com"

print(n1)
print(f1)
print(s1)

print("")

# 将一个变量赋值给  另外一个变量
n2 = n1
f2 = f1
print(n2)
print(f2)

#将一个运算的结果 赋值 给变量
print("")
n3 = 30+15
n4 = 100%3
s2 = str("1234") #类型的转换
print(n3)
print(n4)
print(s2)

f4 = str(1234)+"abc"
print(f4)

#演示 连续 赋值
a = b = c = 100
print(a)
print(b)
print(c)

a = 100 #赋值
print(a==10)  #判断

# 演示 赋值运算符拓展
b = 20

# b = b + 100
# b += 100
# print(b)

# b = b - 3
# b -= 3
# print(b)

# b = b*3
# b *= 3
# print(b)

# b = b/3  #保留 小数点的 除
# b /= 3
# print(b)

# b = b%3
# b %= 3
# print(b)

# b = 10
# b = b**3   # 幂运算
# b **= 3
# print(b)

# b = b // 3 #取整
# b //= 3
# print(b)

b = 4
# b = b&5
# b &=5
# print(b)

# b = b | 5
# b |= 5
# print(b)

# b = b ^ 5
# b ^= 5
# print(b)

b = 8
# b = b << 2
# b <<= 2
# print(b)

# b = b >> 1
b >>= 1
print(b)


#演示  占位符
n = 32
print("我今年%d岁了"%n) #占位符  运行时 %d的位置  会显示一个 整数

n1 = 10
n2 = 20
n3 = 30
print("第一个数是:%d  第二个数是:%d 第三个数是:%d"%(n3,n2,n1))

fn = 12.457545
print("小数：%.2f"%fn) #%.2f 以小数点 后面 只有两位的 形式显示
print("小数：%7.2f"%fn) #%7.2f 以小数点 后面 只有两位总长度为7右对齐位的 形式显示
print("小数：%-7.2f"%fn) #%-7.2f 以小数点 后面 只有两位总长度为7位且左对齐的 形式显示
print("小数：%2.2f"%fn) #%2.2f  总长度 如果 小于 实际长度  将会 失效   （格式要求是2  实际是5   现实的 结果 是5）

# 演示  加法运算

n1 = 20
n2 = 17
sumn = n1 + n2

f1 = 45.67
f2 = 14.54
sumf = f1+f2

print("sumn==%d  sumf==%.2f"%(sumn,sumf))

name = "李响"
age = 32
homePage = "http://www.baidu.com"
info = "我的名字叫:"+name+"我今年:"+str(age)+"岁了"+"我的个人主页是:"+homePage
print(info)

#演示 减法
n1 = 100
n2 = 56
sumn1 = n1 - n2
sumn2 = n2 - n1
print(sumn1)
print(sumn2)


n = 10
print(-n)

n = 10
print(+n)

#演示乘法
n = 10
n1 = n*3
print(n1)

str = "hello "
print(str*3)  #重复 字符串

print(45/5)
print(10/3)

print(11//3)  #舍弃小数部分

# print(10/0)
print(~-4)

str1 = "114514"
print(str1 * 4)

#比较运算符
print("89是否大于100:",89 > 100)
print("24*5是否大于等于76:", 24*5 >= 76)
print("86.5是否等于86.5:",86.5 == 86.5)
print("34是否等于34.0:", 34 == 34.0)
print("False是否小于True:", False < True)
print("True是否等于True:", True < True)

import time
t1 = time.gmtie()
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



