from models.relatorio import Relatorio

class RelatorioCLI:
    def mostrar_relatorios(self):
        relatorio =  Relatorio()
        relatorio.gerar_grafico_obras()
        relatorio.gerar_grafico_status()
        relatorio.gerar_grafico_media_avaliacoes()