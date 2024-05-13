#创建字典
scores = {'数学':95, '英语':92, '语文':84}
print(scores)
dict1 = {(20,30): 'great',30:[1,2,3]}
print(dict1)
dict2 = {}
print(dict2)
#formskey方法创建字典
knowledge = ['语文','数学','英语']
scores = dict.formkeys(knowledge,60)
print(scores)
#访问字典
tup = (['two',26],['one',88],['three',100],['four',-59])
dic = dict(tup)
print(dic['one'])
print(dic['five'])
#get使用列
a = dict(two=0.65, one=88, three=100, fours=-59)
print(a.get('five','该键不存在'))
#删除字典
a = dict(two=0.65, one=88, three=100, fours=-59)
print(a)
del a
print(a)
#字典添加键值对
s = {'数学':95}
print(s)
s['语文'] = 89
print(s)
s['哲学'] = 78
print(s)
#字典修改键值对
a = {'数学':95, '英语':92, '语文':84}
print(a)
a['哲学'] = 100
print(a)
#字典删除值键对
a = {'数学':95, '英语':92, '语文':84}
del a['语文']
del a['数学']
print(a)
#判断字典中是否存在值键对
a = {'数学':95, '英语':92, '语文':84}
print('数学' in a)
print('哲学' in a)
#字典方法
print(dir(dict))
#keys,valuss,items方法
scores = {'数学':95, '英语':92, '语文':84}
print(scores.keys())
print(scores.values())
print(scores.items())
#listf方法返回
a = {'数学':95, '英语':92, '语文':84}
b = list(a.keys())
print(b)
#使用for in 方法循环遍历他们的返回值
a = {'数学':95, '英语':92, '语文':84}
for k in a.keys():
    print(k,end='')
print("\n-------------")
for v in a.values():
    print(v,end='')
print("\n--------")
for k,v in a.items():
    print("key:",k,"value:",v)
#copy方法
a = {'one':1, 'two':2, "three":[1,2,3]}
b = a.copy()
print(b)
a['four']=100
print(a)
print(b)
a['three'].remove(1)
print(a)
print(b)
#update方法
a = {'one':1, 'two':2, "three":3}
a.update({'one':4.5, 'four': 9.3})
print(a)
#pop和popitem方法
a = {'数学':95, '英语':92, '语文':84,'化学':83,'生物':83,'物理':98}
print(a)
a.pop('化学')
print(a)
a.popitem()
print(a)
#setdefault方法
a = {'数学': 95, '英语': 92, '语文': 84}
print(a)
a.setdefault('物理',94)
print(a)
a.setdefault('化学')
print(a)
a.setdefault('数学', 100)
print(a)