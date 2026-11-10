# Construa um programa que leia 10 números inteiros, armazene-os em uma lista e, 
# em seguida, solicite um número adicional para consulta. O sistema deve verificar 
# e exibir se esse valor está presente no vetor e a quantidade exata de vezes 
# que ele se repete.

lista = []

for i in range(10):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

procurado = int(input('Digite o numero a ser consultado: '))

contador = 0

for numero in lista:
    if numero == procurado:
        contador += 1

# Forma 2 -> usar função já pronta
vezes = lista.count(numero)