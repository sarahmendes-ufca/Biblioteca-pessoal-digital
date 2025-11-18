from datetime import date
from typing import List
from typing import Optional

'''A Classe Publicação é a responsável por ser a base da criação de um livro. Origina duas subclasses: Livro e Revista '''
class Publicacao:
    def __init__(self, id_publicacao, titulo, autor, ano, tipo, genero, numero_de_paginas, nota_avaliacao, status_leitura, avaliacao):      
        self.id_publicacao = id_publicacao
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.tipo = tipo
        self.genero = genero
        self.numero_de_paginas = numero_de_paginas
        self.nota_avaliacao = nota_avaliacao
        self.status_leitura = status_leitura
        self.avaliacao = avaliacao
        
    @property
    def titulo(self):
        pass

    @titulo.setter
    def titulo(self, valor = str):
        pass

    @property
    def ano(self):
        pass

    @ano.setter
    def ano(self, valor: int):
        pass

    @property
    def nota_avaliacao(self):
        pass

    @nota_avaliacao.setter
    def nota_avaliacao(self, valor: float):
        pass

    def adicionar_publicacao(self):
        pass

    def buscar_publicacao(self):
        pass

    def atualizar_publicacao(self):
        pass

    def apagar_publicacao(self):
        pass

    def avaliar_publicacao(self, valor):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass

class Livro(Publicacao):
    pass

class Revista(Publicacao):
    pass
