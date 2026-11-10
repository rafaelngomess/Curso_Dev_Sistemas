lista = []

carros = ['Ferrari F430 Spider', 'Monza Tubarão',
'Golf Sapão', 'Uno com Escada', 'Opala SS Beberrão',
'New Civic', ]

# slice
dois_carros = carros[0:3]
print(dois_carros)

# adicionar na lista (no final da lista)
carros.append('Celta Preto')
print(carros)

print(30*'-')

# retira do fim da lista
# em python, aceita parametro (pode tirar de qualquer lugar)
carro_que_saiu = carros.pop()
print(carro_que_saiu)

# New Civic
carros[5]

# Fim da lista - esse '-1' mostra a ultima posição
carros[-1]

# penultima
carros[-2]

# verificar tipo
# print(type(carros))

# imprimir 1 elemento
# print(carros[4])

# imprimir a lista (como ela esta)
# print(carros)

# imprimir elemento por elemento
# for carro in carros:
#     print(f'{carro}')

# for i in range(len(carros)):
#     print(f'{i+1} - {carros[i]}')


notas = [10, 5, 8, 9.5, 7, 4.5, 1, 0]

# for nota in notas:
#     print(type(nota), nota)

# listas podem ter qualquer coisa dentro delas
# sopa = [0, 1.2, 'a', 'E, aí?', True, 
#         ['Mais uma lista']]
# for s in sopa:
#     print(type(s), s)

