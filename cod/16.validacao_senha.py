# Crie um sistema de autenticação de terminal que 
# valida a segurança da senha cadastrada e gerencia o acesso do usuário.

# Primeiro, o usuário define uma senha numérica de 4 dígitos. 
# Use um loop while que continue solicitando até que o valor 
# digitado esteja rigorosamente entre 1000 e 9999.

senha = int(input('Informe sua senha: '))
while senha < 1000 or senha > 9999:
    senha = int(input('Informe sua senha: '))

# fica ai em cima até digitar uma senha (PIN) válida
# -------------------------------------------------

# Em seguida, o sistema entra em modo de bloqueio e 
# pede a confirmação da senha para liberar o sistema, 
# permitindo até 3 tentativas via loop while.
print('\n\n\n\n')

acesso_liberado = False # variavel de controle
tentativa = 3
while tentativa > 0:
    confirmacao_senha = int(
    input('Para entrar no sistema, digite o PIN: '))

    if senha == confirmacao_senha:
        acesso_liberado = True
        break

    else:
        tentativa = tentativa - 1

    print(f'Você ainda tem {tentativa} tentativas')

# Se o acesso for liberado com sucesso, use um loop 
# for para simular uma contagem regressiva de 
# inicialização do sistema (de 5 até 1).

if acesso_liberado:
    for i in range(5, 0, -1):
        print(f'{i}...')
    print('Sistema Inicializado com Sucesso')
else:
    print('Acesso Negado. \nSua conta foi bloqueada')