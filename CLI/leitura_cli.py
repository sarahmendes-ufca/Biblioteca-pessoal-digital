from models.leitura import Leitura
import sqlite3

class LeituraCLI:
    def menu_leitura(self):
        print(" ____________________________________")
        print("| 1 - Iniciar Leitura                |")
        print("|____________________________________|")
        print("| 2 - Finalizar Leitura              |")
        print("|____________________________________|")
        print("| 3 - Deixar avaliação               |")
        print("|____________________________________|")
        print("| 4 - Verificar Meta Anual           |")
        print("|____________________________________|")
        print("| 5 - Sair                           |")
        print("|____________________________________|")
        print("| 6 - Bib Mostrar obras cadastradas  |")
        print("|____________________________________|")
        opcao_acoes_leitura = input("Escolha uma opção: ")

        if opcao_acoes_leitura == "1":
            self.iniciar_leitura_cli()
        elif opcao_acoes_leitura == "2":
            self.concluir_leitura_cli()
        elif opcao_acoes_leitura == "3":
            self.deixar_avaliacao()
        elif opcao_acoes_leitura == "4":
            self.verificar_meta_cli()
        elif opcao_acoes_leitura == "5":
            print("saindo")
            return
        elif opcao_acoes_leitura == "6":
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

    def iniciar_leitura_cli(self):
        id_obra = int(input("Digite o ID da obra: "))
        lei = Leitura(id_obra)
        lei.iniciar_leitura()

    def concluir_leitura_cli(self):
        id_obra = int(input("Digite o ID da obra: "))
        lei = Leitura(id_obra)
        lei.concluir_leitura()

    def verificar_meta_cli(self):
        id_obra = int(input("Digite o ID da obra para checar a meta anual (ou 0 para todas): "))
        leitura = Leitura(id_obra)
        leitura.verificar_meta_anual()


    def deixar_avaliacao(self):
        id_obra = int(input("Digite o ID da obra: "))
        avaliacao = float(input("Avaliação: "))
        av = Leitura(id_obra, avaliacao)
        av.validar_avaliacao(avaliacao)
)



