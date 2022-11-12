#Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.


import math

height = float(input("Inserte la altura del cilindro en cm: "))
radius = float(input("Inserte el radio del cilindro en cm: "))
  
def area_circulo (r:float):
    return (r**2*math.pi)

def volumen_cilindro (r:float, h:float):
    return area_circulo(r) * h

print(f'El volumen del cilindro es {volumen_cilindro(r = radius,h = height)} cm\xb3')