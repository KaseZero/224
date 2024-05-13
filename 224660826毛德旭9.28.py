class java:
    def say(self):
        print("java类的say方法")

class python:
    def say(self):
        print("python类的say方法")

a = java()
a.say()

a = python
a.say()

class language:
    def say(self):
        print("langhage类的say方法")
class java(python):
    def say(self):
        print("java类的say方法")
class python(language):
    def say(self):
        print("puthon类的say方法")

a = language()
a.say()
a = java()
a.say()
a = python()
a.say()

class language:
    def say(self):
        print("langhage类的say方法")
class java(python):
    def say(self):
        print("java类的say方法")
class python(language):
    def say(self):
        print("puthon类的say方法")
class whosay:
    def say(self,who):
        who.say()

a = whosay()
a.say(language())
a.say(java())
a.say(python())
