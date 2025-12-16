from models.configuracao import Configuracao
import sqlite3

class ConfiguracaoCLI:
    def menu_configuracoes(self):
        print(" ____________________________________")
        print("| 1 - Editar configuracoes           |")
        print("|____________________________________|")
        print("| 2 - Sair                           |")
        print("|____________________________________|")
        print("| 3 - Bib Mostrar obras cadastradas  |")
        print("|____________________________________|")
        opcao_acoes_configuracao = input("Escolha uma opção: ").strip()

        if opcao_acoes_configuracao == "1":
            self.editar_json_cli()

        elif opcao_acoes_configuracao == "2":
            print("Saindo do menu Configurações")
            return
        
        elif opcao_acoes_configuracao == "3":
            conn = sqlite3.connect('biblioteca.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM obra")
            registros = cursor.fetchall()
            print(f"Registros na tabela 'obra':")
            for registro in registros:
                print(registro)
            conn.close()
        else:
            print("Opção inválida! ")

    def editar_json_cli(self):
        genero_favorito = None
        meta_anual_leitura = None
        numero_leitura_simultanea = None
        resp = input("Deseja editar o genero favorito? (sim ou nao)").strip()
        if resp == "sim" or resp == "s":
            genero_favorito = input("Gênero favorito: ")
        elif resp == "nao" or resp == "n":
            genero_favorito = None
        else:
            ("Resposta inválida!")
            return
        res = input("Deseja editar a meta anual de leitura? (sim ou nao)").strip()
        if res == "sim" or res == "s":
            meta_anual_leitura = input("Meta anual de Leitura: ")
        elif res == "nao" or res == "n":
            meta_anual_leitura = None
        else:
            ("Resposta inválida!")
            return
        resposta = input("Deseja editar o limite de leituras simultaneas? (sim ou nao)").strip()
        if resposta == "sim" or resposta == "s":
            numero_leitura_simultanea = input("Limite de Leituras Simultaneas: ")
        elif resposta == "nao" or resposta == "n":
            numero_leitura_simultanea = None
        else:
            ("Resposta inválida!")
            return
        config = Configuracao()
        config.atualizar(genero_favorito, meta_anual_leitura, numero_leitura_simultanea)


        
