
import data
 
class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo
    
    def taxaAgua(self, consumo):
       print("Data da leitura: ", data.formatarData())
       match self.tipo:
           case 'Clínica': return 1 * consumo
           case 'Restasurante': return 2 * consumo
           case 'Hotel': return 2.5 * consumo

 

class Imovel:

    imposto = 0.2 

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()
    
     
    def __add__(self, other):  
        somaSelf  = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    def __gt__(self,other):  
        somaSelf  = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    def __lt__(self,other): 
        somaSelf  = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def __str__(self):  
        return str(self.__dict__)
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
     
    @staticmethod
    def metodoEstatico():
        print('Chamou o método estático sem criar um objeto')
    
    #metodos de CLASSE
    @classmethod
    def metodoClasse(cls):
        print('Chamoo o método de classe que vê o imposto', cls.imposto)



casarao = Imovel('Casarão', 3, 4)

print(casarao.__dict__)

mansao = Imovel('Mansão', 4, 5)
print(mansao.__dict__)

categoria = Categoria('Hotel')
hotel = Imovel('Hostel',0,150)
hotel.categoria = categoria

print(hotel.categoria.taxaAgua(300))

 
print(casarao + mansao)
print(casarao > mansao)
print(casarao < mansao)
print(casarao)
 

print(casarao.somarAposentos())
print(mansao.somarAposentos())

Imovel.metodoClasse()
Imovel.metodoEstatico()