#ejemplo de modulo
from datetime import date ##usar especificamente date de la librería datetime
import datetime
import fmath

print(datetime.date.today())
print(datetime.timedelta(milliseconds=500000000))
print(datetime.timedelta(seconds=3600))
print(date.today())

fmath.add(1,2)
fmath.res(2,1)