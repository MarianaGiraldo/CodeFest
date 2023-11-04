from math import sqrt
def distanciaEntreCiudades(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def main():
    cantidadCiudades = int(input())
    ciudades = [0 for i in range(cantidadCiudades)]

    for i in range(cantidadCiudades):
        ciudades[i] = list(map(int, input().split(', ')))

    ciudadesVisitadas = [False for i in range(cantidadCiudades)]
    ciudadesVisitadas[0] = True
    ciudadActual = 0
    ciudadNueva = 0
    sumaDistancias = 0

    for i in range(1, cantidadCiudades):
        distanciaMinima = sqrt(2) * 20000
        for j in range(1, cantidadCiudades):
            if ciudadesVisitadas[j]:
                continue
            distancia = distanciaEntreCiudades(ciudades[ciudadActual], ciudades[j])
            if distancia < distanciaMinima:
                distanciaMinima = distancia
                ciudadNueva = j
        ciudadesVisitadas[ciudadNueva] = True
        ciudadActual = ciudadNueva
        sumaDistancias += distanciaMinima

    print(sumaDistancias)
