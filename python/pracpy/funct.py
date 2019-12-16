def sal(nom):
    print("hey " + nom)
    
def hey():
    print('hey')

def sum(a,b):
    c = a + b
    return c

hey()
sal('Augusto')

print(sum(26,20))

#funcion lambda
#A lambda function can take any number of arguments, but can only have one expression.
#lambda arguments : expression

res = lambda a,b: a - b
print(res(50,10))