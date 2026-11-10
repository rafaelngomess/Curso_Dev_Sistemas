# usuário para digitar oito números e os guarde em um vetor. 
# Depois, o programa deve pedir um número adicional e 
# informar se esse número está presente no vetor. 
# Se estiver, informe em qual posição (índice) ele foi encontrado 
# pela primeira vez.

numeros = []

for i in range(0, 8):
    num = int(input('Digite um numero: '))
    numeros.append(num)

# pegar o numero a ser procurado
procurado = int(input('Digite um numero: '))

# V1 -> usar o operador 'in'
if procurado in numeros:
    print(f'Esta na lista, na posição: {numeros.index(procurado)}')
else:
    print('Não esta na lista')

# V2 -> percorrer a lista
for num in numeros:
    if procurado == num:
        print(f'Esta na lista, na posição: {numeros.index(num)}')
