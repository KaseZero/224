a = input("Enter a number:")
b = input("Enter another unmber:")

print("aType:", type(a))
print("bType:", type(b))

result = a + b
print("resultValue:", result)
print("resultType:", type(result))

a = input("Enter a number:")
b = input("Enter another number:")

a = float(a)
b = int(b)
print("aType:", type(a))
print("bType:", type(b))

result = a + b
print("resultValue:", result)
print("resultType:", type(result))

unm1=int(input("请输入第一个数: "))
num2=int(input("请输入第二个数: "))
if(num1<num2):
    print("两个数从小到大的排序为:",num1,num2)
else:
    print("两个数从小到大的排序为:",num2, num1)





name = "人民网"
age = 100
url = "http://people.com.cn/"
print("中国共产党成立%d周年了！%s网址是%s." % (age, name, url))

n = 1234567
print("n(10):%10d." % n)
print("n(5):%5d." % n)
url = "http://www.python.org"
print("url(35):%35s." % url)
print("url(20):%20s." % url)

n = 114514
print("n(09):%d" % n)
print("n(+9):%9d" % n)
f = 140.5
print("f(-+0):%-+010f" % f)
s = "Hello"
print("s(-10):%." % s)

str1 = '网站\t\t域名\t\t\t年限\t\t价值'
str2 = '开源中国\t\twww.oschina.net\t\t10\t\t5000w'
str3 = '百度\t\twww.baidu.com\t\t20\t\t500000w'

print(str1)
print(str2)
print(str3)
print("----------------------------------")

info = "Python官网:http://www.python.org\n\
       Java官网：http://www.oracle.com\n\
       Vue.js官网:https://cn.vuejs.org/"
print(info)

str4 = "Python官网""http://www.python.org"
print(str4)

str5 = "java""Python""c++""PHP"
print(str5)

name = "Python官网"
age = 10
course = 4
info = name + "已经" + str(age) + "岁了，共发布了" + repr(course) + "个版本"
print(info)

s = "http://www.python.org"
s_str = str(s)
s_repr = repr(s)

print(type(s_str))
print (s_str)
print(type(s_repr))
print(s_repr)
