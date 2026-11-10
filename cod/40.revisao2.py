# Desenvolva um script que leia esse arquivo e 
# filtre apenas os itens cujo saldo_atual esteja 
# estritamente abaixo do estoque_minimo. 

# O resultado filtrado deve ser gravado em um novo arquivo 
# chamado pedidos_reposicao.csv, incluindo uma nova coluna 
# calculada chamada qtd_comprar, que representa a quantidade 
# necessária para atingir a meta mínima.


import csv

with (open('02.arquivo.csv', 'r', encoding='utf-8') as ENTRADA,
     open('pedidos_reposicao.csv', 'a', encoding='utf-8') as SAIDA):

    leitor = csv.DictReader(ENTRADA, delimiter=';')
    escritor = None

    for produto in leitor:
        estoque_minimo = int(produto['estoque_minimo'])
        qtd_produto = int(produto['saldo_atual'])

        # 10 - 20 = -10 -> abs(-10) 
        if qtd_produto < estoque_minimo:
            # diferenca = abs(qtd_produto - estoque_minimo)
            diferenca = estoque_minimo - qtd_produto

            produto['qtd_comprar'] = diferenca

            if escritor == None: # if escritor is None:
                cabecalho = list(produto.keys())
                escritor = csv.DictWriter(SAIDA, 
                                          fieldnames=cabecalho,
                                          delimiter=';')
                escritor.writeheader()

            escritor.writerow(produto)