from Publicacao import Publicacao

class Revista(Publicacao):

    # A lista é vazia na classe Pai.
    lista_genero = [
        'Notícia', 'Reportagem', 'Entrevista', 'Artigo',
        'Charge', 'Editorial', 'Resenha'
        ]

    def __init__(self, titulo, autor, ano, tipo, genero, ordem,
                 numero_de_paginas, nota_avaliacao, status_leitura):
        
        if genero not in self.lista_genero:
            raise ValueError("Gênero inválido")

        super().__init__(
            titulo=titulo,
            autor=autor,
            ano=ano,
            tipo=tipo,
            genero=genero,
            ordem=ordem,
            numero_de_paginas=numero_de_paginas,
            nota_avaliacao=nota_avaliacao,
            status_leitura=status_leitura
        )

    @property
    def titulo(self):
        print("Título da Revista: ")
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Não é possível armazenar título vazio")
        self._titulo = valor

    @property
    def ano(self):
        print("Ano da Revista: ")
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor <= 1500:
            raise ValueError("Ano inválido")
        self._ano = valor

    @property
    def nota_avaliacao(self):
        print("Avaliação da Revista: ")
        return self._nota_avaliacao

    @nota_avaliacao.setter
    def nota_avaliacao(self, valor):
        if not (0 <= valor <= 10):
            raise ValueError("Nota inválida")
        self._nota_avaliacao = valor
