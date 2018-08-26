class Orange:
    def __init__(self, w, c):
        """weight is gram"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, tmp):
        """tmp is c"""
        self.mold = days * tmp

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length

    def change_size(self, w, l):
        self.width = w
        self.length = l

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, num):
        self.nums[index] = num

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._private = "unsafe"
    
    def public_method(self):
        # it can be used by 'client'
        #pass
        print("This is puclib_method")
    
    def _private_method(self):
        # it can NOT be used by 'client'
        #pass
        print("This is _private_method")

class TestInheritance(PublicPrivateExample):
    def __init__(self):
        PublicPrivateExample.__init__(self)
        self.name = "me"

    def public_method(self):
        print("This is NEW public_method")
    
    def test_method(self):
        hoge = [self.public, self._private]
        return hoge
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def sing(self):
        print("Bowow!")

class Person:
    def __init__(self, name):
        self.name = name
    
    def sing(self):
        print("Woooooo!!!!")


orl = Orange(10, "dark orange")
print(orl.mold)
orl.rot(10, 200)
print(orl.mold)

rectangle = Rectangle(10, 200)
print("Now area is...", rectangle.area())
rectangle.change_size(1, 2)
print("And then, area is...", rectangle.area())

data = Data()
print(data.nums)
data.change_data(0, 100)
print(data.nums)

print("This is PublicPrivateExample test")
test_instance = PublicPrivateExample()
print(test_instance.public)
print(test_instance._private)

print("This is inheritance test")
#test_inheritance = PublicPrivateExample()
#print(test_inheritance.public)
test_inheritance = TestInheritance()
#print(test_inheritance.public)
test_inheritance.public_method()
#print(test_instance.public)
#test_inheritance._private_method()
print(test_inheritance.public)
#print(test_inheritance._private)
#print(test_inheritance.name)
print(test_inheritance._private)
print(test_inheritance.test_method())
print(test_inheritance.name)

#test for composition
mick = Person("Mick Jagger")
stan = Dog("Stanhanse", "Chi-wa-wa", mick)
print(stan.owner.name)
stan.owner.sing()
stan.sing()