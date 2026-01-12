
def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    try:
        resultado = n1 / n2
        return resultado
    except ZeroDivisionError:
        return "Não é possível dividir um número por zero"
    except ValueError:
        return "Valor incorreto"
    except Exception:
        return "Ocorreu um erro"

    print(f"O resultado da divisão é {resultado}")
    print(f'{n1} / {n2} = {resultado}')


def calcular(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtrair(n1, n2)
        case '*': return multiplicar(n1, n2)
        case '/': return dividir(n1, n2)
        case other: return 'Operador não encontrado'


print(calcular(10, 5, '+'))
print(calcular(10, 5, '-'))
print(calcular(10, 5, '*'))
print(calcular(10, 5, '/'))
print(calcular(10, 5, 'o'))
print(calcular(10, 0, '/'))

try:
    resultado = ()
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
except ValueError:
    print("Valor incorreto")
except Exception:
    print("Ocorreu um erro")
