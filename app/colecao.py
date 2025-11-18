from datetime import date

'''Agrupa as obras do usuário e permite buscar essas publicações por filtro'''
class Colecao:
    def __init__(self, publicacoes = None):
        self.publicacoes = publicacoes

    def adicionar_publicacao(self, pub):
        pass

    def buscar_por_titulo(self, titulo):
        pass

    def buscar_por_autor(self, autor: str):
        pass

    def buscar_por_genero(self, genero: str):
        pass

    def filtrar_por_status(self, status):
        pass

    def filtrar_por_periodo(self, inicio: date, fim: date):
        pass

    def total_publicacoes(self):
        pass

    def publicacoes_lidas(self):
        pass

    def media_avaliacoes(self):
        pass
