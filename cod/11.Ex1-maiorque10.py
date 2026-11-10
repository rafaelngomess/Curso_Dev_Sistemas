# Construa um programa onde o usuário digitará 
# dez números. O programa deverá calcular quantos 
# deles são maiores que dez.

numeros = []

for i in range(0, 3):
    numero = float(input('Digite um número: '))
    numeros.append(numero)
contador = 0
for numero in numeros:
    if numero > 10:
        contador += 1
print(contador)

# # versão 2 -> quantos são
# contador = 0
# for i in range(0, 3):
#     numero = float(input('Digite um numero: '))
#     if numero > 10:
#         contador += 1


# # versão 3 -> utilizar lista e guardar os maiores
# lista = []
# for i in range(0, 3):
#     numero = float(input('Digite um numero: '))
#     if numero > 10:
#         lista.append(numero)
# print(len(lista))

# # versão 4 -> jeito mais python
# lista = []
# for i in range(0, 3):
#     numero = float(input('Digite um numero: '))
#     lista.append(numero)

# maiores_que_10 = (
#     [numero for numero in lista if numero > 10]
# )
