cargo = input('Digite o cargo: ')
hora = int(input('Digite o horario atual (em horas): '))
chave_emergencia = int(input('Possui chave de emergencia? (1 para sim, 0 para não):'))

if (chave_emergencia or cargo == 'Supervisor' or
    (cargo == 'Operador' and 8 <= hora <= 17)):
    print('Acesso Permitido')
else:
    print('Acesso Bloqueado')