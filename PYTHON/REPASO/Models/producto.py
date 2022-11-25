from enum import Enum

class Categoria(Enum):
    COCINA = 1
    SALON = 2
    

class Producto():
    nombre: str
    precio: float
    categoria: str
