#lambda表达式
def name(list):
    return
name(list)
def add(x,y):
    return x+ y
print(add(3,4))
#eval 和exec的用法
dic ={}
dic['b'] = 3
print(dic.keys())
exec("a = 4",dic)
print(dic.keys())

a =1
exec("a = 2")
print(a)
a = exec("2+3")
print(a)
a = eval('2+3')
print(a)
#zip函数
my_list = [11,12,13]
my_tuple = [21,22,23]
print([x for x in zip(my_list,my_tuple)])

my_dic = {31:2,32:4,33:5}
my_set = {41,42,43,44}
print([x for x in zip(my_dic)])

my_pychar = "python"
my_shechar = "shell"
print([x for x in zip(my_pychar,my_shechar)])
#reversed函数
s = {1,2,3,4,5}
print(list(reversed([1,2,3,4,5])))
print(list(reversed(s)))
print("s=",s)
#sorted函数
b = [5,4,3,2,1]
print(sorted(b))
b = [5,4,3,1,2]
print(sorted(b))
b = {4:1,\
     5:2,\
     3:3,\
     2:6,\
     1:8
}
print(sorted(b.items()))
b = {1,3,3,2,4}
print(sorted(b))
b = "51432"
print(sorted(b))
#range函数
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
#dir函数
print(dir(str))
#help函数
print(help(str.lower()))
