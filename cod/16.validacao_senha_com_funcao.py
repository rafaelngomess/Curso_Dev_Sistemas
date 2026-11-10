# Crie um sistema de autenticação de terminal que 
# valida a segurança da senha cadastrada e gerencia o acesso do usuário.

def inicializarSistema():
    for i in range(5, 0, -1):
        print(f'{i}...')
    print('Sistema inicializado com sucesso')

def errouTudo(tentativa):
    if tentativa <= 0:
        print('Acesso Negado.\nConta Bloqueada')

# Primeiro, o usuário define uma senha numérica de 4 dígitos. 
# Use um loop while que continue solicitando até que o valor 
# digitado esteja rigorosamente entre 1000 e 9999.
print('============== Sistema de Autenticação ===============')
senha = int(input('Informe sua senha: '))
while senha < 1000 or senha > 9999:
    senha = int(input('Informe sua senha: '))


# fica ai em cima até digitar uma senha (PIN) válida
# -------------------------------------------------

tentativa = 3
while tentativa > 0:
    confirmacao_senha = int(
    input('Para entrar no sistema, digite o PIN: '))

    if senha == confirmacao_senha:
        inicializarSistema()
        break

    else:
        tentativa = tentativa - 1

    print(f'Você ainda tem {tentativa} tentativas')

errouTudo(tentativa)