#修改单个列表元素
nums = [40,36,89,2,-66.2,100,7]
nums[2] = -26
nums[-3] = -66.2
print(nums)

#修改一组的元素值
nums = [40,36,89,2,-66.2,100,7]
nums[1:4] = [42.25, -77, -52.5]
print(nums)
#插入元素
nums = [40,36,89,2,-66.2,100,7]
nums[4:4] = [-77, -52.5 ,999]
#指定参数步长
nums = [40,36,89,2,-66.2,100,7]
nums[1:6:2] = [0.025,-99,20.5]
print(nums)
#删除列表元素
lang = ["2","3","45","244"]
del lang[1:4]
print(lang)
lang.extend(["sql","c#","GO"])
del lang[-5: -2]
print(lang)
#pop根据索引值
nums = [40,36,89,2,-66.2,100,7]
nums.pop(3)
print(nums)
nums.pop()
print(nums)
#remove根据元素值删除
nums = [40,36,89,2,-66.2,100,7]
#第一次删除
nums.remove(36)
print(nums)
nums.remove(36)
print(nums)
nums.remove(78)
print(nums)
#clear删除列表所有元素
url = list("https://www.python.org")
url.clear()
print(url)
#元组
#使用tuple函数创建元组
tup1 = tuple("hello")
print(tuple)
list1 = ['python','java','c++','javascprit']
tup2 = tuple(list)
print(tup2)
#将字典转换为元组
dict1 = {'a':100, 'b':42, 'c':9}
tup3 = tuple(dict1)
print(tup3)
#将区间转换为元组
range1 = range(1,2)
tup4 = tuple(range1)
print(tup4)
print(tuple())
#访问元组元素
tup1 = tuple("hello")
print(tup1)
#将列表转换为元组
list2 = ['pythin', 'java','c++','javascprit']
tup2 = tuple(list1)
print(tup2)
url = tuple("https://www.python.org/index")
#使用索引访问元组中的某个元素
print(url[3])
print(url[-4])
#使用切片访问元组中的一组元素
print(url[9:18])
print(url[9:18:3])
print(url[-6:-1])
