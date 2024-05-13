class cat:
    pass

def walk(self):
    print('walk是实例方法')

@classmethod
def run(cls):
    print("run是方法")

@staticmethod
def jump():
    print("jump是静态方法")
cat.walk = walk
cat.run = run
cat.jump = jump
kitty = cat()
kitty.walk()
kitty.run()
kitty.jump()
garfield = cat()
garfield.walk = walk
cat(garfield)

cat.say = walk
dingdong = cat()
dingdong.name = '老八'
dingdong.say()

class cat:
    __slots__ = ('name','age','walk','run','jump')

class tiger(cat):
    pass
def walk(self):
    print('walk是实例方法',self.name)
@classmethod
def run(cls):
    print("run类是方法")

@staticmethod
def jump():
    print("jump是静态方法")
hodori = tiger()
hodori.name = "太极虎多礼"
hodori.say = walk
hodori.say(hodori)
#type()创建动态类
def say(self):
    print("不要拦着我，我要fuck you")
language = type("language",(object),dict(say=say, name="python"))

langs = language()
langs.say()
print(langs.name)

#metaclass元素
class languagemetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['name'] = "计算机编程语言"
        attrs['say'] = lambda self: print("调用say()实例方法")
        return super().__new__(cls,name,bases,attrs)
class pythonlanguage(object,metaclass=languagemetaclass):
    pass
python = pythonlanguage()
print(python.name)
python,say()