def tablero(n,x,y,p):
    matriz=[]
    #guardamos el valor original
    yoriginal=y
    #rellenar matriz con ceros
    for i in range(n):
        fila=[]
        for j in range(n):
            fila.append(0)
        matriz.append(fila)
    matriz[x][y]=p
    for j in range(p+n):
        x-=1;
        y-=1;
        #izquierda
        for i in range(j*2+3):
            if x+i>=0 and y>=0 and x+i<n:
                matriz[x+i][y]=p-j-1
        #abajo
        for i in range(j*2+3):
            if x+j*2+2>=0 and y+i>=0 and x+j*2+2<n and y+i<n:
                if y+i<=yoriginal:
                    matriz[x+j*2+2][y+i]=p-j-1
                else:
                    matriz[x+j*2+2][y+i]=p+j+1
        #derecha
        for i in range(j*2+3):
            if x+i>=0 and y+j*2+2>=0 and x+i<n and y+j*2+2<n:
                matriz[x+i][y+j*2+2]=p+j+1
        #arriba
        for i in range(j*2+3):
            if x>=0 and y+i>=0 and y+i<n:
                if y+i<=yoriginal:
                    matriz[x][y+i]=p-j-1
                else:
                    matriz[x][y+i]=p+j+1
    return matriz

n=int(input())
x,y,p=map(int,input().split())
matriz=tablero(n,x,y,p)
#imprimir matriz
total=""
for i in matriz:
    linea=""
    for j in i:
        linea+=str(j)+" "
    total+=linea[:-1]+"\n"
print(total)
