from abc import ABC, abstractmethod
class Obra(ABC):
    def __init__(self, titulo, ano, tipo, numero_paginas, avaliacao = None):
        self.titulo = titulo
        self.ano = ano
        self.tipo = tipo
        self.numero_paginas = numero_paginas
        self.avaliacao = avaliacao

    @property
    @abstractmethod
    def titulo(self):
        pass
    
    @titulo.setter
    @abstractmethod
    def titulo(self, titulo_valido: str):
        pass    

    @property
    def ano(self):
        pass
    
    @ano.setter
    @abstractmethod
    def ano(self, ano_valido):
        pass

        
    @property
    @abstractmethod
    def tipo(self):
        pass
    
    @tipo.setter 
    @abstractmethod
    def tipo(self, tipo_valido):
        pass
        
    @property
    @abstractmethod
    def numero_paginas(self):
        pass
    
    @numero_paginas.setter
    @abstractmethod
    def numero_paginas(self, numero_paginas_valido):
        pass

    @property
    @abstractmethod
    def avaliacao(self):
        pass
    
    @avaliacao.setter
    @abstractmethod
    def avaliacao(self, avaliacao_valido):
        pass
    
