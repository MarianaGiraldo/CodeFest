#Leer y crear la matriz nxn

n=int(input())

tablero=[]

for i in range(n):

    a=[]

    for j in range(n):

        a.append(0)

    tablero.append(a)

   

   

#Leer las entrada i,j,potencia

entrada=input().split(" ") # ["1","1","5"]

for i in range(len(entrada)):

    entrada[i] = int(entrada[i])

cor_X = entrada[0]

cor_Y = entrada[1]

potencia = entrada[2]

 

#Reemplazar la posicion i,j con potencia

tablero[cor_X][cor_Y] = potencia

 

#modificar cada una de las posiciones según la distancia

 

# (2,2) - (4,5) = 3 = distancia

#x= 4

#y = 5

for x in range(n):

    for y in range(n):

        distanciaX = abs(cor_X - x)

        distanciaY = abs(cor_Y - y)

        distancia = max([distanciaX, distanciaY])
    
        if y<=cor_Y:
            tablero[x][y] = potencia - distancia
        else:
            tablero[x][y] = potencia + distancia
 

# Imprimir la matriz

for i in range(n):

    for j in range(n):

        if j == n-1:

            print(tablero[i][j], end="")

        else:

            print(tablero[i][j], end=" ")

    print()