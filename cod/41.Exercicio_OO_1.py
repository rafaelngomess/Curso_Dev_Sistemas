# Crie uma classe chamada Aluno para gerenciar a nota de um estudante de 
# forma segura:

# i. O construtor __init__ deve receber o nome do aluno e a sua nota inicial.

class Aluno:
    # ii. Guarde o nome como atributo público comum (self.nome = nome).
    # iii. Proteja o atributo da nota utilizando um underline (self._nota).

    def __init__(self, nome, nota):
        self.nome = nome
        self.abobora = nota # validação

        self._nota = nota # salvando a nota (se passar pela validação)

        # vi. No construtor __init__, atribua self.nota = nota (sem underline) 
        # para forçar que a validação do setter já ocorra na hora de criar o objeto.
        
        
    # iv. Crie um @property para permitir a leitura de nota.
    # Isso seria um get
    # em JAVA seria public function get_nota() { return this.nota; }
    # se não fosse @property # JAVANÊS
    # def get_nota(self):
    #     return self._nota
    @property # permite ler a variavel como se fosse assim: aluno.nota
    def abobora(self):
        return self._nota

    # v. Crie um @nota.setter que só permita alterar a nota se o valor 
    # estiver entre 0.0 e 10.0. Caso contrário, exiba uma mensagem de erro e 
    # rejeite a alteração.
    @abobora.setter
    def abobora(self, nova_nota):
        # só muda se estiver entre 0.0 e 10.0
        # if 0.0 <= nova_nota <= 10.0: # jeito python
        if nova_nota >= 0.0 and nova_nota <= 10.0:
            self._nota = nova_nota
        else:
            print(f'[Erro] Nota Inválida: {nova_nota}.\
                   \nA nota deve estar entre 0 e 10.')

    # vii. Crie uma propriedade somente-leitura chamada aprovado 
    # (apenas com @property, sem setter) que retorne True 
    # se a nota for maior ou igual a 6.0, e False caso contrário.
    @property
    def situacao(self):
        # True caso seja >= 6.0 // False caso contrario
        return self._nota >= 6.0

    # esse método permite que você print objetos na tela/arquivo
    def __str__(self):
        return f'class <Aluno> Nome: {self.nome}, Nota: {self._nota}, Aprovado: {self.situacao}'

bene = Aluno('Bene', 10)
print(bene)

alex = Aluno('Alex', 18)
# print(alex.nota)
alex.abobora = 15

# rode uma das 3 linhas abaixo para instalar o pydantic
    # pip install pydantic
    # python -m pip install pydantic
    # py -m pip install pydantic

# from pydantic import BaseModel, Field

# class Aluno(BaseModel):
#     nome : str
#     nota : float = Field(ge=0.0, le=10.0)
#     # greater than (maior ou igual do que)
#     # lesser than (menor ou igual do que)