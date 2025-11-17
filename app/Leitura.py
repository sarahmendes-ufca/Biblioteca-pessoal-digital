from enum import Enum

class Leitura(Enum):
    NAO_LIDO = "NÃO LIDO"
    LENDO = "LENDO"
    LIDO = "LIDO"

    def iniciar_leitura(self):
        pass

    def concluir_leitura(self):
        pass