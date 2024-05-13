class Circular:
    #定义构造法
    def _init_(self, radius):
         self._radius = radius
    def setRadius(selfself,radius):
          self._radius = radius
    def getRadius(self):
        return self._radius
    def delRadius(self):
        self._radius = 0, 0
    radius = property(getRadius,setRadius,delRadius,'用于描述园的半径属性')

   # print(Circular.radius._doc_)
   # help(Circular.radius)
   Circular = Circular(10);
print(Circular.radius)
Circular.radius = 20
print(Circular.radius)
del Circular.radius
print(Circular.radius)
print(dir(Circular))
#封装
class User:
    def setName(selfself,name):
        if len(name) < 3:
            raise ValueError('名称长度必须大于3')
            self._name = name
def getName(self):
    return self._name
    name = property(getName, setName)
    def setAddress(self, address):
        if address.startswitch("http://"):
            self._address = address
        else:
            raise ValueError("地址必须为 http://开头")

    def getAddress(self):
        return self._address

    address = property(getName, setAddress)
    def_display(self):
       print(self._name, self._address)

user = User()
user.name = "Guido"
user.address = "http://www.python.org"
print(user.name)
print(user.address)
#继承
class People:
    def say(self):
        print("我是一个人，名字是:",self.name)
class Animal:
    def display(self):
        print("人也是高级动物")
 clss perosn(People, Animal):
        pass

zhangsan = perosn()
zhangsan.name = "张三"
zhangsan.say()
zhangsan.display()
#多继承
class people:
    def _init_(self):
        self.name = people
    def say(self):
        print("people类",self.name)

class Animal:
    def __init__(self):
        self.name = Animal
    def say(self):
        print("Animal类",self.name)

class person(people, Animal):
    pass

zhangsan = person()
zhangsan.name = "张三"
zhangsan.say()
#方法重写
class bird:
    def iswing(self):
        print("鸟有翅膀")

    def fly(self):
        print("鸟会飞")

class ostrich(bird):
    def fly(self):
        print("鸵鸟不会飞")

ostrich = ostrich()
bird.fly(ostrich)

#super
class dark:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("我是人，名字为：",self.name)

class animal:
    def __init__(self,food):
        self.food = food
    def display(self):
        print("我是老八，我吃",self.food)

class person(dark, animal):
    def __init__(self,name,food):
        super().__init__(name)


per = person("张三","素食")
per.say()
per.display()
