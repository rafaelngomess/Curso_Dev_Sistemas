# usuário digitará o nome e a idade de dez pessoas e o 
# programa escreverá o nome do usuário mais novo.

lista = []
for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    lista.append([nome, idade])

# Forma 1 -> Usar o indice (o mais novo esta no inicio da lista)
mais_novo = 0 # indice
# o loop inicia do proximo elemento
for i in range(1, len(lista)):
    print(f'{lista[i][1]} é menor do que {lista[mais_novo][1]}\n')
    if lista[i][1] < lista[mais_novo][1]:
        mais_novo = i
        print(f'Era, então a posição do mais novo na lista é: {i}\n')

print(f'\n\n\nO usuário mais novo é: {lista[mais_novo][0]}')

# Forma 2 -> agora com função (min)
# [['Alfredo', 35], ['labubu', 5]]
mais_novo = min(lista, key=lambda pessoa: pessoa[1])
print(f'O usuário mais novo é: {mais_novo[0]}')