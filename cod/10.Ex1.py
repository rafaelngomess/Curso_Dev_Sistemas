# Construa um programa onde o usuário digitará 
# dez números e o programa
# somará e calculará a média dos números digitados.

lista = []
for i in range(0,3):
    numero = float(input('Digite um número: '))
    lista.append(numero)

# soma = 0
# for item in lista:
#     soma = soma + item

media = sum(lista)/len(lista)
print(f'A média é: {media:.2f}')