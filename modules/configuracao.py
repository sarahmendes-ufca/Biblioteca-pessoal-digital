from datetime import date
from colecao import Colecao
from leitura import Leitura
import json

class Configuracao:
    def __init__(self, genero_favorito = None, meta_anual_leitura = None, numero_leitura_simultanea = None):
        self.genero_favorito = genero_favorito
        self.meta_anual_leitura = meta_anual_leitura
        self.numero_leitura_simultanea = numero_leitura_simultanea

    def mostrar_json(self):
        parametros_opcionais = {
            "genero_favorito": self.genero_favorito,
            "meta_anual_leitura": self.meta_anual_leitura,
            "numero_leitura_simultanea": self.numero_leitura_simultanea
        }
        with open('settings.json', 'w', encoding='utf-8') as configuracoes:
            json.dump(parametros_opcionais, configuracoes, indent=4, ensure_ascii=False)

    def emitir_aviso(self, leituras: list[Leitura]) -> None:
        if not self.meta_anual_leitura:
            return
        ano_atual = date.today().year
        leituras_concluidas = [
            leitura for leitura in leituras
            if leitura.data_termino is not None and leitura.data_termino == ano_atual
        ]

        total_concluidas = len(leituras_concluidas)

        if total_concluidas < self.meta_anual_leitura:
            print(f"Atenção! Sua meta de leitura não foi concluida.")
