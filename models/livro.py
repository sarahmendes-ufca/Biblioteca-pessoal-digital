from models.obra import Obra

'''Subclasse de Obra. A classe Livro permite adicionar, ler, mmodificar e deletar obras do tipo livro.
    A classe contém os gêneros específicos do seu tipo, como romance ou terror.'''

class Livro(Obra):
    def __init__ (self, titulo, ano, autor, genero, numero_paginas, avaliacao = None, db_path="biblioteca.db"):
        super().__init__(titulo, ano, autor, "livro", genero, numero_paginas, avaliacao, db_path)

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero_valido):
        if genero_valido == "":
                raise ValueError("Gênero inválido! O campo não pode ser vazio!")
        else: 
            self._genero = genero_valido

        
