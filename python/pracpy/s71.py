#Promediotron Ver3

def Promediotron(v):
    x = 0 
    p=0
    while(x < v):
        c = float(input("Teclea tu calificación: "))
        # if c > 10:
        #     raise Exception("Valor debe ser menor de 10")
            
        # else:
        #     p = p + c 
        #     x += 1
        p = p + c
        x += 1
    return p

try:
    v = int(input("Materias cursadas: "))
    pv = Promediotron(v)
    av = pv / v
    print(av)
except ValueError:
    v=0
    print('Debes escribir un valor entero.')

# try:
#     pv = Promediotron(v)
#     av = pv / v
#     print(av)
# except ZeroDivisionError:
#     print('Error')

