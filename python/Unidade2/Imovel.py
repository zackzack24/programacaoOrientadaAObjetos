from abc import ABC, abstractmethod


class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco='', area=''):

        self._nome = nome
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, uf):
        self._uf = uf

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def detalhar(self):

        print(self.__dict__)

    def calcularImposto(self):
        return self._valor * (2/100)

    @abstractmethod
    def AluguelSugerido(self):
        ...


class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco='', area=''):

        super().__init__(nome, uf, valor, endereco='', area='')
        self._quartos = ''
        self._banheiros = ''

    @property
    def quartos(self):
        return self._quartos

    @quartos.setter
    def quartos(self, quartos):
        self._quartos = quartos

    @property
    def banheiros(self):
        return self._banheiros

    @banheiros.setter
    def banheiros(self, banheiros):
        self._banheiros = banheiros

    def AluguelSugerido(self):
        return self._valor * 0.01


class ImovelComercial(Imovel):
    def AluguelSugerido(self):
        return self._valor * 0.020

    def calcularImposto(self):
        match self._uf:
            case 'RJ': taxa = 3
            case 'SP': taxa = 4
            case 'DF': taxa = 5
            case other: taxa = 6
        return self._valor * (taxa/100)


class ImovelRural():
    def __init__(self, hectares='', curral='', produtiva=True):
        self._hectares = hectares
        self._curral = curral
        self._produtiva = produtiva

    @property
    def hectares(self):
        return self._hectares

    @hectares.setter
    def hectares(self, hectares):
        self._hectares = hectares

    @property
    def curral(self):
        return self._curral

    @curral.setter
    def curral(self, curral):
        self._curral = curral

    @property
    def produtiva(self):
        return self._produtiva

    @produtiva.setter
    def produtiva(self, produtiva):
        self._produtiva = produtiva

    def mesPlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')


class Fazenda(Imovel, ImovelRural):
    def AluguelSugerido(self):
        return self.valor * 0.015


casa = ImovelResidencial('Bandeira 51', 'RJ', 250000)
casa.setNome('Casa Bonita')
print(casa.getNome())
casa.nome = 'Casa muito bonita'
print(casa.nome)
casa.detalhar()
print(casa.AluguelSugerido())

print(casa.calcularImposto())

clinica = ImovelComercial('São Luiz', 'SP', 300000)
clinica2 = ImovelComercial('São Luiz', 'RJ', 300000)

print(clinica.calcularImposto())
print(clinica2.calcularImposto())


fazenda = Fazenda('São Luiz', 'RJ', 300000)
fazenda.detalhar()


imovel = Imovel('Apartamento A', 'RJ', 500000)

imovel.endereco = 'Rua dos Limoeiros, 55, 201'
imovel.area = 100

imovel.detalhar()
