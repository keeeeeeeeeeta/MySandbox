fruit = list()
print("fruit list is...")
print(fruit)
#new_list = ["a", "b", "c", "d"]
new_list = "abcde"
# not itterable obj to list method
#new_list = 123456
fruit = list(new_list)
print("fruit new list is...")
print(fruit)
#fruit = []
#fruit = ["Apple", "Orange", "Pear"]
#fruit

colors = ["purple", "orange", "green"]

print(colors)

guess = input("what color? (plz input):")

print(guess)

print(guess in colors)

if guess in colors:
    print("atari")
else:
    print("hazure")
