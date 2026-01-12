import json
from abc import ABC
from typing import SupportsIndex


class AbstractCRUD(ABC):

    def detalhar(self):
        return self.__dict__

    def Inserir(self):

        lista = self.consultar()

        lista.append(self.detalhar())

        self.__gravarArquivo(lista)

    def Alterar(self, item):

        lista = self.consultar()

        lista[item] = self.detalhar()

        self.__gravarArquivo(lista)

    @classmethod
    def Excluir(cls, item):

        lista = cls.consultar()

        del lista[item]

        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Operação realizada com sucesso')

    def __gravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Operação realizada com sucesso')

    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")

    @classmethod
    def consultar(cls, item=None):
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file)
                return lista[item] if isinstance(item, int) else lista
        except Exception:
            return []
