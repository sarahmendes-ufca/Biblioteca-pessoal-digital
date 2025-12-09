from obra import Obra

class Colecao:
    def __init__(self, colecao: list):
        self.colecao = colecao

    def adicionar_obra(self, obra: Obra):
        if isinstance(obra, Obra):
            self.colecao.append(obra)
        else: 
            raise ValueError("Erro ao adicionar obra à coleção.")
