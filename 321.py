#1、使用循环语句，创建一个列表，列表中包括1~10 十个数的平方
for value in range(1,11):
    print(value**2)
num=[value**2 for value in range(1,11)]
print(num)
#改进版本
list =(1,2,3,4,5,6,7,8,9,10)
num_list=[item**2for item in list]
print(num_list)
