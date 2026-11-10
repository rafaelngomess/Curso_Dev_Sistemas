# 3 funções -> iniciando pelo "Inicio"

def quicksort(lista):
    quicksort_recursivo(lista, 0, len(lista)-1)
    return lista

def quicksort_recursivo(lista, inicio, fim):
    if fim > inicio: # inicio < fim
        indice_pivo = dividir(lista, inicio, fim)
        quicksort_recursivo(lista, inicio, indice_pivo-1)
        quicksort_recursivo(lista, indice_pivo+1, fim)

def dividir(lista, inicio, fim):
    pivo = lista[fim] # elemento/numero da ultima posição
    # pivo = lista[inicio]
    # pivo = lista[len(lista)//2] # pegaria o pivo no meio do vetor
    # len(lista)//2 -> parte inteira da divisão

    i = inicio - 1
    # isso vai ser minha referencia de até onde vão os menores
    # que o pivo
    # pq "- 1"? não olhei os elementos do vetor ainda

    for j in range(inicio, fim): 
        if lista[j] <= pivo: 
            i += 1 
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[fim] = lista[fim], lista[i+1]

    return i + 1
    