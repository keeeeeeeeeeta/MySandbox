class TestLt:
    def __init__(self, test_str):
        self.str = test_str

#    def __gt__(self, another_one):
#        if "A" in self.str and "A" in another_one.str:
#            return True
#        else:
#            return False
    def __lt__(self, another_one):
        if ("A" in self.str) and ("A" in another_one.str):
            print("in if")
            return True
        else:
            print("in else")
            return False

first_int = 10
second_int = 20
print(first_int < second_int)

first_str = TestLt("Aoao")
second_str = TestLt("asdf")
print(first_str < second_str)

import this


#from random import shuffle
#
#
#fuga = ["a", "b", "c"]
#arg = 1
#print(fuga[arg])
#
#print("fuga is ...", fuga)
#shuffle(fuga)
#print("After shuffle, fuga is ...", fuga)

#class TestClass:
#    def __init__(self):
#        pass
#
#print(type("hoge"))
#print(type(type("hoge")))
#print(type(100))
#print(type(100.0))
#
#test_class = TestClass()
#print(type(test_class))
#isinstance(test_class, TestClass)

#import module
#print("this is in test.py")
#print(module.check_str)


#char = input("input one char:")
#while  len(char) != 1:
#    print("input ONLY one char")
#    char = input("input one char:")
#char = input("input one char:")
#while  len( input("input one char:") ) != 1:
#    print("you input char is ...", )
#    print("input ONLY one char")
#    char = input("input one char:")

#test = ["a", "b", "c"]
#print("Nanbanme", test.index("b"))



#def oya_func():
#    lists = ["a", "b", "c"]
#    digit = 2
##    print("In oya_func", lists[0:digit])
#    ko_func(lists, digit)
#
#
#def ko_func(lists, digit):
#    print("hoge")
#    print("In ko_func", lists[0:digit])
#
#oya_func()