from status import Status
from obra import Obra
from datetime import datetime

class Leitura:
    def __init__(self, obra: Obra, data_inicio = None, data_termino = None, status_leitura = Status.NAO_LIDO):
        self.obra = obra
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.status_leitura = status_leitura
            
    def iniciar_leitura(self):
        if self.status_leitura != Status.NAO_LIDO:
            raise ValueError("Leitura já iniciada ou concluída.")
        else:
            self.data_inicio = datetime.now().strftime("%d/%m/%y")
            self.status_leitura = Status.LENDO
                
    def concluir_leitura(self):
        if  self.status_leitura != Status.LENDO:
            raise ValueError("Você deve iniciar a leitura antes de concluir.")
        else:
            self.status_leitura = Status.LIDO
            self.data_termino =  datetime.now().strftime("%d/%m/%y")

    def verificar_status_leitura(self):
        print(f'Título: {self.obra.titulo} \n Status: {self.status_leitura.name}')
