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

