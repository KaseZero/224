url = 'http://www.python.org'
print(url[10])
print(url[-6])

url = 'www.baidu.com'
print(url[2: 10])
print(url[7: -6])
print(url[-10: -6])
print(url[3: 20: 4])

url = 'http://www.baidu.com'
print(url[5: ])
print(url[-10: ])
print(url[: 20])
print(url[:: 3])

str = "欢迎访问开源中国 www.oschina.com"

print("我们旧地址", str)
print("我们新地址:", str.replace(".com",".net"))

str = "this is string example....wow!!!"
print(str.replace("is", "was", 3))

while True:
    name = input("请输入内容:")
    if "傻逼" in name or "没马" in name or "sb":
        v = name.replace('傻逼', '**')
        v1 = v.replace('没马', '**')
        v2 = v.replace('sb', "**")
        print(v1)
        print(v2)
        exit()
    else:
        print(name)

str1 = "人生苦短,我用oython"
length = len(str1.encode('gbk'))
print(length)

srt = "ptghon官网 >>> www.python.org"
list1 = str.split()
print(list1)

list2 = str.split('>>>')
print(list2)

list3 = str.split(',')
print(list3)

list4 = str.split('',4)
print(list4)

list5 = str.split('>')
print(list5)

str2= "python官网"
list1 = str.split()
print(list1)

myDate = input("请输入日期")
a = myDate.split("/")
date = a[0] + "年" + a[1] + "月" +a[2] + "日"
print("日期为:",date)

bewstr = str.join(iterable)
list = ['www','python','org']
print('.',join(list))

dir = '','usr','bin','env'
print(type(dir))
print('/'.join(dir))

srt = 'www.python.org'
print(str.count('.'))

str = 'www.python.org'
print(srt.count('.',3))
print(str.count('.',5))

str = 'www.python.org'
print(str.count('.',3,-3))
print(str.count('.'),3,-4)
