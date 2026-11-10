def bubble_sort(lista):
    # primeiro: andar na lista
    for j in range(len(lista)):
        # Otimização 2: Parar o algoritmo quando não haver mais trocas
        houve_troca = False
        # verificar cada numero
        # Otimização 1: a medida que vai ordenando, nas ultimas posições
        # sempre tem os maiores, então não preciso ir até lá
        # Faço isso com (-i) no range
        for i in range(len(lista) - 1 - j): # l = [2, 4, 5, 0, 8, 10]
            # verifica se o elemento da proxima posição é maior do que
            # o elemento da atual 
            # i -> 0 a 5
            if lista[i] > lista[i+1]: 
                # se for, troca de posição
                lista[i+1], lista[i] = lista[i], lista[i+1]
                houve_troca = True
                # como seria feito em outra linguagem
                # aux = lista[i]
                # lista[i] = lista[i+1]
                # lista[i+1] = aux

        # Se não ocorreu troca alguma, já esta ordenado
        if not houve_troca:
            break
    return lista

l = [2, 8, 5, 4, 10, 0]
bubble_sort(l)
print(l)

# def bubble_sort_v1(lista):
#     for _ in range(len(lista)):
#         for i in range(len(lista)-1):  
#             if lista[i] > lista[i+1]: 
#                 lista[i+1], lista[i] = lista[i], lista[i+1]
#     return lista

# def bubble_sort_v2(lista):
#     for j in range(len(lista)):
#         for i in range(len(lista) - 1 - j):  
#             if lista[i] > lista[i+1]: 
#                 lista[i+1], lista[i] = lista[i], lista[i+1]
#     return lista

# def bubble_sort_v3(lista):
#     for j in range(len(lista)):
#         houve_troca = False
#         for i in range(len(lista) - 1 - j):  
#             if lista[i] > lista[i+1]: 
#                 lista[i+1], lista[i] = lista[i], lista[i+1]
#                 houve_troca = True
#         if not houve_troca:
#             break
#     return lista
       