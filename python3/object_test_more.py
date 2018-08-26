class Hoge:
    def __init__(self):
        self.name = "hoge name"

hoge = Hoge()
print("type test")
print(type(hoge))
print(hoge)
print("type string")
print(type("test string"))
print(100)
print(type(100))


class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))
        #print(self.width)

    def __repr__(self):
        return "{} by {}".format(self.width, self.length)


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)
r3 = Rectangle(1000, 2000)

print("r1 is ...")
r1.print_size()
print("r2 is ...")
r2.print_size()
print("r3 is ...")
r3.print_size()

print(Rectangle.recs)

print(r1)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)


class Person:
    def __init__(self):
        self.name = "Bob"

print("is keyword test")
bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(another_bob is bob)

x = 10
if x is None:
    print("x is None")
else:
    print("x is NOT None")

x = None
if x is None:
    print("x is None")
else:
    print("x is NOT None")

type_test = type
print(type_test)

test_obj = object()
print(type(test_obj))