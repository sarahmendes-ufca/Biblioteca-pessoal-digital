from models.obra import Obra
'''Subclasse de Obra. A classe Revista permite adicionar, ler, mmodificar e deletar obras do tipo revista.
    A classe contém os gêneros específicos do seu tipo, como editorial ou opiniao.'''
class Revista(Obra):
    def __init__ (self, titulo, ano, autor, genero, numero_paginas, avaliacao = None, db_path ='biblioteca.db'):
        super().__init__(titulo, ano, autor, "revista", genero, numero_paginas, avaliacao, db_path)

    @property
    def genero(self):
        print("Gênero da revista: ")
        return self._genero
    
    @genero.setter
    def genero(self, genero_valido):
        if genero_valido not in ('noticia', 'reportagem', 'entrevista', 'editorial', 'cronica', 'resenha', 'opiniao'):
            raise ValueError("Gênero inválido")
        else:
            self._genero = genero_valido

 
 