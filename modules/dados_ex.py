from dados import Dados
from conexao import Conexao
Conexao()

db = Dados()

db.adicionar_obra("Dom Casmurro", 1899, "Machado de Assis", "Romance", "Clássico", 256, 9.5, "LIDO")
db.adicionar_obra("A Hora da Estrela", 1975, "Clarisse Lispector", "Drama", "livro", 80, 9.2, "LENDO")

print(db.listar_obras())

db.adicionar_anotacao(1, "Ótimo capítulo inicial", "Capítulo 1", "2025-11-30")

print(db.listar_anotacoes(1))