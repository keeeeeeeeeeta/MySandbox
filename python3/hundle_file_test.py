import os

os.path.join("C:", "Users", "Keita","AppData", "Local", "Programs", "Python", "Python37", "st.txt")

#st = open("st.txt", "w", encoding="utf-8")
#st.write("Pythonからこんちには")
#st.close()

#with open("st.txt", "w", encoding="utf-8") as f:
#    f.write("Pythonからこんにちは")

#with open("st.txt", "r", encoding="utf-8") as f:
#    print(f.read())

my_list = []
with open("st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())
print(my_list)
print(len(my_list))

print(os.getcwd())
with open("cubed.py", "r", encoding="utf-8") as target_file:
    print(target_file.read())
    