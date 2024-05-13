#定义一个函数 打印乘法表 。有一个数值型的参数  可以输出 几几乘法表
def fun(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j}*{i}={i * j}", end="\t")
        print( )
fun(9)
def fun(i):
 for i in range(1,12):
    for j in range(1, i + 1):
        print("*", end='')
    print()
fun(12)
def fun(n):
    for i in range(1,9):
        for j in range(i-0,9):
            print("*", end="\t")
        print( )
fun(9)

