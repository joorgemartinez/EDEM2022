#Una tienda vende Discos de música . Con la idea de vender un stock almacenado durante meses, se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.
#Cada disco (usa un diccionario para esto) tendrá:
#Nombre
#Artista
#Año
#Precio
#Género (solo pueden ser de los siguientes)
#Pop
#Electro
#Reggaeton
#Rock
#Metal
#Death Metal
#Black Metal
#Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.
#Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final de la compra.


from datetime import datetime as dt
  
thriller = {
    'Nombre' : 'Thriller',
    'Artista' : 'Michael Jackson',
    'Año' : 1995,
    'Precio' : 20, 
    'Género' : 'Pop'
     }
microdosis = {
    'Nombre' : 'Microdosis',
    'Artista' : 'Mora',
    'Año' : 2022,
    'Precio' : 18, 
    'Género' : 'Reggaeton'
     }
filosofem = {
    'Nombre' : 'Filosofem',
    'Artista' : 'Burzum',
    'Año' : 1996,
    'Precio' : 16, 
    'Género' : 'Black Metal'
     }
computerwelt = {
    'Nombre' : 'Computerwelt',
    'Artista' : 'Kraftwerk',
    'Año' : 1981,
    'Precio' : 17, 
    'Género' : 'Electro'
     }
ferxxo = {
    'Nombre' : 'Feliz Cumpleaños Ferxxo',
    'Artista' : 'Feid',
    'Año' : 2022,
    'Precio' : 22, 
    'Género' : 'Reggaeton'
     }
hotel_california = {
    'Nombre' : 'Hotel California',
    'Artista' : 'Eagles',
    'Año' : 1976,
    'Precio' : 16, 
    'Género' : 'Rock'
     }

print(f'Los discos que puede elegir son los siguientes: \n1. {thriller["Nombre"]} de {thriller["Artista"]} \n2. {microdosis["Nombre"]} de {microdosis["Artista"]}  \n3. {filosofem["Nombre"]} de {filosofem["Artista"]} \n4. {computerwelt["Nombre"]} de {computerwelt["Artista"]} \n5. {ferxxo["Nombre"]} de {ferxxo["Artista"]} \n6. {hotel_california["Nombre"]} de {hotel_california["Artista"]}')

disco = input ('¿Qué disco desea elegir? Indique el número: ')

if disco == "1":
    disco_elegido = thriller
    print(f"Buenísima elección! Ha elegido usted {disco_elegido['Nombre']} de {disco_elegido['Artista']} ")
elif disco == '2':
    disco_elegido = microdosis
    print(f"Buenísima elección! Ha elegido usted {disco_elegido['Nombre']} de {disco_elegido['Artista']} ")
elif disco == "3":
    disco_elegido = filosofem
    filosofem.update({'Precio': 0.7*16})
    print(f"Buenísima elección! Ha elegido usted {disco_elegido['Nombre']} de {disco_elegido['Artista']} ")
elif disco == "4":
    disco_elegido = computerwelt
    computerwelt.update({'Precio': 0.7*17})
    print(f"Buenísima elección! Ha elegido usted {disco_elegido['Nombre']} de {disco_elegido['Artista']} ")
elif disco == '5':
    disco_elegido = ferxxo
    print(f"Buenísima elección! Ha elegido usted {disco_elegido['Nombre']} de {disco_elegido['Artista']} ")
elif disco == '6':
    disco_elegido = hotel_california
    print(f"Buenísima elección! Ha elegido usted {disco_elegido['Nombre']} de {disco_elegido['Artista']} ")
else: 
    print ("Lo sentimos. Ha elegido un disco que no tenemos en stock")
    exit()

ticket = int(input('Si ya ha terminado su compra, por favor, pulse el número 0: '))
fecha = dt.now().strftime("%d, %B, %Y")


if ticket == 0:
    print ("TICKET DE COMPRA")
    print(f'Fecha de compra: {fecha}')
    print(f'Disco elegido: {disco_elegido["Nombre"]}') 
    print(f'Artista: {disco_elegido["Artista"]}')
    print(f'Total a pagar: {round(disco_elegido[("Precio")],2)}€')
    if disco_elegido == filosofem:
      print ("El dinero ahorrado ha sido de: " + str(0.3*16) + "€")
    elif disco_elegido == computerwelt:
      print ("El dinero ahorrado ha sido de: " + str(0.3*17)+ "€")
    
    print('Gracias por su visita. Esperamos verle de nuevo pronto')