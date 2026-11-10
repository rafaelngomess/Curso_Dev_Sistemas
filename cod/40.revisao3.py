# Um formulário web despadronizado gerou um arquivo de texto 
# bruto chamado emails_brutos.txt com e-mails digitados pelos 
# usuários. 
# Esse arquivo contém espaçamentos indesejados nas pontas, 
# caracteres maiúsculos misturados e linhas vazias acidentais. 

# Escreva um script em Python que leia esse arquivo linha por 
# linha, descarte linhas em branco, converta todos os e-mails 
# válidos para letras minúsculas (lowercase), remova espaços 
# extras nas pontas e salve a lista limpa e padronizada em um 
# novo arquivo chamado emails_padronizados.txt.

with open('03.arquivo.txt', 'r', encoding='utf-8') as arquivo:
    linhas_corretas = []

    for email in arquivo:
        if email.strip() != '':
            email = email.strip().lower()
            linhas_corretas.append(email)

    with open('emails_padronizados.txt', 'a', encoding='utf-8') as saida:
        for email in linhas_corretas:
            saida.write(f'{email}\n')



#  forma 2
with(open('03.arquivo.txt', 'r', encoding='utf-8') as arquivo,
open('emails_padronizados.txt', 'a', encoding='utf-8') as saida):
    for email in arquivo:
        if email.strip() != '':
            email = email.strip().lower()
            saida.write(f'{email}\n')
