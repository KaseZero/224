S = 'www.python.org'
addr = 'http://www.oschina.net'
print(S.ljust(35))
print(addr.ljust(35))

S= 'www.python.org'
addr = 'http://oschina.net'
print(S.ljust(35,'-'))
print((addr.ljust(35,'-')))

#r.just
S = 'www.python.org'
addr = 'http://www.oschina.net'
print(S.ljust(35))
print(addr.rjust(35))

S = 'www.python.org'
addr = 'http://www.oschina.net'
print(S.ljust(35,'_'))
print(addr.rjust(35,'_'))

#center
S = 'www.python.org'
addr = 'http://www.oschina.net'
print(S.center(35))
print(addr.center(35,))

S = 'www.python.org'
addr = 'http://www.oschina.net'
print(S.center(35,'_'))
print(addr.center(35,'_'))

#startswith检索字符
str = 'www.python.org'
print((str.starswith("w")))
print(str.startswith("p",4))
#endswith()
str = 'www.python.org'
print(str.endswitch("org"))
#字符大小写转换
#1.title()
str = 'www.python.org'
print(str.title())
#lower()
str = 'WWW.PYTHON.ORG'
print(str.lower())

#upper
str = 'www.python.org'
print(str.upper())

#去除字符间空格
#strip
str = "python可用于多种平台包括liunc和os \t\n\r"
print(str.strip())
print(str.strip(",\r"))
print(str)

#rstrip
str = "python可用于多种平台包括liunc和os \t\n\r"
print(str.rstrip())
#格式化输出
str = "网站名称: {:>9s}\t网址:{:S}"
print(str.format("python官网","www.python.org"))

#以货币形式显示
print("货币形式: {:,d}".format(1000000))
print("科学计数法:{:E}".format(1200.12))
print("100的十六进制: {:#x}".format(100))
print("0.01的百分比表示:{:.0%}".format(0.01))

#字符编码转换
str = "python计算机编程语言"
print(str.encode())

str = "python计算机编程语言"
print(str.encode("GBK"))

#decode
str = "Python计算机编程语言"
bytes=str.encode()
print(bytes)
print(bytes.decode())

str = "python计算机编程语言"
print(str.encode("GBK"))
print(bytes)
print(bytes.decode())