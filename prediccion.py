import csv
dicc={}
with open('Ocupados.CSV', mode='r') as data:
    reader = csv.reader(data)
    for line in reader:
        linea=line[0].split(";")
        for i in linea:
            dicc[i]=[]
        break
    for line in reader:
        lline=line[0].split(";")
        if lline!=linea:
            for i in range(len(lline)):
                dicc[linea[i]].append(lline[i])
for i in range(len(dicc['P6426'])):
    dicc['P6426'][i]=int(dicc['P6426'][i])//12