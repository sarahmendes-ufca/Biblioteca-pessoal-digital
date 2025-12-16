from models.livro import Livro
from models.leitura import Leitura

class LivroCLI:
    def menu_livro(self):
        print(" ____________________________________")
        print("| 1 - Adicionar Livro                |")
        print("|____________________________________|")
        print("| 2 - Visualizar Livro               |")
        print("|____________________________________|")
        print("| 3 - Atualizar Livro                |")
        print("|____________________________________|")
        print("| 4 - Deletar Livro                  |")
        print("|____________________________________|")
        print("| 5 - Sair                           |")
        print("|____________________________________|")
        opcao_acoes_livro = input("Escolha uma opção: ").strip()
    
        if opcao_acoes_livro == "1":
            self.adicionar_livro()
        
        elif opcao_acoes_livro == "2":
            self.listar_livro_cli()

        elif opcao_acoes_livro == "3":
            self.atulizar_livro_cli()

        elif opcao_acoes_livro == "4":
            self.deletar_livro_cli()

        elif opcao_acoes_livro == "5":
            print("Saindo")
            return
        
        else:
            print("Opção inválida!")

    def adicionar_livro(self, avaliacao = None):
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        genero = input("Gênero: ")
        numero_paginas = int(input("Numero de páginas: "))
        avaliacao = None
        livro = Livro(titulo, ano, autor, genero, numero_paginas, avaliacao)
        livro.salvar_no_banco()

    def listar_livro_cli(self):
        titulo = input("Digite o titulo da obra:")
        if titulo:
            livros = Livro.listar_obras(titulo)
        else:
            livros = Livro.listar_obras()

        if not livros:
            print("Nenhum livro encontrado.")
            return

        for livro in livros:
            print(livro)

    def atulizar_livro_cli(self):
        print("Atenção: Todos os campos devem ser preenchidos para atualizar a obra.")
        id_obra = int(input("Digite o ID da obra: "))
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        genero = input("Gênero: ")
        numero_paginas = int(input("Numero de páginas: "))
        resp = input("Deseja incluir avaliação: ")
        if resp == "sim" or resp == "s":
            avaliacao = float(input("Avaliação: "))
        elif resp == "nao" or resp == "n":
            avaliacao = None
        else:
            print("Resposta inválida!")
        Livro.atualizar_obra(id_obra, titulo, ano, autor, genero, numero_paginas, avaliacao)


    def deletar_livro_cli(self):
        id_obra = int(input("Id da obra: "))
        Livro.deletar_obra(id_obra)
        