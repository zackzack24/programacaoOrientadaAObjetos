from classes.AbstractCRUD import AbstractCRUD


class Categoria(AbstractCRUD):

    arquivo = 'db/categorias.json'

    def __init__(self, nome):
        self.nome = nome
