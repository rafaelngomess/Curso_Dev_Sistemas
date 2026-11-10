# Construa uma matriz 2X2 e, como saída desse programa, 
# a média e a soma dos valores digitados deverão ser calculadas.

matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Digite um número: ')))
    matriz.append(linha)

soma = 0
# for linha in matriz:
#     for coluna in linha:
#         soma += coluna
contador = 0
for linha in range(len(matriz)): # quantas linhas tem
    for coluna in range(len(matriz[linha])): # quantas colunas tem
        soma += matriz[linha][coluna]
        contador += 1

media = soma/contador

