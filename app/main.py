import crud.read
import crud.insert
import crud.update
import crud.delete
import utils.clear_terminal


def application():
    option = 0
    while option != 5:
        crud.read.show_menu()
        option = int(input("Digite a opção desejada: "))

        if option == 1:
            utils.clear_terminal.clear_terminal()
            crud.insert.adding_hamburguers()
        elif option == 2:
            utils.clear_terminal.clear_terminal()
            crud.insert.list_hamburgers()

        elif option == 3:
            utils.clear_terminal.clear_terminal()
            crud.update.update_list_hamburguers()
        elif option == 4:
            utils.clear_terminal.clear_terminal()
            crud.delete.delete_hamburguer()
        elif option == 5:
            utils.clear_terminal.clear_terminal()
            print("Saindo do programa...")
        else:
            utils.clear_terminal.clear_terminal()
            print("Opção inválida. Por favor, escolha uma opção válida.")


application()
