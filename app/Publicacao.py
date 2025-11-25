from datetime import date
from typing import List
from app.Anotacao import Anotacao
from app.Colecao import Colecao

'''A Classe Publicação é a responsável por ser a base da criação de um livro. Origina duas subclasses: Livro e Revista '''
class Publicacao:
    def __init__(self, titulo, autor, ano, tipo, genero, ordem: List, numero_de_paginas, nota_avaliacao, status_leitura):      
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.tipo = tipo
        self.genero = genero
        self.anotacoes = Anotacao(self)
        self.colecao = Colecao(self)
        self.ordem = ordem
        self.numero_de_paginas = numero_de_paginas
        self._nota_avaliacao = nota_avaliacao
        self.status_leitura = status_leitura
        
    # Valida título e ano da publicação
    @property
    def titulo(self):
        print("Título da obra: ")
        return self._titulo

    @titulo.setter
    def titulo(self, valor_titulo: str):
        if valor_titulo == None:
            raise ValueError("Não é possível armazenar título vazio")
        self._titulo = valor_titulo

    @property
    def ano(self):
        print("Ano da Obra: ")
        return self._ano

    @ano.setter
    def ano(self, valor_ano: int):
        if valor_ano <= 1500:
            raise ValueError ("Ano inválido")
        self._ano = valor_ano

    @property
    def nota_avaliacao(self):
        print("Avaliação da obra: ")
        return self._nota_avaliacao

    @nota_avaliacao.setter
    def nota_avaliacao(self, valor_avaliacao: float):
        if valor_avaliacao < 0 or valor_avaliacao > 10:
            raise ValueError("Nota inválida")
        self._nota_avaliacao = valor_avaliacao

    @property
    def tipo(self):
        print("Tipo da Obra:")
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor_tipo: list):
        if valor_tipo != "livro" or valor_tipo != "revista":
            raise  ValueError("Tipo inválido!")
        self._tipo = valor_tipo

    # Métodos especiais
    def __str__(self):
        return f'"{self.titulo} de {self.autor}"'

    def __repr__(self):
        return f'{self.titulo}, de {self.autor}'

    def __lt__(self, other):
        return self.ano < other.ano

    def __eq__(self, other):
        if not isinstance(self, other):
            return NotImplemented
        return (self.titulo == self.titulo and self.autor == self.autor)
