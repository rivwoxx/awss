#if
x = input("give me a number: ")
y = input("give me a color: ")
x = int(x)

if x < 30:
    print(str(x) + " is less than 30")
elif x == 30:
    print(str(x) + " is equal than 30")
else:
    print(str(x) + " is more than 30")

if x > 2 or x < 100:        #con operadores, and ,or, not etc
    print("meh") 
else:
    print("yeah")

if y == "red":
    print(str(x))
else:
    print(y)


