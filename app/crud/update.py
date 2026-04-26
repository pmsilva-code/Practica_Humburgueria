from data.data import data_hamburguers


def update_list_hamburguers():

    update_hamburger = (
        int(input("Digite o número do hamburguer que deseja atualizar: ")) - 1
    )

    if update_hamburger < 0 or update_hamburger >= len(data_hamburguers):
        print("Número inválido. Por favor, escolha um número válido da lista.")
        return

    new_name_hamburger = str(input("Digite o nome do novo hamburger: "))
    new_price_hamburger = int(input("Digite o novo preço:"))

    data_hamburguers[update_hamburger] = {
        f"name": new_name_hamburger,
        "price": new_price_hamburger,
    }
    print("Hambúrguer atualizado com sucesso!")
    print(
        f'Hambúrguer atualizado: {data_hamburguers[update_hamburger]["name"]} - Price: R${data_hamburguers[update_hamburger]["price"]:.2f}'
    )
