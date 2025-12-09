from obra import Obra
from livro import Livro
from typing import Optional
from datetime import datetime
class Anotacao:
    def __init__(self, obra: Obra, texto: str, trecho: Optional[str]):
        if not isinstance(obra, Obra):
            raise TypeError("Anotacao precisa de uma instância concreta de Obra")
        self.obra = obra
        self.texto = texto
        self.trecho = trecho
        self.data_texto = datetime.now().strftime("%d/%m/%y")
        self.lista_anotacoes = []

    def adicionar_anotacao(self):
        bloco = {
            "data": self.data_texto,
            "anotacao": self.texto,
            "trecho": self.trecho
        }
        self.lista_anotacoes.append(bloco)
        print("Anotação adicionada com sucesso.")
        
    def mostar_anotacoes(self):
        if not self.lista_anotacoes:
            return("Ainda não há anotações")
        for i, anotacao in enumerate(self.lista_anotacoes):
            print(f"Anotação {i+1}:")
            print(f"  data: {anotacao['data']}")
            print(f"  trecho: '{anotacao['trecho']}'")
            print(f"  anotacao: '{anotacao['anotacao']}'")
