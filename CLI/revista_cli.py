from models.revista import Revista

class RevistaCLI:
    def menu_revista(self):
            print(" ____________________________________")
            print("| 1 - Adicionar Revista              |")
            print("|____________________________________|")
            print("| 2 - Visualizar Revista             |")
            print("|____________________________________|")
            print("| 3 - Atualizar Revista              |")
            print("|____________________________________|")
            print("| 4 - Deletar Revista                |")
            print("|____________________________________|")
            print("| 5 - Sair                           |")
            print("|____________________________________|")
            opcao_acoes_revista = input("Escolha uma opção: ")
        
            if opcao_acoes_revista == "1":
                self.adicionar_revista_cli()
            
            elif opcao_acoes_revista == "2":
                self.atulizar_revista_cli()

            elif opcao_acoes_revista == "3":
                self.atulizar_revista_cli()
            
            elif opcao_acoes_revista == "4":
                self.deletar_revista_cli()

            elif opcao_acoes_revista == "5":
                print("Saindo do menu Revista.")
                return
            
            else:
                print("Opção inválida!")

    def adicionar_revista_cli(self, avaliacao = None):
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        genero = input("Gênero: ")
        numero_paginas = int(input("Numero de páginas: "))
        avaliacao = None
        revista = Revista(titulo, ano, autor, genero, numero_paginas, avaliacao)
        revista.salvar_no_banco()

    def listar_livro_cli(self):
        titulo = input("Digite o titulo da obra:")
        if titulo:
            revistas = Revista.listar_obras(titulo)
        else:
            revistas = Revista.listar_obras()

        if not revistas:
            print("Nenhum livro encontrado.")
            return

        for revista in revistas:
            print(revista)

    def atulizar_revista_cli(self):
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
        Revista.atualizar_obra(id_obra, titulo, ano, autor, genero, numero_paginas, avaliacao)


    def deletar_revista_cli(self):
        id_obra = int(input("Id da obra: "))
        Revista.deletar_obra(id_obra)
        