#创建set集合
set1 = set("www.python.org")
set2 = set([1,2,3,4,5])
set3 = set((1,2,3,4,5))
print("set1:",set1)
print("set2:",set2)
print("set3:",set3)
#访问set集合
a = {1,'c',1(1,2,3),'c'}
for ele in a:
    print(ele,end='')
#删除set集合
a = {1,'c',1(1,2,3),'c'}
print(a)
del(a)
print(a)
#向set集合中添加元素
a = {1,2,3}
a.add((1,2))
print(a)
a.add([1,2])
print(a)
#从set集合中删除元素
a = {1,2,3}
a.remove(1)
print(a)
a.remove(1)
print(a)
#discard()
a = {1,2,3}
a.remove(1)
print(a)
a.discard(1)
print(a)
#set作集合交集并集差集
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)
#set集合方法
set1 = {1,2,3}
set1.add((1,2))
print(set1)
set1 = {1,2,3}
set1.clear()
print(set1)
set1 = {1,2,3}
set2 = set1.copy()
print(set2)
set1 = {1,2,3}
set2 = {3,4}
set3 = set1.difference_update(set2)
print(set1)
set1 = {1,2,3}
set1.discard(2)
print(set1)
set1.discard(4)
print(set1)
set1 = {1,2,3}
set2 = {3,4}
set3 = set1.intersection(set2)
print(set1)
set1 = {1,2,3}
set2 = {3,4}
set1.intersection(set2)
False
print(set1)
set1 = {1,2,3}
set2 = {1,2}
set1.issubset(set2)
False
print(set1)
set1 = {1,2,3}
set2 = {1,2}
set1.issuperset(set2)
True
print(set1)
set1 = {1,2,3}
a = set1.pop()
print(set1)
set1 = {1,2,3}
set1.remove(2)
print(set1)
set1 = {1,2,3}
set2 = {3,4}
set3 = set1.symmetric_difference(set2)
print(set3)
set1 = {1,2,3}
set2 = {3,4}
set1.symmetric_difference_update(set2)
print(set1)
set1 = {1,2,3}
set2 = {3,4}
set3=set1.union(set2)
print(set3)
set1 = {1,2,3}
set1.update([3,4])
print(set1)
#frozenset集合
s = {'python','c','c++'}
fs = forzenset(['java','shell'])
s_sub = {'php','c##'}
s.add(fs)
print('s = ',s)
s.add(s_sub)
print('s =', s)
