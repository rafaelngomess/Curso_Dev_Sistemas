# Construa um programa onde o usuário digitará 
# três números e o programa exibirá, 
# na tela, o maior entre eles.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

if numero1 > numero2 and numero1 > numero3:
    print('O primeiro número é o maior')
elif numero2 > numero3:
    print('O segundo número é o maior')
else:
    print('O terceiro número é o maior')
