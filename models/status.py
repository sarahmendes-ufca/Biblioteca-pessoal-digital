from enum import Enum
'''Classe Status define valores constantes para os 3 status de leitura'''
class Status(Enum):
    NAO_LIDO = "NAO_LIDO"
    LENDO = "LENDO"
    LIDO = "LIDO"