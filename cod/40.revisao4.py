# A secretaria de uma escola técnica disponibilizou o 
# arquivo notas_turma.csv com as colunas matricula, aluno, nota1 
# e nota2.

# Construa um programa em Python que leia esses registros e 
# calcule a média aritmética de cada aluno.
# Se a média final for maior ou igual a 7.0, o aluno recebe a 
# situação "APROVADO"; caso contrário, recebe "REPROVADO".
# O programa deve gerar o arquivo boletim_final.csv contendo as 
# notas originais, a média final arredondada para uma casa 
# decimal e a situação acadêmica calculada.

import csv

with (
    open('04.arquivo.csv', 'r', encoding='utf-8') as ENTRADA,
    open('boletim_final.csv', 'a', encoding='utf-8') as SAIDA
):
    # é um csv, então devo criar um leitor
    leitor = csv.DictReader(ENTRADA, delimiter=';')

    escritor = None

    for aluno in leitor:
        media = (float(aluno['nota1']) + 
                 float(aluno['nota2']))/2
        status = 'REPROVADO'
        if media >= 7:
            status = 'APROVADO'

        aluno['status'] = status
        aluno['media'] = f'{media:.1f}'

        if escritor is None:
            cabecalho = list(aluno.keys())
            escritor = csv.DictWriter(SAIDA, 
                                      fieldnames=cabecalho,
                                      delimiter=';')
            escritor.writeheader()

        escritor.writerow(aluno)

        