#变量类类属性
class Address:
    detail = "会员制餐厅"
    post_code = "下北泽"
    def info(self,content):
        print(content)

address = Address()
Address.handset = '114514'
print(address.handset)

#实例变量
class Computer:
    cpu = '英特尔奔腾G6450'
    motherboard = "微星(mis)MAG B460"
      def_init_(self):
      self.cpu = "i9-13900HX"
      self.motherboard = "华硕GAMING B650M-PLAS"
      self.memory = "金士顿 16GB ddr4 3200"
       self.harddriver = "西部数据wd蓝盘 4TB stata6GB/s 1tb"
 def display(self):
     self.monitor = "明基 sw321c 32寸4K"
computer3 = Computer()
print(computer3.cpu,computer3.motherboard)

computer3.cpu = "i5-13400f"
computer3.motherboard = "技嘉小雕 pro z590"
print(computer3.cpu.computer3.motherboard)
print(Computer.cpu,Computer.motherboard)
computer3.videocard = '七彩虹 1660/2060 super 独立游戏显卡'
print(computer3.videocard)
#局部变量
class Computer:
    cpu = '英特尔奔腾G6450'
    motherboard = "微星(mis)MAG B460"
   def_init_(self):
   self.cpu = "i9-13900HX"
   self.motherboard = "华硕GAMING B650M-PLAS"
   self.memory = "金士顿 16GB ddr4 3200"
   self.harddriver = "西部数据wd蓝盘 4TB stata6GB/s 1tb"

   def display(self):
       self.monitor = '明基十五2IC32寸4K'

       def count(self,money):
           sale = 0.8 * money
           print("优惠后的价格",sale)

computer = Computer()
computer.count(8000)
#实例方法
class Bird:
    def_init_(self,name,clor,foot):
    self.name = name
    self.color = color
    self.foot = foot

    def fly(self):
        print(self,"实例方法 飞飞飞")

Bird.fly("zhangsan")
#类方法
class Bird:
    def_init_(self,name,clor,foot):
    self.name = name
    self.color = color
    self.foot = foot
 def fly(self):
     print(self.name + "实例方法 飞飞飞")
     @classmethod
     def eat(cls):
 print("内方法，吃吃吃",cls)
Bird.eat()
crow = Bird("乌鸦","黑色","2")
crow.eat()
#静态方法
class Bird:
    def_init_(self,name,clor,foot):
    self.name = name
    self.color = color
    self.foot = foot
 def fly(self):
     print(self.name + "实例方法 飞飞飞")
     @classmethod
     def eat(cls):
 print("内方法，吃吃吃",cls)
Bird.eat()
crow = Bird("乌鸦","黑色","2")
crow.eat()
@staticmethod
def cry(sound):
    print("静态方法" + sound)
    Bird.cry("咕咕咕")
    dove = Bird("灰鸽","灰色",2)
    dove.cry("咕咕咕")
#描述付
class RevealAccess:
    def_init_(self,initVal=None,name='var'):
    self.val = initVal
    self.name = name
    def_get_(self,obj,obJtype):
    print("Retrieving",self.name)
    return self.val
    def_set_(self,obj,val):
    print("updating",self.name)
    self.val = val

class MyClass:
    x = RevealAccess(10,'var "x')
    y = 5
m = MyClass()
print(m,x)
m.x = 20
print(m.x)
print(m.y)