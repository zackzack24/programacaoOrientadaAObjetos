from classes.AbstractCRUD import AbstractCRUD


class Produto(AbstractCRUD):

    arquivo = 'db/produtos.json'

    def __init__(self, codigo, nome, quantidade=0, valor=0):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor = valor

    def Inserir(self):
        lista = self.consultar()
        produtoDuplicado = filter(lambda p: p['codigo'] == self.codigo, lista)

        if len(list(produtoDuplicado)):
            print()
            print('Já existe um produto com esse código')
        else:
            super().Inserir()
