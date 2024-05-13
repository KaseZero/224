import re
inputNum = input("请输入一个三位数")
result = re.match("r^\d[3]$", inputNum)
if result is None:
    print("不符合要求")
else:
    print("符合要求")

import re
pattern = re.compile(r"[1][345789]\d[9]")
imputMobile = input("请输入手机号码:")
if pattern.match(imputMobile):
    print("手机号有效")
else:
    print("手机号无效！")

import re
pattern = re.compile(r'\d+')
result = re.match(pattern,"8abcdefg0")
print(result)
print(result.group(0))
print(result.start(0))
print(result.end(0))
print(result.span(0))

import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
result = pattern.match('hello warld')

print(result)
print(result.group(0))
print(result.span(0))
print(result.group(1))
print(result.span(1))
print(result.group(2))
print(result.span(2))
print(result.groups())
print(result.group3)

import re
ipaddress = "123.323.321"
result = re.search(r"\d\d\d\.\d\d\d.\d\d\d\.\d\d\d", ipaddress)
print(result)

import re
content = "123def"
pattern = re.compile("([a-z]*)([0-9]*)([a-z]*)")
result = pattern.search(content)
print(result.group)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))

