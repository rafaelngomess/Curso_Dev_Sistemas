# Construa um programa que receba 8 números inteiros e os guarde em um vetor. 
# Em seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares 
# do vetor original sejam multiplicados por 2 e os números pares permaneçam 
# inalterados. Ao final, exiba os dois vetores.

import copy

lista = []
for i in range(8):
    numero = int(input('Digite um número: '))
    lista.append(numero)

# Forma 1
nova_lista = lista.copy() # copia (copia rasa)

for i in range(len(lista)):
    if lista[i]%2 != 0: # quem não é par <=> é impar
        nova_lista[i] = nova_lista[i] * 2 # multiplica por 2
        # nova_lista[i] *= 2
    
print(lista)
print(nova_lista)


# Forma 2 -> Copiar on-the-fly (na hora)

nova_lista = []

for numero in lista:
    if numero % 2 != 0:
        nova_lista.append(numero*2)
    else:
        nova_lista.append(numero)

print(lista)
print(nova_lista)

# Forma 3 -> para quando copy não funcionar
nova_lista = copy.deepcopy(lista)
