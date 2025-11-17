from Usuario import Colecao

'''A Classe Usuário registra o nome, coleção de Publicações e permite o acesso às Configurações'''
class Usuario:
    def __init__(self, nome, colecao = None, configuracao = None):
        self.nome = nome
        self.colecao = colecao or Colecao()
        self.configuracao = configuracao

    def carregar_configuracoes(self):
        pass

    def salvar_configuracoes(self):
        pass