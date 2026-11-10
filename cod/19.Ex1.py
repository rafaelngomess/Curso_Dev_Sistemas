# Desenvolva um programa que solicite dois números inteiros representando os
# limites de um intervalo [A, B] (garantindo que A ≤ B). 
# O programa deve iterar sobre o intervalo utilizando uma estrutura de repetição 
# e calcular a soma apenas dos
# números ímpares presentes nele, exibindo o resultado final ao usuário.

def somarImpares(inicio, fim):

    # while fim < inicio:
    #     fim = int(input('Digite o segundo numero: '))

    # if inicio > fim:
    #     inicio, fim = fim, inicio
    
    if inicio > fim:
        print('Cara, tu digitou errado, saindo do programa')
        return None
        # se não tem função tire o return use
        # exit(0)
    
    somatorio = 0
    for i in range(inicio, fim+1): # +1 no 'b' pq tem que incluir ele
        if i%2 != 0: # verifica se é impar
            somatorio += i

    return somatorio

# inicio do programa
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

soma = somarImpares(a, b)
print(soma)