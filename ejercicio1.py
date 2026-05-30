herraduras= []

#Solicitud de colores de herraduras
for i in range(4):
    colores = int(input())
    herraduras.append(colores)

#comparacion de colores 
if herraduras[0] == herraduras[1] or herraduras[0] == herraduras[2] or herraduras[0] == herraduras[3]:
    print("SI")
    