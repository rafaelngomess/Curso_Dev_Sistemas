
renda_mensal = 25000.0
score = 800
possui_restricao = False

if (not possui_restricao and score >= 700 
    and renda_mensal >= 4000):
    print('Empréstimo Aprovado')

elif (not possui_restricao and renda_mensal >= 2500
      and (score >= 500 or renda_mensal > 6000)):
    print('Analise Manual')

else:
    print('Empréstimo Reprovado')

