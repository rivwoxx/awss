nombres = ['Pepe', 'Augusto', "Mariano", 'Anastasia', 'Nancy', 'Grate', 'Mauricio']

for x in nombres:
    if x == 'Augusto':
        print('Dios')
        #break
        continue    ##si verdadero no muestres el valor (en este caso 'Augusto' y continua)
    print(x)


for i in range(1,8):    #imprime cada valor dentro del rango 
    print(i)

for l in 'I am the Walrus':      #imprime cada letra del string
    print(l)
 
 ##while

c = 5
while c <= 100:
    print(c)
    c = c + 10

m = 1
while m < 100:
    m = m + 1
    if m == 50:
        print('Hey Ya!')
        continue    
        #  break
    print(m)
    