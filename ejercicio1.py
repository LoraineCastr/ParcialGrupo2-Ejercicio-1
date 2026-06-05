# Problematica : Un cabello tiene 4 herraduras del año pasado pero no sabe cuantas herraduras son del mismo color.
# El quiere reemplazarlas para que cada una quede de un color diferente a la moda actual. 
# Y necesita realizar una compra de herraduras nuevas contando con el dinero suficiente,
# sin embargo requiere ahorrar para gastar lo menos posible. 

# Solucion : Desarrollar un sistema que permita identificar 
# cuantas herraduras son del mismo color y asi determinar cuantas herraduras nuevas debe comprar el caballo.
 
herraduras = []

#Solicitud de colores de herraduras
for i in range(4):
    colores = int(input())
    herraduras.append(colores)

#comparacion de colores 
comprar_herradura = 0

if herraduras[0] == herraduras[1] or herraduras[0] == herraduras[2] or herraduras[0] == herraduras[3]:
    comprar_herradura += 1
if herraduras[1] == herraduras[2] or herraduras[1] == herraduras[3]:
    comprar_herradura += 1
if herraduras[2] == herraduras[3]:
    comprar_herradura += 1
print(comprar_herradura)

