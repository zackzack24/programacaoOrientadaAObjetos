import matplotlib.pyplot as plt
from moedas import get_cotacao

def grafico_barra(l_moedas,l_valores):
    plt.bar(l_moedas,l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def grafico_pizza(l_moedas,l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção em relação ao Real (BRL)')
    plt.show()

def grafico_dispercao(l_moedas,l_valores):
    plt.scatter(l_moedas,l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def menu():
    print()
    print('1 - Gráfico de Barras')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Sair')
    print()

cotacoes = get_cotacao()

l_moedas = ['USD - Dólar', 'EUR - Euro', 'GBP - Libras']
l_valores = [1 / cotacoes['USD'],1 / cotacoes['EUR'],1 / cotacoes['GBP']]

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input("Escolha um tipo de gráfico: "))

    match opcao:
        case 1: grafico_barra(l_moedas,l_valores)
        case 2: grafico_pizza(l_moedas,l_valores)
        case 3: grafico_dispercao(l_moedas,l_valores)
                    
    print()
    print('Até a próxima')
    