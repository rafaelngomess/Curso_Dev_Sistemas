# construa um programa onde o usuario digitará um valor
# e o programa mostrará na tela a tabuada de multiplicação 
# desse numero

numero = int(input('digite um numero: '))

for i in range(numero, -1, -1):

    if i % 2 == 0:
         print(i)       