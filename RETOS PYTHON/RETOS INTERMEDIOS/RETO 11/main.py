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

clientes = {}
clientes_preferentes = {}

opcion_elegida = input('(1) Añadir un cliente \n(2) Eliminar cliente \n(3) Mostrar Cliente \n(4) Listar TODOS los clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nElija una de las opciones mostradas:')

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
        with open('/Users/jorgemartinezcanet/Documents/GitHub/EDEM2022/RETOS PYTHON/RETOS INTERMEDIOS/RETO 11/clientes.csv', 'w') as f:  
            writer = csv.writer(f)
            for k, v in clientes.items():
                writer.writerow([k, v])

    #Si elige la opción 2, el cliente puede borrar cualquier cliente mediante la clave de su NIF.
    if opcion_elegida == '2':
        nif = input("Introduzca el NIF del cliente que desea borrar: ")
        if nif in clientes:
            del clientes[nif]

            #Actualizamos el archivo .csv, retirando el cliente eliminado de la base de datos.
            with open('/Users/jorgemartinezcanet/Documents/GitHub/EDEM2022/RETOS PYTHON/RETOS INTERMEDIOS/RETO 11/clientes.csv', 'w') as f:  
                writer = csv.writer(f)
                for k, v in clientes.items():
                    writer.writerow([k, v])
        else:
            print (f"Lo siento, no existe ningún cliente con el NIF: {nif}")

    #Si elige la opción 3, podemos mostrar los datos de un cliente en concreto, utilizando la clave de su NIF.
    if opcion_elegida == '3':
        nif = input("Introduzca el NIF del cliente que desea mostrar: ")
        #Mediante una condición if, si el NIF es correcto, imprimiremos en un comentario multilínea los datos de ese cliente.
        if nif in clientes:

            print (f'''El cliente con NIF {nif} tiene los siguientes datos:
Nombre: {clientes[nif]['Nombre']} 
Apellidos: {clientes[nif]['Apellidos']}
Teléfono: {clientes[nif]['Teléfono']}
Email: {clientes[nif]['Email']}
Cliente Preferente: {clientes[nif]['Preferente']}''')

        #Si el NIF no corresponde a ningún cliente de nuestra base de datos, la consola devolverá un mensaje indicando que no existe.
        else:
             print(f"Lo siento, no existe ningún cliente con el NIF: {nif}")

    #Si elige la opción 4, podemos mostrar los datos de todos los clientes de la base de datos.
    if opcion_elegida == '4':

        #Mediante un bucle for iteramos por todos los clientes y los mostramos mediante un comentario multilínea.
        for key, value in clientes.items():
            print (f'''El cliente con NIF {key} tiene los siguientes datos:
Nombre: {value['Nombre']} 
Apellidos: {value['Apellidos']}
Teléfono: {value['Teléfono']}
Email: {value['Email']}
Cliente Preferente: {value['Preferente']}''')
            print ('--------------------------------')

    #Si elige la opción 5, podemos mostrar los datos de todos los clientes preferentes.
    if opcion_elegida == '5':

        #Mediante un bucle for iteramos por todos los clientes.
        for key, value in clientes.items():
            #Mediante un condicional (if), indicamos que deben imprimirse por consola únicamente los clientes preferentes. 
            if value['Preferente'] == True:
                print(f'''El cliente con NIF {key} tiene los siguientes datos:
Nombre: {value['Nombre']} 
Apellidos: {value['Apellidos']}
Teléfono: {value['Teléfono']}
Email: {value['Email']}
Cliente Preferente: {value['Preferente']}''')
                print ('--------------------------------')
            

    opcion_elegida = input("(1) Añadir un cliente \n(2) Eliminar cliente \n(3) Mostrar Cliente \n(4) Listar TODOS los clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nElija una de las opciones mostradas:")

print ("Programa Finalizado")
    



