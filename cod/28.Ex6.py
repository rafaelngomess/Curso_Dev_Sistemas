# Uma rota administrativa da API exige o seguinte conjunto de permissões para 
# ser executada:

permissoes_rota = {'AUTH_READ', 'AUTH_WRITE', 'DB_ADMIN', 'LOG_EXPORT'}

# O sistema recuperou as permissões atribuídas a dois perfis de usuários distintos:
usuario_analista = {"AUTH_READ", "LOG_EXPORT"}
usuario_techlead = {"AUTH_READ", "AUTH_WRITE", "DB_ADMIN", "LOG_EXPORT", 
                    "BILLING_ACCESS"}

# Desenvolva a lógica que:
# Identifique se cada um dos usuários tem acesso permitido à rota 
# (todas as permissões de permissoes_rota devem estar contidas no 
#  conjunto do usuário).

# analista
if permissoes_rota.issubset(usuario_analista):
    print('Usuario Analista Validado, acesso permitido')
else:
    print(f'Faltam essas permissoes: {permissoes_rota.difference(usuario_analista)}')

if usuario_techlead.issuperset(permissoes_rota):
    print('Usuario TechLead Validado, acesso permitido')

# Para o usuário que não tiver acesso, calcule e exiba via diferença entre 
# conjuntos (difference ou operador -) exatamente quais permissões estão 
# faltando para liberar o acesso.

