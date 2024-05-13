#集合
s = {"张三","李四","先辈"}
s.update(["赵六","德川"])
print(s)
s.remove("张三")
print(s)
#焦急用 & 或者 intersection
s1 = {"张三","李四","先辈"}
s2 = {'王五','赵六','德川','李四'}
print(s1 & s2)
print(s1.intersection(s2))
#并集用 | 或者unio
s1 = {'张三','李四','王五'}
s2 = {'王五','赵六','先辈','德川'}
print(s1 | s2)
print(s1.union(s2))
#差集用 - 或者difference
s1 = {'张三','李四','王五'}
s2 = {'王五','赵六','先辈','德川'}
print(s1 - s2)
print(s1.difference(s2))

#数据类型转换
num_int = 123
num_float = 1.23

num_new = num_int + num_float
print("num_int 数据类型为:",type(num_int))
print("num_float 数据类型为:",type(num_float))

print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))
#Int函数将一个字符串转换为数值类型
print(int())
print(int(3))
print(int(3.6))
print(int('12',16))
print(int('10',8))
#float函数用于将整数和字符转换为浮点型
print(float(112))
print(float(-123.6))
print(float('123'))
#eval函数用来执行表达式并且返回表达式的值
x = 7
x = eval('3 * x')
print(x)

#1float_转换为浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))
#str-- 转换为字符串行
num2 = 10
print(type(str(num2)))
#4.tuple --将一个序列转换为元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))
#4list--- 将一个序列转换为一个表
t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))
#5 eval --- 将字符串中的数据转换成python表达式原本类型
str1 = '10'
str2 = '[1,2,3]'
str3 = '(1000,2000,3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

d = {"张三":"财务部","李四":"市场部","王五":"品牌部"}
print(d)
#添加
d.setdefault("田所浩二","研发部")
print(d)
d.pop("研发部")
print(d)
for i in d:print(i)
print(d.get("张三"))
print(d.get("田所浩二"))

c = [1,2,'a',3123,314441]
c.append(334)
c.insert(1,"野兽先辈")
c.pop(2)
print(c)
for i in 1:print(i)

b1 = bytes()
b2 = b''
b3 = b'https://c.baicheng.net/python/'
print("b3:",b3)
print(b3[3])
print(b3[7:22])
b4 = bytes('中国共产党成立100周年了‘, encoding='UTF-8')
print("b4:", b4)
b5 = "坚决拥护中国共产党的领导".encode('UTF-8')
print("b5:", b5)

