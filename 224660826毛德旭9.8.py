#1序列索引
str="python官网"
print(str[0],"==",str[-6])
print(str[5],"==",str[-1])

#序列切片
str="python官网"
print(str[:2])
print(str[::2])
print(str[:])

#序列相加
str="www.python.org"
print("python语言"+"官网地址:"+str)

#序列相乘
str="python语言"
print(str*3)
#列表的创建用
list = [None]*5
print(list)
#元素baohan
str="www.python.org"
print('o' not in str)

#序列相关函数
str="www.python,org"
print(max(str))
print(min(str))
print(sorted(str))
#列表list
print(type(["http://www.python.org", 1, [2,3,4], 3.0]))

#创建列表
num = [1,2,3,4,5,6,7]
name = ["python官网","https://www.python.org"]
program = ["C++", "python", "Java"]
#使用list函数创建表
list1 = list("hello")
print(list)
#将元组转换成表
tuple1 = ('python','java','c++','JavaSCript')
list2 = list(tuple1)
print(list2)
#将字典转换成列表
dict1 = {'a':100, 'b':42,'c':9}
list3 = list(dict1)
print(list3)
#将区间转换成列表
range1 = range(1,6)
list4 = list(range1)
print(list4)
#创建空列表
print(list())

#访问列表元素
list = ['red','green','blue','yellow','white','black']
print(list[0])
print(list[1])
print(list[2])

list = ['red','green','blue','yellow','white','black']
print(list[-1])
print(list[-2])
print(list[-3])
#使用负数索引值截取
nums = [10,20,30,40,50,60,70,80,90]
print(nums[0:4])
companylist = ['google','apple','jd','taobao','wiki']
print("companylist[1]:",companylist[1])
print("companylist[1:-2]",companylist[1:-2])

url = list("https://www.python.org/index")
print(url[3])
print(url[-4])
print(url[9: 18])
print(url[9: 18: 3])
print(url[-6: -1])

#删除列表
intlist = [1,45,8,34]
print(intlist)
del intlist
print(intlist)

#添加列表元素
language = ["python","c++","java"]
birthday = [1991, 1998, 1995]
info = language + birthday
print("language =",language)
print("birthday =", birthday)
print("info =", info)
#append方法添加元素
a = ['python','c++','java']
a.append('Php')
print(a)
t = ('Javascprit','c#','Go')
a.append(t)
print(a)
a.append(['ruby','sql'])
print(a)

#etend方法添加元素
a = ['python','c++','java']
a.extend('c')
print(a)
t = ('Javascprit','c#','Go')
a.extend(t)
print(a)
a.extend(['ruby','sql'])
print(a)

#insert方法插入元素
a = ['python','c++','java']
a.insert(a,'c')
print(a)
t = ('c#','Go')
a.insert(2,t)
print(a)
a.insert(3, ['ruby','sql'])
print(a)
a.insert(0,"http://www.python.org")
print(a)
#查找列表元素
nums = [40,36,89,2,36,100,7,-20.5, -999]
print(nums.index(2))
print(nums.index(100,3,7))
print(nums.index(7,4))
print(nums.index(55))

#count
nums = [40,36,89,2,36,100,7,-20.5, -999,36]
print("36出现了%d次"% nums.count(36))
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")