#1、创建一个demo.py文件
#在demo文件内 有个 class方法 为计算
#计算内 有  判断是否为偶数并返回      计算平方 并返回结果      计算立方并返回结果     求是否能被10整除并返回结果
#并在demo中 编写测试方法

#2、创建一个 计算的py文件
#3、在文件中 导入 demo模块中的各个方法

#4、输入一个数 输出的  是否为偶  是否能被10整除 他的平方 和立方
#demo.py
class Calculator:
    Calculator = input("请输入数字")
    @staticmethod
    def is_even(num):
        if num %2 == 0:
            return True
        else:
            return False
        @staticmethod
        def square(num):
            return  num ** 2
        @staticmethod
        def cube(num):
            return num ** 3
            @staticmethod
            def is_divisible_by_10(num):
                if num % 10==2:
                    return True
                else:
                    return False
