from obra import Obra

class Revista(Obra):
    def __init__ (self, titulo, ano, editora, tipo, genero, numero_paginas, avaliacao):
        super().__init__(titulo, ano, tipo, numero_paginas, avaliacao)
        self.editora = editora
        self.genero = genero

    @property
    def editora(self):
        print("Autor da Obra: ")
        return self._editora
    
    @editora.setter
    def autor(self, editora_valida):
        if editora_valida == "":
            raise ValueError("Editora inválida! O campo não pode ser vazio!")
        else: 
            self._editora = editora_valida

    @property
    def genero(self):
        print("Gênero do livro: ")
        return self._genero
    
    @genero.setter
    def genero(self, genero_valido):
        if genero_valido not in ('noticia', 'reportagem', 'entrevista', 'editorial', 'cronica', 'resenha', 'opiniao'):
            raise ValueError("Gênero inválido")
        else:
            self._genero = genero_valido

livro = Revista("Dom Casmurro", 1888, "Machado_de_Assis", "livro","epico", 280, 8.9)
print(livro.titulo)
print(livro.ano)
print(livro.autor)
print(livro.tipo)
print(livro.genero)
print(livro.numero_paginas)
print(livro.avaliacao)    