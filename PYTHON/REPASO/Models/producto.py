from enum import Enum

class Categoria(Enum):
    COCINA = 1
    SALON = 2
    TERRAZA = 3

class Color(Enum):
    BLANCO = 1
    NEGRO = 2
    MARRON = 3

class Producto():
    nombre: str
    precio: float
    categoria: Categoria
    coste: float
    color: Color

    def __init__(self, nombre:str, precio:float, categoria: Categoria, coste:float, color:Color):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria 
        self.coste = coste
        self.color = color


        
     
