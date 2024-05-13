#1、使用循环语句，创建一个列表，列表中包括1~10 十个数的平方
for value in range(1,11):
    print(value**2)
num=[value**2 for value in range(1,11)]
print(num)
