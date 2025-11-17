from datetime import date
from typing import List
from typing import Optional

class Publicacao:
    def __init__(self, id_publicacao, titulo, autor, ano, tipo, genero, numero_de_paginas, nota_avaliacao, status_leitura, avaliacao, data_inclusao, data_inicio, data_fim, anotacoes):      
        self.id_publicacao = id_publicacao
        titulo = str
        autor = str
        ano = int
        tipo = str
        genero = str
        numero_de_paginas = int
        nota_avaliacao = int
        status_leitura = str
        avaliacao = Optional[float]
        data_inclusao = date
        data_inicio = Optional[date]
        data_fim = Optional[date]
        anotacoes = Optional[List]

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O título não pode ser vazio.")
        self._titulo = valor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor: int):
        if valor < 1500:
            raise ValueError("O ano deve ser maior ou igual a 1500.")
        self._ano = valor

    @property
    def nota_avaliacao(self):
        return self._nota_avaliacao

    @nota_avaliacao.setter
    def nota_avaliacao(self, valor: float):
        if not (0 <= valor <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota_avaliacao = valor

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

    def iniciar_leitura(self):
        pass

    def concluir_leitura(self):
        pass

    def adicionar_anotacao(self, texto: str, trecho: Optional[str] = None):
        pass

    def listar_anotacoes(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass
