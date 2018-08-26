x = 10
while x > 0:
    #print('{}'.format(x))
    print(x)
    x -= 1
print("Happy New Year!")

#for i in range(0, 10):
#    print(i)
#    break

#while True:
#    print("Infinite loop")

# test for break
#qs = ["What is you name?",
#      "What is your fav. color?",
#      "What is your quest?"]
#n = 0
#while True:
#    print("Type q to quit")
#    a = input(qs[n])
#    if a == "q":
#        print("It will stop")
#        break
#    n = (n + 1) % 3

# test for continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

print("/n")
print("new line")
print("/n")

for i in range(1, 3):
    print(i)
    for letter in ("a", "b", "c"):
        print(letter)

print("/n")
print("new line")
print("/n")

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

#while input("y or n?") != "n":
#    for i in range(1, 6):
#        print(i)

challenge_list = ["walking dead", "antrage", "the soplanos", "vanpire diarys"]
for i in range(0, len(challenge_list)):
    print(challenge_list[i])

answer = [4, 6, 9]
while True:
    enter = input("Input your answer.(quit to q)")
    
    if enter == "q":
        print("It will stop")
        break

    try:
        enter = int(enter)
    except ValueError:
        print("Plz input integer, again")
        continue

    if enter in answer:
        print("Match!!!")
        break
    else:
        print("Not match...")