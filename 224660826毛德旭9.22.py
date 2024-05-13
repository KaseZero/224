#面向对象
class Tortoise:
    bodyClor = "绿色"
    footNum = 4
    weight = 10
    hasShell = True
def crawl(self):
    print("fuck you")
def eat(selt):
    print("ass we can")
def sleep(self):
    print("boy net door")
def protect(self):
    print("think you sir")

#定义类
class theFirstDemo:
    '''这是学习python定义的第一个类'''
    add = 'http://www.python.org'
    def say(self,content):
        print(content)
#init self类构造方法
class theFirstDemo:
    '''这是学习python定义的第一个类'''
    def_init_(self):
         print("调用构造方法")
    add = 'http://www.python.org'
    def say(self,content):
        print(content)
myObj = theFirstDemo()
#对象
class Planguage:
    name = "python官网"
    add = "http://www.python"
    def_init_(self,name,add):
    self.name = name
    self.add = add
    print(name,"网址为:",add)
    def say(self,content):
        print(content)
planguage = Planguage("java官网","https://www.orcle.com")
#类对象的使用
class Planguage:
    name = "python官网"
    add = "http://www.python"
    def_init_(self,name,add):
    self.name = name
    self.add = add
    print(name,"网址为:",add)
    def say(self,content):
        print(content)
planguage = Planguage("java官网","https://www.orcle.com")
print(planguage.name,planguage.add)
#修改是实例的变量的值
planguage.name="C语言"
planguage.add="https://en.cppreference.com/w/"
planguage.say("人生苦短我用python")
print(planguage.name,planguage.add)
#给类对象添加删除变量
planguage.money= 159.9
print(planguage.money)
del planguage.money
print(planguage.money)
#实例2
class Planguage :
    name = "python官网"
    add = "http://www.python"
    def_init_(self, name, add):
    self.name = name
    self.add = add
    print(name, "网址为:", add)
    def say(self, content):
        print(content)
planguage = Planguage("java官网", "https://www.orcle.com")
#先定义一个函数
def info(self):
    print("---info函数--------",self)
#使用info对planguage的foo方法赋值
planguage.foo = info
planguage.foo(planguage)
planguage.bar = lambda self: print('--lambda表达式--',self)
planguage.ber(planguage)
#self
class Person:
    def __init__(self):
        print("正在执行构造方法")
    def study(self,name):
        print(name,"正在学习python")
#实例2
 class Person:
        def __init__(self):
            print("正在执行构造方法")

        def study(self, name):
            print(name, "正在学习python")
zhangsan = Person()
zhangsan.study()
lisi = Person()
lisi.study()
#构造参数
class Person:
    name = "xxx"
    def __init__(self,name):
zhangsan = Person("zhangsan")
print(zhangsan.name)

lisi = Person("lisi")
print(lisi.name)


