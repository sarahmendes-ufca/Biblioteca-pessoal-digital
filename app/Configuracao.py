from typing import Optional

class Configuracao:
    def __init__ (self, genero_favorito = Optional[str], limite_paginas_leitura_simultanea = Optional[int], meta_leitura_anual = Optional[str]):
        self.genero_favorito = genero_favorito
        self.limite_paginas_leitura_simultanea = limite_paginas_leitura_simultanea
        self.meta_leitura_anual = meta_leitura_anual

    def carregar_de_json(self):
        pass

    def salvar_em_json(self):
        pass


