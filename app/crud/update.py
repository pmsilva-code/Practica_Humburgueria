from data.data import data_hamburguers


def update_hamburger(index: int, new_name: str, new_price: float) -> dict | None:
    """Update the index and return the updated item."""
    if index < 0 or index >= len(data_hamburguers):
        return None
    data_hamburguers[index] = {"name": new_name, "price": new_price}
    return data_hamburguers[index]


def update_hamburger_interactive():
    """ "Requests the user which hamburger to update and applies the changes."""

    try:
        index = int(input("Digite o número do hambúrguer que deseja atualizar: ")) - 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    if index < 0 or index >= len(data_hamburguers):
        print(f"Número inválido. Escolha um número entre 1 e {len(data_hamburguers)}.")
        return

    new_name = input("Digite o nome do novo hambúrguer: ")
    try:
        new_price = float(input("Digite o novo preço: "))
    except ValueError:
        print("Preço inválido. Digite um número válido.")
        return

    updated = update_hamburger(index, new_name, new_price)
    if updated:
        print("Hambúrguer atualizado com sucesso!")
        print(f'Hambúrguer atualizado: {updated["name"]} - Preço: R${updated["price"]:.2f}')
