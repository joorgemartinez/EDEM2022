#Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
#NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
#El programa debe mostrar las siguientes opciones para que escoja el usuario:
#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa

import csv
import errno

clientes = {}


print('''#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS os clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa''')

opcion_elegida = input("Elija una de las opciones mostradas:")

while opcion_elegida != '6':

    #Si la opción elegida es la 1, añadiremos un nuevo diccionario al diccionario de clientes.

    if opcion_elegida == '1':
        nif = input("Introduzca su NIF: ")
        nombre = input("Introduzca su nombre: ")
        apellidos = input("Introduzca sus apellidos: ")
        tlf = input("Introduzca su teléfono: ")
        email = input("Introduzca su email: ")
        preferente = (input("¿Ha contratado usted el servicio preferente? Indique Si o No: "))
        
        #Mediante otro bucle while, tomamos la variable "preferente" como un boolean, dado que por el input cualquier valor non-empty sera True
        while True:
            if preferente.lower() != "si" and preferente.lower() != "no":
                print ("Lo siento, debe responder Sí o No")
                preferente = (input("¿Ha contratado usted el servicio preferente? Indique Si o No: "))
                continue

            elif preferente.lower() == "si":
                preferente = True
                break

            else:
                preferente = False
                break

        cliente = {"Nombre": nombre, "Apellidos": apellidos, "Teléfono" : tlf, "Email": email, "Preferente": preferente}

        #Actualizamos el diccionario utilizando como clave el NIF y como valor el diccionario con sus datos.
        clientes[nif] = cliente

        #Incluimos los datos de los clientes en un archivo.csv en el que la clave será el NIF y el valor cada diccionario.
        with open('clientes.csv', 'w') as f:  
            writer = csv.writer(f)
            for k, v in clientes.items():
                writer.writerow([k, v])

    #Si elige la opción 2, el cliente puede borrar cualquier cliente mediante la clave de su NIF.
    if opcion_elegida == '2':
        nif = input("Introduzca el NIF del cliente que desea borrar: ")
        if nif in clientes:
            del clientes[nif]

            #Actualizamos el archivo .csv, retirando el cliente eliminado de la base de datos.
            with open('clientes.csv', 'w') as f:  
                writer = csv.writer(f)
                for k, v in clientes.items():
                    writer.writerow([k, v])
        else:
            print (f"Lo siento, no existe ningún cliente con el NIF: {nif}")

    if opcion_elegida == '3':
        nif = input("Introduzca el NIF del cliente que desea mostrar: ")
        if nif in clientes:
            print(clientes[nif])
        else:
             print(f"Lo siento, no existe ningún cliente con el NIF: {nif}")

    if opcion_elegida == '4':
        print (clientes)


    if opcion_elegida == '5':
        for value in clientes.items():
            if value["Preferente"] == "True": #Error
                clientes_preferentes = clientes
                print(clientes_preferentes)
                
                
                with open('clientes_VIP.csv', 'w') as f:  
                    writer = csv.writer(f)
                    for k,v in clientes_preferentes.items():
                        writer.writerow([k, v])
                
                break

    opcion_elegida = input("Elija otra de las opciones del menú:")

print ("Programa Finalizado")
    



