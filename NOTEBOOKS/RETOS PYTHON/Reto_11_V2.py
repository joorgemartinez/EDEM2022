#Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
#NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
#El programa debe mostrar las siguientes opciones para que escoja el usuario:
#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa

clientes = {}

print('''#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa''')

opcion_elegida = int(input("Elija una de las opciones mostradas:"))

while opcion_elegida != 6:

    #Si la opción elegida es la 1, añadiremos un nuevo diccionario al diccionario de clientes.

    if opcion_elegida == 1:
        nif = input("Introduzca su NIF: ")
        nombre = input("Introduzca su nombre: ")
        apellidos = input("Introduzca sus apellidos: ")
        tlf = input("Introduzca su teléfono: ")
        email = input("Introduzca su email: ")
        preferente = bool(input("¿Ha contratado usted el servicio preferente? Indique Sí o No: "))
        cliente = {"Nombre": nombre, "Apellidos": apellidos, "Teléfono" : tlf, "Email": email, "Preferente": preferente}

        #Actualizamos el diccionario utilizando como clave el NIF y como valor el diccionario con sus datos.
        clientes[nif] = cliente

    if opcion_elegida == 2:
        nif = input("Introduzca el NIF del cliente que desea borrar: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print (f"Lo siento, no existe ningún cliente con el NIF: {nif}")

    if opcion_elegida == 3:
        nif = input("Introduzca el NIF del cliente que desea borrar: ")
        if nif in clientes:
            print(clientes[nif])
        else:
             print (f"Lo siento, no existe ningún cliente con el NIF: {nif}")




    opcion_elegida = int(input("Elija otra de las opciones del menú:"))

    




