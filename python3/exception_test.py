
try:
    a = input("type a number:")
    b = input("type a another:")

    a = int(a)
    b = int(b)
    print(a / b)
#except ZeroDivisionError:
except(ZeroDivisionError, ValueError):
    print("Invalit error")

#Error caused by refferation of try variable
try:
    10 / 0
    c = "I well never get difined."
except ZeroDivisionError:
    print(c)
