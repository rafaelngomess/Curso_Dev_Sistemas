# Desenvolva um programa que leia os valores de uma matriz 2x4 de números inteiros.
# O programa deve contar quantos valores estão abaixo de um limiar, 
# que também será informado pelo usuário, estão presentes na estrutura e 
# exibir a contagem total, além de imprimir a matriz completa formatada em 
# linhas e colunas.

matriz = []

for i in range(2): # linhas
    lista = []
    for j in range(4): # colunas
        numero = int(input('Digite um número: '))
        lista.append(numero) # guardo o que leio na coluna
    matriz.append(lista) # guardo a linha toda na matriz

# agora pegar o limitador (limiar)
limiar = int(input('Digite o limiar: '))

# achar quantos numeros da matriz é menor do que o limiar
contador = 0

for linha in matriz:
    for numero in linha:
        if numero < limiar: # matriz[i][j] < limiar
            contador += 1
            # contador = contador + 1

print(f'Existe(m) {contador} número(s) menor(es) do que o \
      limiar({limiar}) na matriz abaixo')

# for i in range(len(matriz)): # verificando numero de linhas
#     for j in range(len(matriz[i])): # verificando quantas colunas em cada linha
#         print(matriz[i][j], end='\t') # da "4" espaços para cada num da coluna
#     print() # acabou a linha de numeros, pula uma linha

# como imprimir uma matriz de forma bonita
for linha in matriz:
    for numero in linha:
        print(numero, end='\t')
    print()