'''Площадь квадрата'''

import math
def square(side):
    b = math.ceil(side*side)
    return b

side = 2

result = square(side) #название функции со скобками - не только вызов функции, но и ее значение (результат), если есть return

print("сторона = "+str(side)+", площадь = " +str(result))