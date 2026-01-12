
arquivo = open('pessoas.txt', 'w')


arquivo.write('Mauricio\n')
arquivo.write('Milton\n')
arquivo.write('Myrna\n')


arquivo.close()

with open('pessoas.txt', 'r+') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)
