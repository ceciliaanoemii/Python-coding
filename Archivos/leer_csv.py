import csv

with open("Archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader: #Va a recorrer fila por fila (row)
        print(row)
