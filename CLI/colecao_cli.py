from models.colecao import Colecao

class ColecaoCLI:
    def menu_colecao(self):
        print(" ____________________________________")
        print("| 1 - Adicionar Obra à Coleção       |")
        print("|____________________________________|")
        print("| 2 - Listar Obra na Coleção         |")
        print("|____________________________________|")
        print("| 3 - Sair                           |")
        print("|____________________________________|")
        opcao_acoes_colecao = input("Escolha uma opção: ").strip()
    
        if opcao_acoes_colecao == "1":
            self.adicionar_obra_cli()
        
        elif opcao_acoes_colecao == "2":
            self.listar_obra_cli()

        elif opcao_acoes_colecao == "3":
            print("Saindo dp menu Coleção.")
            return
        
        else: 
            print("Opção inválida!")

    def adicionar_obra_cli(self):
        id_obra = int(input("Digite o ID: "))
        add = Colecao(id_obra)
        add.adicionar_obra_colecao(id_obra)

    def listar_obra_cli(self):
        id_obra = int(input("Digite o ID: "))
        add = Colecao(id_obra)
        add.listar_obras_colecao()