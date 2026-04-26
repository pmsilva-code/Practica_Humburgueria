from data.data import data_hamburguers


def add_hamburger(name_hamburger: str, price_hamburger: float) -> dict:
    """function that take and add name_hamburger and price_hamburger to data_hamburgers list"""
    hamburguer = {"name": name_hamburger, "price": price_hamburger}
    data_hamburguers.append(hamburguer)
    return hamburguer


def adding_hamburguers():
    """Function request data of user and add a hamburger list"""
    name_hamburger = input("Digite o nome do hamburguer que deseja adicionar:")
    try:
        price_hamburger = float(input("Digite o valor do hamburguer: "))
        return add_hamburger(name_hamburger, price_hamburger)
    except ValueError:
        print("Valor inválido. Por favor, insira um número para o preço do hambúrguer.")


def list_hamburgers():
    """Function show all hamburgers in list."""
    if not data_hamburguers:
        print("Nenhum hambúrguer cadastrado.")
        return
    print(f"lista de hamburguers cadastrados: ")
    for i, hamburguers in enumerate(data_hamburguers, start=1):
        print(f'{i} - {hamburguers["name"]} - Price: R${hamburguers["price"]:.2f}')
