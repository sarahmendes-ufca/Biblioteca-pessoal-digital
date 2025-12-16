from CLI.livro_cli import LivroCLI
from CLI.revista_cli import RevistaCLI
 
class ObraCLI:
    def mostrar_menu_tipo(self):
        print("____________________________________")
        print("| 1 - Livro                          |")
        print("|____________________________________|")
        print("| 2 - Revista                        |")
        print("|____________________________________|")
        print("| 3 - Voltar                         |")
        print("|____________________________________|")
        opcao = input("Digite o número: ").strip()
        
        if opcao == "1":
            livro = LivroCLI()
            livro.menu_livro()

        elif opcao == "2":
            revista = RevistaCLI()
            revista.menu_revista()

        elif opcao == "3":
            print("Saindo do Menu Obra.")
            return
        
        else:
            print("Opção inválida!")