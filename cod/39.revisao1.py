# Crie uma função em Python chamada 
# registrar_evento(usuario, acao, status) que receba o nome do 
# usuário, a ação executada (ex: LOGIN, SAQUE, EXCLUSAO) e o 
# status da operação (SUCESSO ou FALHA). 

# O programa deve anexar cada registro em uma nova linha no 
# arquivo auditoria_sistema.log, contendo a data e a hora 
# do momento exato em que a ação ocorreu, sem sobrescrever 
# os registros anteriores.

from datetime import datetime

def registrar_evento(usuario, acao, status):
    with open('auditoria_sistema.log', 'a', 
              encoding='utf-8') as arquivo:
        data_formatada = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        arquivo.write(f'{usuario}, {acao}, {status}, {data_formatada}\n')

registrar_evento('USUARIO', 'LOGIN', 'SUCESSO')