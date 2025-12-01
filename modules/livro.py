from obra import Obra

class Livro(Obra):
    def __init__ (self, titulo, ano, autor, tipo, genero, numero_paginas, avaliacao):
        super().__init__(titulo, ano, autor, tipo, numero_paginas, avaliacao)
        self.genero = genero

    @property
    def genero(self):
        print("Gênero do livro: ")
        return self._genero
    
    @genero.setter
    def genero(self, genero_valido):
        if genero_valido not in ("fantasia", "ficcao", "poseia", "epico", "peca", "romance", "drama", "terror", "suspense" ):
            raise ValueError("Gênero inválido")
        else:
            self._genero = genero_valido

livro = Livro("Dom Casmurro", 1888, "Machado_de_Assis", "livro","epico", 280, 8.9)
print(livro.titulo)
print(livro.ano)
print(livro.autor)
print(livro.tipo)
print(livro.genero)
print(livro.numero_paginas)
print(livro.avaliacao)    