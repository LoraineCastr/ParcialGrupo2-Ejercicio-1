herraduras= []

#Solicitud de colores de herraduras
for i in range(4):
    colores = int(input())
    herraduras.append(colores)

#comparacion de colores 
comprar_herradura = 0

if herraduras[0] == herraduras[1] or herraduras[0] == herraduras[2] or herraduras[0] == herraduras[3]:
    comprar_herradura = 1
if herraduras[1] == herraduras[2] or herraduras[1] == herraduras[3]:
    comprar_herradura = 1
if herraduras[2] == herraduras[3]:
    comprar_herradura = 1
   print(comprar_herradura)