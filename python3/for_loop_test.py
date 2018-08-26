name = "Ted"
for character in name:
    print(character)

shows = ["Got", "Narcos", "Vice"]
for show in shows:
    print(show)

print("\n")
itterable_tuple = ("this", "is", "tuple")
for i in itterable_tuple:
    print(i)

print("\n")
people = {"G Bluth 2": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny",
          }
for character in people:
    print(character)

print("\n")
#tv = ["GOT", "Narcos", "Vice"]
#i = 0
#for show in tv:
#    new = tv[i]
#    new = new.upper()
#    tv[i] = new
#    i += 1
tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    #print("loop start")
    #print("i =", i)
    #print("new =", new)
    new = tv[i]
    new = new.upper()
    tv[i] = new
    #print("loop end")
    #print("i =", i)
    #print("new =", new)
print(tv)


print("\n")
tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)
print(all_shows)


print("\n")
for i in range(1, 11):
    print(i)
#print(range(1, 11))
#low = range(1, 11)
#print(low)