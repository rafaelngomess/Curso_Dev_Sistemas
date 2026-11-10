# como achar o menor valor entre dois números

# Passo 1 -> Ter 2 números
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

# Passo 2 -> Testar condicional
if numero1 == numero2:
    print(f'Ambos os números são iguais')
elif numero1 < numero2:
    print(f'{numero1} é menor do que o {numero2}')
else:
    print(f'{numero2} é menor do que o {numero1}')

