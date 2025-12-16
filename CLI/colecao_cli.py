from models.colecao import Colecao
import sqlite3

class ColecaoCLI:
    def menu_colecao(self):
        print(" ____________________________________")
        print("| 1 - Adicionar Obra à Coleção       |")
        print("|____________________________________|")
        print("| 2 - Listar Obra na Coleção         |")
        print("|____________________________________|")
        print("| 3 - Sair                           |")
        print("|____________________________________|")
        print("| 4 - Bib Mostrar obras cadastradas  |")
        print("|____________________________________|")
        opcao_acoes_colecao = input("Escolha uma opção: ").strip()
    
        if opcao_acoes_colecao == "1":
            self.adicionar_obra_cli()
        
        elif opcao_acoes_colecao == "2":
            self.listar_obra_cli()

        elif opcao_acoes_colecao == "3":
            print("Saindo dp menu Coleção.")
            return
        elif opcao_acoes_colecao == "4":
            conn = sqlite3.connect('biblioteca.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM obra")
            registros = cursor.fetchall()
            print(f"Registros na tabela 'obra':")
            for registro in registros:
                print(registro)
            conn.close()

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
