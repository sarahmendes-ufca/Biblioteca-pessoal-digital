from typing import Optional
from datetime import date

'''A Classe Anotação permite registrar e listar anotações relacionadas à uma publicação '''
class Anotacao:
    def __init__ (self, texto, trecho = Optional[str], data = date):
        self.texto = texto
        self.trecho = trecho
        self.data = data
    
    def adicionar_anotacao(self, texto: str, trecho: Optional[str] = None):
        pass

    def listar_anotacoes(self):
        pass
