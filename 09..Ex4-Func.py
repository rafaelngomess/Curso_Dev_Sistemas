# Crie uma função que coloque qualquer texto no seguinte 
# padrão e o retorne:
#   Tudo em minúscula.
#   Sem espaços na frente ou atrás 
#       (começando e finalizando o texto).

def limpar_texto(texto):
    novo_texto = texto.lower() # tudo em minuscula
    novo_texto = novo_texto.strip() # sem espaço no inicio/fim
    return novo_texto

def limpar_texto_de_uma_vez(texto):
    return texto.strip().lower()

