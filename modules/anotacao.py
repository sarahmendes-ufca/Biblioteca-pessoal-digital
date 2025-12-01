from typing import Optional
from datetime import datetime
class Anotacao:
    def __init__(self, texto: str, trecho: Optional[str]):
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

# Instância da classe Anotação

nova_anotacao = Anotacao("Não gostei desse personagem", "exemplo")
nova_anotacao.adicionar_anotacao()
nova_anotacao.mostar_anotacoes()
print(nova_anotacao.lista_anotacoes)