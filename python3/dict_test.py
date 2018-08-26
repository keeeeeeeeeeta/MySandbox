#my_dict = dict()
my_dict = {}
print(my_dict)

fruits = {"Apple": "Red",
          "Banana": "Yellow"}
print(fruits)

facts = dict()

# add value
facts["code"] = "fun"
# reffer by key
print(facts["code"])

# add value
facts["Bill"] = "Gates"
# reffer by key
print(facts["Bill"])

# add value
facts["founded"] = 1776
# reffer by key
print(facts["founded"])

print(facts)

print("code" in facts)

# test reffer by not existed key
#print(facts["bILL"])

# test delete key value pair
del facts["founded"]
print(facts)

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"
         }
n = input("enter number:")
if n in songs:
    #song = songs[n]
    #print(song)
    print(songs[n])
else:
    print("not match")