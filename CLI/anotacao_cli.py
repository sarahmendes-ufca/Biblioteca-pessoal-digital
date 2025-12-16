from models.anotacao import Anotacao
from datetime import datetime
import sqlite3

class AnotacaoCLI:
    def menu_anotacao(self):
        print(" ____________________________________")
        print("| 1 - Adicionar Anotação             |")
        print("|____________________________________|")
        print("| 2 - Visualizar Anotação            |")
        print("|____________________________________|")
        print("| 3 - Atualizar Anotação             |")
        print("|____________________________________|")
        print("| 4 - Deletar Anotação               |")
        print("|____________________________________|")
        print("| 5 - Sair                           |")
        print("|____________________________________|")
        print("| 6 - Bib Mostrar obras cadastradas  |")
        print("|____________________________________|")
        opcao_acoes_anotacao = input("Escolha uma opção: ")
        
        if opcao_acoes_anotacao == "1":
            self.adicionar_anotacao_cli()
        elif opcao_acoes_anotacao == "2":
            self.visualizar_anotacao_cli() 
        elif opcao_acoes_anotacao == "3":
            self.atualizar_anotacao_cli() 
        elif opcao_acoes_anotacao == "4":
            self.deletar_anotacao()
        elif opcao_acoes_anotacao == "5":
            print("Saindo do Menu de Anotações")
            return
        elif opcao_acoes_anotacao == "6":
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


    def adicionar_anotacao_cli(self, trecho = None):
        id_obra = int(input("Id da obra: "))
        texto = input("Texto: ")
        resp = input("Deseja incluir trecho? ")
        if resp == "sim" or resp == "s":
            trecho = input("Trecho:" )
            data = datetime.now().strftime("%d-%m-%Y")
        elif resp == "nao" or resp == "n":
            trecho = None
            data = datetime.now().strftime("%d-%m-%Y")
        else:
            print("Resposta inválida!")
            data = datetime.now().strftime("%d-%m-%Y")
        anotacao = Anotacao(id_obra, texto, trecho, data)
        anotacao.adicionar_anotacao(id_obra, texto, trecho, data)

    def visualizar_anotacao_cli(self):
        id_obra = int(input("Id da obra: "))
        anotacao = Anotacao(id_obra)
        anotacoes = anotacao.listar_anotacoes(id_obra)

        if not anotacoes:
            print("Nenhuma anotação encontrada.")
            return

        for a in anotacoes:
            print(f"""
            ID: {a[0]}
            Texto: {a[2]}
            Trecho: {a[3]}
            Data: {a[4]}
            ------------------
            """)
    
    def atualizar_anotacao_cli(self):
        id_obra = int(input("Id da obra: "))
        texto = input("Texto: ")
        resp = input("Deseja incluir trecho? ")
        if resp == "sim" or resp == "s":
            trecho = input("Trecho:" ).strip()
        elif resp == "nao" or resp == "n":
            trecho = None
        else:
            print("Resposta inválida!")
        data = datetime.now().strftime("%d-%m-%Y")
        anotacao = Anotacao(id_obra, texto, trecho, data)
        anotacao.atualizar_anotacao(id_obra, texto, trecho, data)

    def deletar_anotacao(self):
        id_anotacao = int(input("Id da anotacao: "))
        Anotacao.deletar_anotacao(id_anotacao)



        
