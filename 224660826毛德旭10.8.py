class language:
    def __ceil__(self,name,add):
        print("调用——call--方法",name,add)

plangs = language()
plangs("python官网","http://www.python.org")

def say():
    print("python官网：http://www.python.org")

say()
say.__call__()

class language:
    def __init__(self):
        self.name = "python官网"
        self.add = "http://www.python.org"

    def say(self):
        print("我正在学习python")

plangs = language()
if hasattr(plangs,"name"):
    print(hasattr(plangs.name,"__call__"))
print("********")
if hasattr(plangs,"say"):
    print(hasattr(plangs.say,"__call__"))

class Myclass:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name:"+self.name+";age:"+str(self.age)
    __repr__=__str__
    def __it__(self, record):
        if self.age < record.age:
            return  True
        else:
            return False

    def __add__(self, record):
        return Myclass(self.name, self.age+record.age)
myc = Myclass("Anna",42)
myc1 = Myclass("Gary",23)
print(repr(myc))
print(myc)
print(str (myc))
print(myc < myc1)
print(myc+myc1)

class ListDemo:
    def __init__(self):
        self.__date=[]
        self.__step = 0
    def __next__(self):
        if self.__step <= 0:
            raise stopiteration
        self.__step -= 1
        return  self.__date[self.__step]
    def __iter__(self):
        return self
    def __setitem__(self,key,value):
        self.__date.insert(key.value)
        self.__step +=1
mylist = ListDemo()
mylist[0]=1
mylist[1]=2
for i in mylist:
    print (i)

class ListDemo:
    def __init__(self):
        self.__date=[]
        self.__step = 0
    def __setitem__(self,key,value):
        self.__date.insert(key,value)
        self.__step +=1

    def __call__(self):
        self.__step-=
        return self.__date[self.__step]


mylist = ListDemo()
mylist[0] =1
mylist[1] =2
a = iter(mylist,1)
print(a.__next__())
print(a.__next__())

def funA(fn):
    print("python官网")
    fn()
    print("http://www.python.oorg")
    return "装饰函数的返回值"
@funA
def funB():
    print("学习 python")
print(funB)

def funA(fn):
    def say(*arges,**kwargs):
        fn(*arges,**kwargs)
    return say
@funA
def funB(arc):
    print("python官网:",arc)

@funA
def other_funB(name,arc):
    print(name,arc)

funB("http://www.python.org")
other_funB("python官网：","http://www.python.org")