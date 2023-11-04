def main():
    distribucionTareas = list(map(int, input().split(', ')))
    distanciaCercanos = int(input())

    for i in range(len(distribucionTareas)):
        if distribucionTareas[i] > 0:
            indexDelvalorMinimo = -1
            valorMinimo = 0
            for j in range(-distanciaCercanos, distanciaCercanos+1):
                if i + j < 0:
                    continue
                if i + j >= len(distribucionTareas):
                    break
                if distribucionTareas[i + j] < valorMinimo:
                    valorMinimo = distribucionTareas[i + j]
                    indexDelvalorMinimo = i + j
                if distribucionTareas[i] >= -distribucionTareas[indexDelvalorMinimo] and indexDelvalorMinimo >= 0:
                    break
            if indexDelvalorMinimo >= 0:
                if distribucionTareas[i] >= -distribucionTareas[indexDelvalorMinimo]:
                    distribucionTareas[i] += distribucionTareas[indexDelvalorMinimo]
                    distribucionTareas[indexDelvalorMinimo] = 0
                else:
                    distribucionTareas[indexDelvalorMinimo] += distribucionTareas[i]
                    distribucionTareas[i] = 0

    for i in range(len(distribucionTareas)):
        if distribucionTareas[i] < 0:
            distribucionTareas[i] *= -1

    print(sum(distribucionTareas))

            
