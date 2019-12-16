t = (1,2,3,4)
print('Tuplas no puedes cambiar su valor, listas si')
print(type(t))
print(t)
print(dir(t))   #muestra metodos de una tuple

#si solo ponemos un solo dato no se considera como tuple sino como dato 
a = (2)
print(a)
print(type(a))

#ejemplo de uso
#usamos la tuple para definir, por ejemplo, latitud y longitud de una ciudad [ojo! los datos de ahi no son correcto o si no lo se]
loc = {
    (32.55, 36.69):"CDMX",
    (25.69,89.66):"NYC"
}

print(loc)