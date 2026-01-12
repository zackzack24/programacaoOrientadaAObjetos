
class Produto:

    # metodo construtor da classe, variaveis obrigam a ter parâmetros
    def __init__(self, nome, marca, valor=0, quantidade=0, modelo=''):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.quantidade = quantidade

    def vender(self, quantidade):
        if (quantidade > self.quantidade):
            print("*************************************")
            print("Não há estoque suficiente")
            print("Quantidade máxima: ", self.quantidade)
            print("*************************************")
        else:
            self.quantidade -= quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade


produto0 = Produto()
produto0.nome = 'Smartphone'
produto0.marca = 'LG'

produto1 = Produto()
produto1.nome = 'Geladeira'
produto1.marca = 'Consul'

produto2 = Produto()
produto2.nome = 'Notebook'
produto2.marca = 'Dell'

produto0 = Produto('Smartphone', 'LG', 5000, 100, 'LX1')
produto1 = Produto('Geladeira', 'Consul', 2000)
produto2 = Produto('Notebool', 'Dell', 3000, 3)

 
print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)

produto0.vender(90)
produto0.comprar(10)
print()
print(produto0.__dict__)
produto0.vender(30)
