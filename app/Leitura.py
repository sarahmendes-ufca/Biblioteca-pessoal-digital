rom enum import Enum

'''Classe Leitura engloba o status do livro, o início e o término da leitura'''

class Leitura(Enum):
    NAO_LIDO = "NÃO LIDO"
    LENDO = "LENDO"
    LIDO = "LIDO"

    def status_leitura(self):
        pass 
    
    def iniciar_leitura(self):
        pass

    def concluir_leitura(self):
        pass
