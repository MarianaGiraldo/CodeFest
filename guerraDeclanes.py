def cantidadMiembros(P, G, p, g):
    parejass = zip(p, g)
    tuplaMinima = min(zip(p, g), key=lambda x: x[0] + x[1])
    
        

def main():
    Clanes, TotalPistolas, TotalGranadas = list(map(int, input().split(' ')))
    for i in range(Clanes):
        CantidadMiembros = int(input())
        pistolas, granadas = [0 for i in range(CantidadMiembros)], [0 for i in range(CantidadMiembros)]
        for j in range(CantidadMiembros):
            pistolas[j], granadas[j] = list(map(int, input().split(' ')))
        c = cantidadMiembros(TotalPistolas, TotalGranadas, pistolas, granadas)
        print(c, end=' ')
