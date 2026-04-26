from data.data import data_hamburguers
from crud.insert import list_hamburgers


def remove_hamburger(index: int) -> dict | None:
    """Remove the hamburger by the index, and return the removed item."""
    if index < 0 or index >= len(data_hamburguers):
        return None
    return data_hamburguers.pop(index)


def delete_hamburguer():
    """Requests to user which hamburger should be excluded from the list."""
    try:
        list_hamburgers()
        if not data_hamburguers:
            print("Não há hambúrgueres para excluir.")
            return
        index = int(input("Digite o número do hamburger que deseja excluir: "))
        if index < 1 or index > len(data_hamburguers):
            print("Número inválido. Por favor, escolha um número válido da lista.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    deleted = remove_hamburger(index - 1)
    if deleted is None:
        print("Erro inesperado ao excluir.")
        return
    print(f"Hambúrguer excluído: {deleted['name']} - Preço: R${deleted['price']:.2f}")
    list_hamburgers()
