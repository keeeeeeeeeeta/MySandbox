import csv
import os

print(os.getcwd())

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        #print(row)
        print(",".join(row))

list1 = ["Top Gun", "Risky Buisiness", "Minority Report"]
list2 = ["Titanic", "The Revenant", "Inception"]
list3 = ["Training Day", "Man on Fire", "Flight"]
lists = [list1, list2, list3]

with open("challenge.csv", "w",newline='', encoding="utf-8") as file_obj:
    csv_obj = csv.writer(file_obj, delimiter=",")
    for i in lists:
        csv_obj.writerow(i)
