#while循环
num = 1
while num <100 :
    print("num=",num)
    num += 1
print("循环结束!")
#2
my_char="http://www.python.org"
i = 0;
while i<len(my_char):
    print(my_char[i],end='')
    i = i+1
#for in循环
print("计算1+2+3...+100的值为：")
result = 0
for i in range(101):
    result += i
print(result)
#for in 循环对列表进行遍历
my_list = [1,2,3,4,5]
for ele in my_list:
    print('ele=',ele)
#for in 循环遍历字典
my_dic = {'百度':"百度搜索,百度文库",\
          '阿里巴巴':"淘宝,天猫,咸鱼".\
          '腾讯':"qq,微信"

}
for ele in my_dic:
    print('ele =',ele)
#循环结构中else
address = "http://www.baidu.com"
i = 0
while i < len(address):
    print(address[i],end="")
    i = i + 1
else:
    print("\n执行else 模块")
#while for 循环嵌套
 i = 0
 while i<10:
     for j in range(10):
     print('i=',i,"j="j)
     i=i+1
#break结束循环
 add = "http://www.oschina.net/,http://www.csdn.net"
 for  i in add:
     if i ==',' :
         #中止循环add
        break
   print(i,end="")
else:
    print("执行else语句中的代码")
print("\n执行循环体外的代码")
#跳出外循环和内循环
saa = "http://www.oschina.net/,http://www.csdn.net"
flag = False
for i in range(3):
    for j in add:
        if j ==',':
            flag = True
            break
        print(j,end="")
        print("\n跳出内循环")
    if flag == True:
        print("跳出外层循环")
        break
#return 结束方法
def test() :
    for i in range(10)  :
        for j in range(10) :
            print("i的值是:%d,j的值是:%d" % (i , j))
            if j == 1:
                return
            print("return后的输出语句")
test()
#1、使用循环语句，创建一个列表，列表中包括1~10 十个数的平方
for value in range(1,11):
    print(value**2)
num=[value**2 for value in range(1,11)]
print(num)

