class DemoClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute


demo1 = DemoClass("abc")
demo2 = DemoClass("xyz")

print(demo1.number, demo1.instances_created)
print(demo2.number, demo2.instances_created)


class nonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        print("__init__()")
        super().__init__()


print(type(nonZero(-12)))
print(type(nonZero(0)))


class language:
    pass


plangs = language()
print(plangs)


class language:
    def _init_(self):
        self.name = "python官网"
        self.address = "https://www.python.org"

    def _repr_(self):
        return "language[name="
        self.name + ".address=" + self.address + ",]"


plangs = language()
print(plangs)


class Language:
    def _init_(self):
        print("调用 _init_() 方法构造对象")

    def _del_(self):
        print("调用__del__() 销毁对象 释放空间")


plangs = Language()


del plangs


class language:
    def _init_(self):
        print("调用 __init__ 方法构造对象")

    def __del__(self):
        print("调用 _del_() 销毁对象，释放其空间")


plangs = language()

cl = plangs
del plangs
print("********")


class langugae:
    def __del__(self):
        print("调用父类 _del_() 方法")


class cl(language):
    def __del__(self):
        print("调用子类 _del_() 方法")


c = cl()
del c

class Language:
    def __init__(self,):
        self.name="Python官网"
        self.add="http://www.python.org"
    def say(self):
        pass

plangs=Language()
print(dir(plangs))
#
class Language:
    def __init__(self,):
        self.name="Python官网"
        self.add="http://www.python.org"

    def say(self):
        pass

plangs=Language()
print(plangs.__dir__())
#
class Language:
    a=1
    b=2

    def __init__(self,):
        self.name="Python官网"
        self.address="http://www.python.org"
    def say(self):
        pass

print(Language.__dict__)
plangs=Language()
print(plangs.__dict__)
#
class Language:
    a=1
    b=2
    def __init__(self,):
        self.name="Python官网"
        self.address="http://www.python.org"

class Java(Language):
    c=1
    d=2
    def __init__(self):
        self.na="Java官网"
        self.addr="http://www.oracle.com"

print(Language.__dict__)
print(Java.__dict__)

plangs=Language()
print(plangs.__dict__)

java=Java()
print(java.__dict__)
#
class Language:
    a="编程语言"
    b=2

    def __init__(self,):
        self.name="Python官网"
        self.address="http://www.python.org"

plangs=Language()
print(plangs.__dict__)
plangs.__dict__['name']="Python学习"
print(plangs.name)
#
class Language:
    def __init__(self):
        self.name="Python官网"
        self.add="http://www.python.org"

    def say(self):
        print("我正在学Python")

plangs=Language()
print(hasattr(plangs,"name"))
print(hasattr(plangs,"add"))
print(hasattr(plangs,"say"))
#
class Language:
    def __init__(self):
        self.name="Python官网"
        self.add="http://www.python.org"
    def say(self):
        print("我正在学Python")

plangs=Language()
print(getattr(plangs,"name"))
print(getattr(plangs,"add"))
print(getattr(plangs,"say"))
print(getattr(plangs,"display",'nodisplay'))
#
class Language:
    def __init__ (self):
        self.name='python官网'
        self.add='http://www.python.org'
    def say(self):
        print('我正在学习python')
plangs=Language()
print(plangs.name)
print(plangs.add)

setattr(plangs,'name','swift语言')
setattr(plangs,'add','http://swift.org/')

print(plangs.name)
print(plangs.add)
#
def say(self):
    print("我正在学Python")

class Language:
    def __init__(self):
        self.name="Python官网"
        self.add="http://www.python.org"

plangs=Language()
print(plangs.name)
print(plangs.add)

setattr(plangs,"name",say)
plangs.name(plangs)

def say(self):
    print('我正在学python')
class Language:
    pass
plangs = Language()
setattr(plangs,"name",'Python官网')
setattr(plangs,'say',say)

print(plangs.name)
plangs.say(plangs)

hello = 'Hello';
print('"Hello"是str类的实例：', isinstance(hello,str))
print('"Hello"是object类的实例：', isinstance(hello,object))
print('"Hello"是object类的子类：', issubclass(str,object))
print('"Hello"是否是tuple类的实例：', isinstance(hello,tuple))
print('str是否是tuple类的子类：', issubclass(str,tuple))
my_list = [2,4]
print('[2,4]是否是list类的实例：',isinstance(my_list, list))
print('[2,4]是否是object类及其子类的实例：',isinstance(my_list, object))
print('[2,4]是否是object类的子类：',issubclass(list, object))
print('[2,4]是否是tuple类及其子类的实例：',isinstance([2,4], tuple))
print('list是否是tuple类的子类：',issubclass(list, tuple))

data = (20, 'fkit')
print('data是否为列表或元组：', isinstance(data, (list,  tuple)))
print('str是否为list或tuple的子类：', issubclass(str,  (list,  tuple)))
print('str是否为list或tuple或object的子类',issubclass(str, (list, tuple, object)))

class A:
    pass
class B:
    pass
class C(A,B):
    pass
print('类A的所有父类：', A.__bases__)
print('类B的所有父类：', B.__bases__)
print('类C的所有父类：', C.__bases__)
print('类A的所有父类：', A.__subclasses__())
print('类B的所有父类：', B.__subclasses__())

class Language:
    def __call__(self,name,add):
        print('调用__call__()方法',name,add)
plangs = Language()
plangs('Python官网','http://www.python.org')
plangs.__call__('Python官网','http://www.python.org')

def say():
    print('Python官网','http://www.python.org')

say()
say.__call__()

class Language:
    def __init__(self):
        self.name = 'Python官网'
        self.add = 'http://www.python.org'

    def say(self):
        print('我正在学Python')
plangs = Language()
if hasattr(plangs,'name'):
    print(hasattr(plangs.name,'__call__'))
print('**********')
if hasattr(plangs,'say'):
    print(hasattr(plangs.say,'__call__'))
