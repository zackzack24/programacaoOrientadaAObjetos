n1 = 10
n2 = 4
n3 = 6
n4 = 2

soma = n1 + n2 + n3 + n4
media = soma / 4


if media >= 7:
    print("Aprovado")
    print("Esse print está dentro do IF")

print("Esse print não está dentro do IF")


print("A média é: ", media)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


 
print("A média é: ", media)
if media >= 7:
    print("Aprovado")
elif media < 5:  
    print("Reprovado")
else:
    print("Recuperação")
