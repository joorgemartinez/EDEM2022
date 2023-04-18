#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

import math

height = int(input("Inserte la altura del trángulo en cm: "))
base = int(input("Inserte la base del triángulo en cm: "))
  
def area_triangulo (a:float,b:float):
  return (a*b*0.5)


print(f'El área del triángulo es {area_triangulo(a = height,b = base)} cm\xb2')

radius = int(input("Inserte el radio del círculo en cm: "))
def area_circulo (r:float):
  return (r**2*math.pi)

print(f'El área del círculo es {area_circulo(r=radius)} cm\xb2')

  