fish =1
while True:
    total = fish
    for _ in range(5):
        if (total -1) % 5 ==0:
            total = (total - 1) // 5 * 4
        else:
            flag = False
            break
     if flag:
         print(f"至少有{fish}条鱼")
         break
     fish += 1
#输入三角形三条边的长度如果他是三角形计算出面积不是则重新输入
import math
while True:
    a = float(input(('输入第一条边的长度')))
    b = float(input(('输入第二条边的长度')))
    c = float(input(('输入第三条边的长度')))
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        half = perimeter / 2
        area = math.sqrt(half * (half -a ) * (half - b) * (half - c))
        print(f'周长为{perimeter}')
        print(f'面积为{area}')
        break
    else:
        print('不能构成三角形面积')
#用户登录
for i in range(3):
    name = input('请输入用户名')
    passwd = input('请输入密码')
    if name == 'admin' and passwd =='123':
        print('登陆成功')
        break
    else:
        print('登录失败！')
        print('%d 次机会' %(2 - i))
else:
       print('三次机会用完')
#dos命令行程序
import os
for i in range(1000):
    cmd = input('[locahost@root]$')
    if cmd:
        if cmd == 'exit':
            print('退出')
            break
        else:
            print('运行 %s' % (cmd))
            os.system(cmd)
    else:
        continue
#输入十个大于0的整数1到100之间找出品均值最大值最小值
total = 0
x = 0
y = 101
for _ in range(1, 11):
    a = int(input('请输入10个0~100之间的整数'))
    total = total + a
    if a <+ y:
        y = a
        average = total /10
    print(f'平均数为{average}最大值为{x}最小值为{y}')
#统计不同字符个数
x = input("输入你的字符串:")
a = b = c = d = 0
for i in x:
    if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
        a = a + 1
    elif ord('0') <= ord(i) <= ord('9'):
        b = b + 1
        elif ord(i) == ord('')
        c = c +1
    else:
        d = d + 1

    print("这一行字符中字母的数量是: {},数字的数量是: {},空格的数量是:{},其他字符的数量是:{}.".format(a, b, c, d))