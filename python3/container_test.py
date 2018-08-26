lists = []

rap = ["canie", "Jay-Z", "Eminem", "Nazz"]
rock = ["Bob diran", "the beatles", "Red Zeppelin"]
djs = ["Zess dead", "tiest"]

#lists.append(2)
#lists.append("hoge")

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
print(rap)
#hoge = lists[0]
#print(hoge)

rap = lists[0]
rap.append("Kendric Rammer")
print(rap)
print(lists)



# test for tuple and list
locations = []

la = (34.0522, 199.234234)
chicago = (41.83242, 87.2131)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["Edgar", "Charles"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)

#authors.append("hoge")
#del authors[eights]
#del authors[0]
print(authors[0])



# test for tuple, list, and dictoinary
bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}
print("it is dictionary", bday)
my_list = [bday]
print("it is list", my_list)
print("it is list in other way", my_list[0])
my_tuple = (bday,)
print("it is tuple", my_tuple)
print("it is tuple in other way", my_tuple[0])

ny = {
    "Zahyo": (40.4214, 74.0059),
    "Celeb": [
        "Uddy arren",
        "Jay Z",
        "Kevin Bacon",
    ],
    "facts":{
        "Syu": "New york",
        "country": "America",
    }
}

print(ny)
print("Zahyo is...", ny["Zahyo"])
print("Celeb is...", ny["Celeb"])
print("facts is...", ny["facts"])