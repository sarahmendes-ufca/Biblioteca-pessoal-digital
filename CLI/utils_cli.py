from CLI.obra_cli import ObraCLI
from CLI.relatorio_cli import RelatorioCLI
from CLI.anotacao_cli import AnotacaoCLI
from CLI.colecao_cli import ColecaoCLI
from CLI.leitura_cli import LeituraCLI
from CLI.configuracao_cli import ConfiguracaoCLI
# Antes de executar o código, instale os requirements.txt
class UtilsCLI:
    def escolher_acao(self):
        print(" _________ Biblioteca Pessoal _______")
        print("| 1 - Gerenciar Obras                |")
        print("|____________________________________|")
        print("| 2 - Acessar configurações          |")
        print("|____________________________________|")
        print("| 3 - Gerenciar Anotações            |")
        print("|____________________________________|")
        print("| 4 - Gerenciar Leitura              |")
        print("|____________________________________|")
        print("| 5 - Gerenciar Coleção              |")
        print("|____________________________________|")
        print("| 6 - Gerar Relatório                |")
        print("|____________________________________|")
        print("| 7 - Sair                           |")
        print("|____________________________________|")
        opcao = input("Digite o número: ").strip()
        
        if opcao == "1":
            obra = ObraCLI()
            obra.mostrar_menu_tipo()

        elif opcao == "2":
            configuracao = ConfiguracaoCLI()
            configuracao.menu_configuracoes()

        elif opcao == "3":
            ano = AnotacaoCLI()
            ano.menu_anotacao()

        elif opcao == "4":
            leitura = LeituraCLI()
            leitura.menu_leitura()

        elif opcao == "5":
            colecao = ColecaoCLI()
            colecao.menu_colecao()

        elif opcao == "6":
            rel = RelatorioCLI()
            rel.mostrar_relatorios()

        elif opcao == "7":
            print("Saindo da Biblioteca")
            return
        
        else:

            print("Opção inválida!")

