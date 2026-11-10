# Construa um programa onde o usuário digitará dois números, 
# utilizando passagem de parâmetros e, dentro da função, 
# irá calcular a soma desses dois números.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

def somar(num1, num2):
    return num1 + num2

resultado = somar(numero1, numero2)
print(resultado)
