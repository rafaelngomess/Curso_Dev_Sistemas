def insertion_sort(lista):
    # começa do indice 1 (pq ja vamos comparar com quem esta
    # a esquerda)
    for i in range(1, len(lista)):
        # separo o elemento atual
        selecionado = lista[i]
        posicao = i - 1 # olha o anterior (esquerda)

        # olhar a lista e ver se o atual é menor que o proximo
        # ou em outras palavras se ele é maior que o anterior

        selecionado = 10 // posicao = 4
        while posicao >= 0 and lista[posicao] > selecionado:
            lista[posicao + 1] = lista[posicao] # inverte
            posicao = posicao - 1

        lista[posicao + 1] = selecionado
    return lista
# posicao =   [0, 1, 2, 3, 4, 5]
# original =  [1, 2, 5, 8, 0, 10]
# l1 =        [1, 2, 5, 8, 8, 10]
# l2 =        [1, 2, 5, 5, 8, 10]
# l3 =        [1, 2, 2, 5, 8, 10]
# l4 =        [1, 1, 2, 5, 8, 10]
# l4 =        [0, 1, 2, 5, 8, 10]





l2 =        [1, 2, 5, 8, 0, 10]
