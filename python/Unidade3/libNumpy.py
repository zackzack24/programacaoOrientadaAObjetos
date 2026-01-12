
import numpy as np
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for n in numeros:
    soma = soma + n
    soma += n
media = soma / 10
media = soma / len(numeros)
print(soma, media)
print('media manual :', media)
array_numeros = np.array(numeros)
media = np.mean(array_numeros)
print('media numpy :', media)
