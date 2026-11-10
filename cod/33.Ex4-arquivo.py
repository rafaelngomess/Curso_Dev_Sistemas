# Criar um script em Python que leia o arquivo vendas.csv, 
# aplique cálculos e regras de negócio para cada pedido e 
# gere um novo arquivo chamado faturamento.csv.
# Para cada linha do arquivo, realize as seguintes operações:
#   Valor Bruto: quantidade * preco_unitario
#   Desconto: 10% do valor bruto se a quantidade >= 5; 
#       caso contrário, 0.00
#   Valor Líquido: valor_bruto - desconto
#   Status: "PREMIUM" se valor_liquido >= 1000.00; 
#      caso contrário, "PADRAO"
import csv

with(open('vendas.csv', 'r', encoding='utf-8') as arquivo,
    open('faturamento.csv', 'w', encoding='utf-8') as arq_saida):

    leitor = csv.DictReader(arquivo, delimiter=';')

    # criar o escritor
    escritor = None # None em Python é Null

    for venda in leitor:
        qtd = int(venda['quantidade'])
        valor = float(venda['preco_unitario'])

        valor_bruto = qtd * valor

        # desconto = valor_bruto * 0.1 if qtd >= 5 else 0.0
        desconto = 0.0
        if qtd >= 5:
            desconto = valor_bruto * 0.1

        valor_liquido = valor_bruto - desconto

        status = 'PADRÃO'
        if valor_liquido >= 1000.00:
            status = 'PREMIUM'

        venda_consolidada = {
            'id_pedido': venda['id_pedido'],
            'cliente': venda['cliente'],
            'produto': venda['produto'],
            'quantidade': venda['quantidade'],
            'preco_unitario': venda['preco_unitario'],
            'valor_bruto': f'{valor_bruto:.2f}',
            'desconto': f'{desconto:.2f}',
            'valor_liquido': f'{valor_liquido:.2f}',
            'status': status
        }
        
        if escritor == None:
            cabecalhos = list(venda_consolidada.keys())
            escritor = csv.DictWriter(arq_saida, delimiter=';',
                                      fieldnames=cabecalhos)
            # escrever a primeira linha (que são os nomes das colunas)
            escritor.writeheader()
        
        escritor.writerow(venda_consolidada)
    