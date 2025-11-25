from typing import Optional
from datetime import date
from datetime import datetime

'''A Classe Anotação permite registrar e listar anotações relacionadas à uma publicação '''
class Anotacao:
    def __init__ (self, publicacao, texto, trecho: Optional[str], data_texto = None):
        self.publicacao = publicacao
        self.anotacoes = []
        self.texto = texto
        self.trecho = trecho
        self.data_texto = data_texto
    
    def adicionar_anotacao(self, publicacao, trecho, data_texto = None):
        if data_texto is None:
            data_texto= datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        else:
            print("Sem data")
        nova_anotacao = {
            "Título": publicacao,
            "Trecho": trecho,
            "Data": data_texto
        }
        self.anotacoes.append(nova_anotacao)
        print(f"Anotação adicionada em {self.titulo}, em {self.data_texto}")

    def listar_anotacoes(self):
        print(f"Anotações de {self.publicacao}")
        if not self.anotacoes:
            print("Ainda não há anotações")
        for i, anotacao in enumerate(self.anotacoes):
            print(f"Anotação {i+1}:")
            print(f"  Data: {anotacao['data_texto']}")
            print(f"  Trecho: '{anotacao['trecho']}'")
            print(f"  Texto Livre: '{anotacao['texto']}'")
