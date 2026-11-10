# Desenvolva um programa que simule a coleta e armazenamento de dados de 5 
# candidatos a vagas de emprego:
# Cada candidato deve ser representado por um dicionário com os campos: 
# "nome", "idade", "telefone", "email" e "formacao".
# Todos os candidatos aprovados na triagem devem ser armazenados em uma 
# lista principal chamada banco_candidatos
banco_candidatos = []

for i in range(2):
    nome = input('Digite o nome do candidato: ')
    idade = int(input('Digite a idade do candidato: '))
    telefone = input('Digite o telefone do candidato: ')
    email = input('Digite o email do candidato: ')
    formacao = input('Digite a formação do candidato: ')
    # Regra de negócio: Candidatos com idade inferior a 18 anos não podem 
    # participar do processo. 
    # Caso a idade informada seja menor que 18, o programa deve rejeitar 
    # o registro, exibir uma mensagem de recusa e não inserir o candidato na lista.

    if idade < 18:
        print('Só pode participar do processo maiores de 18 anos')
        continue

    candidato = {
        'nome': nome,
        "idade": idade,
        'telefone': telefone,
        'email': email,
        'formacao': formacao
    }

    if not '@' in candidato['email']:
        print('Email invalido')

    banco_candidatos.append(candidato)
# Ao término da entrada de dados, o sistema deve iterar sobre banco_candidatos 
# e exibir um relatório contendo: Nome, E-mail e Formação de cada candidato apto.

# print(banco_candidatos)

for i in range(len(banco_candidatos)):
    print(banco_candidatos[i]['nome'], '\t', banco_candidatos[i]['email'],
          '\t', banco_candidatos[i]['formacao'])

for candidato in banco_candidatos:
    print(candidato['nome'], '\t', candidato['email'], '\t', candidato['formacao'])
