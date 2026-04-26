from data.data import data_hamburguers
from crud.insert import list_hamburgers


def delete_hamburguers():
    delete_hamburger = (
        int(input("Digite o número do hamburguer que deseja excluir: ")) - 1
    )

    if delete_hamburger < 0 or delete_hamburger >= len(data_hamburguers):
        print("Número inválido. Por favor, escolha um número válido da lista.")
        return

    deleted_hamburger = data_hamburguers.pop(delete_hamburger)
    print(
        f"Hambúrguer excluído: {deleted_hamburger['name']} - Price: R${deleted_hamburger['price']:.2f}"
    )

    list_hamburgers()
