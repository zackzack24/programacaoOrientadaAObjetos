from classes.Produto import Produto
from classes.Categoria import Categoria

def menu():
    print()
    print('1 - Listar Produtos')
    print('2 - Inserir Produtos')
    print('3 - Alterar Produtos')
    print('4 - Excluir Produtos')
    print('0 - Sair')

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print()
            print(' ')
            Produto.listarTodos()
            print('')
        case 2:
            código = input('Digite o código: ')
            nome = input('Digite o nome: ')
            quantidade = input('Digite o quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(código,nome,quantidade,valor)
            produto.Inserir()
        case 3:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja alterar? '))
            item = Produto.consultar(selecionado)

            quantidade = int(input('Qual a nova Quantidade? '))
            valor = int(input('Qual o novo Valor? '))

            produto = Produto(item['codigo'], item['nome'],quantidade,valor)
            produto.Alterar(selecionado)

        case 4:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja excluir? '))
            Produto.Excluir(selecionado)

print('Até a próxima!')