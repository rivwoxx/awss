demo = [1, "Hello", 1.34, True,  [1,2,3]]
colors =['red', 'yellow', 'blue']

numbers = list((1,2,3,4))  #pasamos una tuple, una tuple lo convierte como si fuera un solo elemento

print(numbers)

r = list(range(0,1000,10))      #range (inicio,fin,paso)
print(r)

print(type(colors))         #typo de la lista

print(len(r))           #mestra la longitud de la lista
print(r[7])             #muestra el valor n dentro de la lista

print(5 in r)         #5 esta dentro de la lista r?
print(50 in r)
print(colors)
print('green' in colors)

colors[1] = 'green'
print(colors)
print(dir(colors))       #muestra método de la lista
colors.append('brown')
print(colors)
colors.extend(['yellow', 'pink', 'black'])
print(colors)

colors.insert(2,'violet')   #inserta valor en posicion '2' (puede ser 0,1,2,3...bla) en la lista colors
print(colors)

colors.pop()    #quita ultimo valor de lista
print(colors)

colors.pop(3)        #quita la posicion 3
colors.pop(0)
colors.pop(2)
print(colors)

colors.remove('green')      #quita valor de la lista
print(colors)

colors.sort()       #ordenalos alfabt
print(colors)       

colors.sort(reverse=True)
print(colors)

print(colors.index('yellow'))       #posicion de yellow
print(colors.index('pink'))

print(r.count(50))      #cuantas veces aparece valor en una lista

colors.clear()      #limpia la lista
print(colors)