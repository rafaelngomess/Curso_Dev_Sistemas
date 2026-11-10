# Desenvolva um programa que solicite o preenchimento de uma matriz 3x3 com 
# números inteiros e, em seguida, peça ao usuário um valor numérico constante 
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar 
# cada elemento da matriz original por esse valor escalar e exibir a matriz 
# resultante formatada em linhas e colunas.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input('Digite um numero: '))
        linha.append(numero)
    matriz.append(linha)

escalar = int(input('Digite um número inteiro: '))

for linha in matriz:
    for numero in linha:
        print(f'{numero*escalar}', end='\t')
    print()
