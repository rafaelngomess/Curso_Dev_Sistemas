filmes = ['Transformer', 'Os Smurfs',
          'Interstellar', 'Vingadores',
          'Sexta-Feira 13', 'Frozen', 'Shrek']

# ordena a lista de forma crescente (padrão)
filmes.sort()

# ordena a lista de forma decrescente (maior para menor)
filmes.sort(reverse=True)
print(filmes)

print(60*'=')

# ordernar e salvar em outro local
filmes2 = sorted(filmes)

print(filmes2)
print(60*'=')

filmes2.insert(2, 'João e Maria')
print(filmes2)


print(filmes2.index('Shrek'))
