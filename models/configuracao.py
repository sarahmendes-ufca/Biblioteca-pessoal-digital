
import json
import os
'''Classe Configuracao controla os parametros opcionais e controla o 'settings.json'.'''
NAO_INFORMADO = object()


class Configuracao:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ARQUIVO = os.path.join(BASE_DIR, "..", "settings.json")

    def __init__(self):
        self.genero_favorito = None
        self.meta_anual_leitura = None
        self.numero_leitura_simultanea = None


        self.carregar()

    def carregar(self):
        if not os.path.exists(self.ARQUIVO):
            return

        with open(self.ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)

        self.genero_favorito = dados.get("genero_favorito") or "Indefinido"
        self.meta_anual_leitura = int(dados.get("meta_anual_leitura") or 0)
        self.numero_leitura_simultanea = int(dados.get("numero_leitura_simultanea") or 1)

    def atualizar(
        self,
        genero_favorito=NAO_INFORMADO,
        meta_anual_leitura=NAO_INFORMADO,
        numero_leitura_simultanea=NAO_INFORMADO
    ):
        if genero_favorito is not NAO_INFORMADO:
            self.genero_favorito = genero_favorito

        if meta_anual_leitura is not NAO_INFORMADO:
            self.meta_anual_leitura = meta_anual_leitura

        if numero_leitura_simultanea is not NAO_INFORMADO:
            self.numero_leitura_simultanea = numero_leitura_simultanea

        self.salvar()

    def salvar(self):
        dados = {
            "genero_favorito": self.genero_favorito,
            "meta_anual_leitura": self.meta_anual_leitura,
            "numero_leitura_simultanea": self.numero_leitura_simultanea
        }

        with open(self.ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

