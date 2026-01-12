 
import pandas as pd

cidades = [
    {'nome' : 'Brásilia', 'uf': 'DF', 'populacao': 321212},
    {'nome' : 'São Paulo', 'uf': 'SP', 'populacao': 5212121},
    {'nome' : 'Rio de Janeiro', 'uf': 'RJ', 'populacao': 3212121},
    {'nome' : 'Recife', 'uf': 'PE', 'populacao': 1212121},
]

dataFrame = pd.DataFrame(cidades)
print(dataFrame)

ordenada = dataFrame.sort_values(by='populacao',ascending=False)

print(ordenada)
print(ordenada.head(2)['nome'])  