# Given a string and an int n, 
# remove characters from string starting from zero up to n and return a new string

def s4(str,x):
    if x < len(str):
        return str[x:]
    else:
        return print ('Number must be smaller than String')
        
    
str = input("Give me a String: ")
x = int(input("Give me a Number: "))

s = s4(str,x)

print(s)