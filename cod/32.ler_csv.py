import csv

print('--------- Sistema de Leitura de CSVs Abrasileirados ---------')
try:
    with open('carros.csv', 'r', 
          encoding='utf-8') as arq_csv:

        leitor = csv.DictReader(arq_csv, delimiter=';', )
        for carro in leitor:
            marca = carro['marca']
            modelo = carro['modelo']
            ano = carro['ano']
            print(f'Marca: {marca}, Modelo: {modelo}, Ano: {ano}')

except FileNotFoundError:
    print('Deu erro na leitura do arquivo')
except FileExistsError:
    print('Deu outro erro')
except Exception as e:
    print(f'Erro: {e}')


