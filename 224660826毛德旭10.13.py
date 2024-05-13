import re
print(re.findall(r"\d+","12345678888888abc"))
print(re.findall(r"\d*","12345678888888abc"))
print(re.findall(r"\d{3,}","12345678888888abc"))
print(re.findall(r"\d{3,8}","12345678888888abc"))
print(re.findall(r"\d+?","12345678888888abc"))
print(re.findall(r"\d{3,8}?","12345678888888abc"))
import re
str="Use this toggle to the left to manage how your"\
    "borwser uses BBC' s performance cookies. If you're"\
    "outside the UK you can also use the toggle to set"\
    "your preferences for personalised advertising cookies."
pattern=re.compile(r"\b[abcABC][a-z]*\b")
print(pattern.findall(str))

import re
str="Use this toggle to the left to manage how your"\
    "borwser uses BBC' s performance cookies. If you're"\
    "outside the UK you can also use the toggle to set"\
    "your preferences for personalised advertising cookies."
pattern=re.compile(r"\b[a-z]*(es|ing|er)\b")
print(pattern.findall(str))
import re
result=re.finditer(r"\b([a-z])([a-z])[a-z]\2\1\b","fdadd abcba")
match_list=[]
for i in result:
    match_list.append(i.group(0))
    print(match_list)

#JSON
import json
#Python
data = {
    'id':1,
    'title':'建党100周年',
    'content':'2021年是中国建党100周年。为庆祝党的百年华诞，党中央决定举行一系列活动'
}

json_str = json = json.dumps(data)
print("Pyth原始数据：",repr(data))
print("JSON对象:",json_str)

import json
#Python
data = {
    'id':1,
    'title':'建党100周年',
    'content':'2021年是中国建党100周年。为庆祝党的百年华诞，党中央决定举行一系列活动'
}

json_str = json = json.dumps(data)
print("Pyth原始数据：",repr(data))
print("JSON对象:",json_str)

data2 = json.loads(json_str)
print("data2['title']",data2['title'])
print("data2['content']",data2['content'])

with open('data.json','w')as f:
    json.dump(data,f)

with open('data.json','r')as f:
    data = json.load(f)

import os

print(os.path.join('demo', 'exercise'))

import os

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('D:\\demo\\exercise', filename))

f = open("my_file.txt", 'rb+')
byt = f.read()
print(byt)
print("\n:")
print(byt.decode('utf-8'))
f.close()
f = open('a.txt', 'rb')
print(f.tell())
print(f.read(1))
print(f.tell())
f.seek(5)
print(f.tell())
print(f.read(1))
f.seek(5, 1)
print(f.tell())
print(f.read(1))
f.seek(-1, 2)
print(f.tell())
print(f.read(1))


import os
print(os.path.join('demo','exercise'))

import os
myFiles=['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
    print(os.path.join('D:\\demo\\exercise',filename))

f=open("my_file.txt",'rb+')
byt=f.read()
print(byt)
print("\n:")
print(byt.decode('utf-8'))
f.close()
f=open('a.txt','rb')
print(f.tell())
print(f.read(1))
print(f.tell())
f.seek(5)
print(f.tell())
print(f.read(1))
f.seek(5,1)
print(f.tell())
print(f.read(1))
f.seek(-1,2)
print(f.tell())
print(f.read(1))
class Sample:
    def __enter__(self):
        print("调用__enter__()")
        return "Foo"
    def __exit__(self, type, value, trace):
        print("调用__exit__()")

with Sample() as Sample:
    print("sample:",sample)

class Sample:
    def __enter__(self):
        return self
    def __exit__(self, type, value, trace):
        print("type:",type)
        print("value:",value)
        print("trace:",trace)
    def do_something(self):
        bar=1/0
        return bar+10
with Sample() as sample:
    sample.do_something()


try:
    with open("a.txt") as f :
         do something
except xxxError:
    do something about exception









