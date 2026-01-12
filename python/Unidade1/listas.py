
numeros = [10, 20, 30, 17]
print(numeros)
print(numeros[0])


carros = ["gol", "variant", "k", "palio", "ecosport"]
print(len(carros))
print('1->', carros)
carros.append('i30')
print('2->', carros)
carros.remove('gol')
print('3->', carros)
del carros[3]
print('4->', carros)
carros = sorted(carros)
print('5->', carros)

for carro in carros:
    print(carro)
