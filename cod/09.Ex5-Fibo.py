# calcular a sequencia de fibonacci ate 2000
# não tem entrada de usuario

# antipenultimo = 0
# penultimo = 1

# print(f'{antipenultimo}')
# print(f'{penultimo}')
# for i in range(0,2000):
#     i = antipenultimo + penultimo
#     if i < 2000:
#         print(f'{i}')
#     antipenultimo = penultimo
#     penultimo = i

anterior = 0
atual = 1
proximo = anterior + atual # 1
print(anterior)
print(atual)
print(proximo)
while(atual <= 2000):
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    # anterior, atual = atual, atual + anterior
    print(atual)






a = 10
b = 2

a, b = b, a 



