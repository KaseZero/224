#return语句
def add(a,b):
    c = a + b
    return c
c = add(3,4)
print(c)
print(add(3,4))

def isGreater0(x):
    if x > 0:
        return  True
    else:
        return False
    print(isGreater0(5))
    print(isinstance(0))
#空值
print(None is [])
print(None is "")
print(type(None))
#局部变量
def demo():
    add = "https://github.com"
    print("函数内部add=",add)

demo()
print("函数外部 add=",add)
#全局变量
sxr = 'https//www.baidu.com'
def text():
    print("函数体内访问:",add)

text()
print('函数体外访问:',add)
#globals函数
github = "githug官网"
githubAddess = "https://github.com"
def text():
    gitee = "shell教程"
    githubAddess="https:gitee.com/"
print(globals())
#locals函数
github = "githug官网"
githubAddess = "https://github.com"

def text():
    gitee = "shell教程"
    githubAddess= "https://gitee.com/"
    print("函数内部的 locals:")
    print(locals())

text()
print("函数外部的 locals:")
print(locals())
#vars object函数
github = "githug官网"
githubAddess = "https://github.com"
class Demo:
    gitee = "gitee官网"
    githubAddess =" https://gitee.com/"

print("有 object:")
print(vars(Demo))
print("无 object:")
print(vars())
#局部函数
def outdef ():
    def indef():
        print("http://www.python.org")
        indef()
    outdef()
def outdef():
    def indef():
        print("调用局部函数")
    return indef()

new_indef = outdef()
new_indef()

#闭包函数
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

square = nth_power(2)
cube = nth_power(3)

print(square(2))
print(cube(2))
#闭包方法
def nth_power_rewrite(base,exponent):
    return base ** exponent