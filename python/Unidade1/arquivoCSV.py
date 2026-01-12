import csv

carros = [
    ['gol','VW','2011'],
    ['variant','VW','1973'],
    ['k','FORD','2003'],
]

with open('carros.csv', 'w', newline='') as arquivo:
    fileCSV = csv.writer(arquivo, delimiter=";")
    fileCSV.writerow(['Modelo','Marca','Ano'])
    fileCSV.writerows(carros)