list1 = [1,2,3]
list2 = list(list1)
print(list2)
print("list1==list2?", list1 == list2)
print("list1==list2 ?", list1 is list2)

set1 = set([1,2,3])
set2 = set(set1)
print(set2)
print("set1==set2?", set1 == set2)
print("set1 is set2 ?", set1 is set2)

dict1 = {1: [1,'w'], 2: 0, 3: 98}
dict2 = dict(dict1)
print(dict2)
print("dict1 == dict2？", dict1 ==dict2)
print("dict1 is dict2 ?", dict1 is dict2)

import copy
list1 = [1,2,3]
list2 = copy.copy(list1)
print(list2)
print("list1==list2?", list1 == list2)
print("list1==list2 ?", list1 is list2)
set1 = set([1,2,3])
set2 = copy.copy(set1)
print(set2)
print("set1==set2?", set1 == set2)
print("set1 is set2 ?", set1 is set2)

dict = [1:'人工智能应用', 2:'数据统计分析',3:'web开发']
dict2 = dict(dict1)
print(dict2)
print("dict1 == dict2？", dict1 ==dict2)
print("dict1 is dict2 ?", dict1 is dict2)


tuple = (1,2,3)
tuple2 = tuple(tuple)
print(tuple2)
print("tuple1 == tuple2 ?",tuple== tuple2)
print("tuple is tuple2 ?",tuple is tuple2)

tuple = (1,2,3)
tuple2 = tuple[:]
print(tuple2)
print("tuple1 == tuple2 ?",tuple== tuple2)
print("tuple is tuple2 ?",tuple is tuple2)

list1 = [[1,2], (30,40)]
list2 = list(list1)

list1.append(100)
print("list1:",list1)
print("list2:",list2)

list1[0].appened(3)
print("list1:",list1)
print("list2:",list2)

list1[1] += (50,60)
print("list1:",list1)
print("list2:",list2)

import copy

alist=[1,2,3,["a","b"]]
d = copy.deepcopy(alist)

print(alist)
print("拷贝后的对象",d)

alist.append(5)
print(alist)
print("拷贝后的对象",d)

alist[3].append("c")
print(alist)
print("拷贝后的对象",d)

set1 = {1:1, 2:2, 3:3}
set2 = set1
print(set2)
print("set1 == set2 ?".set1 == set2)
print(id(set1))
print(id(set2))


