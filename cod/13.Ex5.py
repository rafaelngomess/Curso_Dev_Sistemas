# usuário digitará dez números inteiros. 
# O programa deve identificar qual é o maior e qual é o 
# menor número digitado, exibindo também a posição (índice)
#  em que cada um deles se encontra no vetor.
lista = []
for i in range(0, 5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

maior = max(lista)
indice_maior = lista.index(maior)

menor = min(lista)
indice_menor = lista.index(menor)