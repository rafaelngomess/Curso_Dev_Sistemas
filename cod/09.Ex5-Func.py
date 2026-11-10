# Crie uma função que coloque qualquer texto no seguinte 
# padrão e o retorne:
#   Tudo em minúscula.
#   Sem espaços na frente ou atrás 
#       (começando e finalizando o texto).
# retorne também se há um número no texto


def limpar_texto(texto):
    texto = texto.strip().lower()
    if '2' in texto:
        return texto, True

texto, tem_numero = limpar_texto(' vamos2 ver  ')
print(texto)
print(tem_numero)