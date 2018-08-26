long_str = """line one
              line two
              line three
           """
print(long_str)

author = "Kafka"
print(author)
#print(author[0])
#print(author[1])
#print(author[2])
#print(author[3])
#print(author[4])

#test for index out of range
#print(author[5])

#print(author[-1])
#print(author[-2])
#print(author[-3])
#print(author[-4])
#print(author[-5])

#doramer = "Sisido" + "kafka"
#doramer = "Sisido" * 3
doramer = "Sisido".upper()
#doramer = "Ｓｉｓｉｄｏ".upper()
print(doramer)

band = "RIZE".lower()
print(band)

sentense = "long sentence can change initial char.".capitalize()
print(sentense)

#format_test = "hello, {}".format("name")
#name = "Mr.Lorense"
#print("Enter your name:")
#name = input("Enter your name:")
#format_test = "hello, {}. This is practise".format(name)
#print(format_test)

muliple_format = "one {}, two {}, three {}".format(1, 2, 3)
print(muliple_format)

split_test = "split test. Sep by comma. Third sentence.".split(".")
print(split_test)
print(len(split_test))

print("")
print("new line for console viewable")
print("")

first_three = "abc"
result = "+".join(first_three)
print(first_three)
print(result)

# from list obh of str to str obh
words = ["The", "fox", "capture", "plan", "."]
#marged_words = "".join(words)
marged_words = " ".join(words)
print(marged_words)

print("")
print("new line for console viewable")
print("")

#s = "     hoge    "
# include Japanese Zenkaku space
s = "   　  hoge  　  "
s = s.strip()
print(s)

# replace test
replace_test = "Like a angele"
replace_test = replace_test.replace("a", "@")
print(replace_test)

# index test
index_test = "abcderg"
# substring not found test
#index_num = index_test.index("h")
try:
    index_num = index_test.index("b")
except:
    print("Not found.")
print("b is at", index_num)

# including test
result = "Cat" in "Cat in the hat."
print(result)

# escape test
#error_str = "She said, "Yes..." again and again"
error_str = 'She said, "Yes..." again and again'
#error_str = "She said, \"Yes...\" again and again"
print(error_str)

# new line test
long_str = "line1\nline2\nline3"
print(long_str)

# slice test
fict = ["Torstoi", "Camu", "Owel", "Haksury", "Oustin"]
print(fict[0:3])
ivan = "死の代わりにひとつの光があった。"
#print(ivan[0:6])
print(ivan[:6])
#print(ivan[6:16])
print(ivan[6:])

new_ivan = ivan[:]
print(new_ivan)

# challenge
target_str = "Camu"
print(target_str[0])
print(target_str[1])
print(target_str[2])
print(target_str[3])

#first_input = input("Plz input 1st str")
#second_input = input("Plz input 2nd str")
#print("1st one is {}. 2nd one is {}. That is all.".format(first_input, second_input))

target = "Hemingway"
whare = target.index("m")
print(whare)

target = "three "
print(target+target+target)
print(target*3)

slice_target ="四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(slice_target[:10])

# format test
# like bash style
test_str = "hoge"
print("If bash, $hoge this can execute without any problem.")
print("If bash, $hoge this can execute without any problem.", test_str)
print("If bash, $hoge this can execute without any problem.",test_str)
print("If bash, $hoge this can execute without any problem." + test_str)