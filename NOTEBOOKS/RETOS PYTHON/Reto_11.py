#Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
#NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
#El programa debe mostrar las siguientes opciones para que escoja el usuario:
#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa

class Cliente():
  nombre:str
  apellidos:str
  nif:str
  telefono:str
  email:str
  preferente:bool

  def __init__(self, nombre, apellidos, nif, telefono, email, preferente):
    
      self.nombre = nombre
      self.apellidos = apellidos
      self.nif = nif
      self.telefono = telefono
      self.email = email
      self.preferente = preferente
    
  clientes = []

  def add (self, nombre, apellidos, nif, telefono, email, preferente):
      self.nombre = input("Añade el nombre del cliente: ")
      self.apellidos = input("Añade los apellidos del cliente: ")
      self.nif = input("Añade el NIF del cliente: ")
      self.telefono = input("Añade el teléfono del cliente: ")
      self.email = input("Añade el email del cliente: ")
      self.preferente = input("Escribe True si es un cliente preferente o False si no lo es: ")
        
