from data.data import data_hamburguers


def adding_hamburguers():

    name_hamburguer = str(input("Digite o nome do hamburguer que deseja adicionar:"))
    price_hamburguer = int(input("Digite o valor do hamburguer: "))

    try:
        data_hamburguers.append({"name": name_hamburguer, "price": price_hamburguer})
        return {"name": name_hamburguer, "price": price_hamburguer}
    except ValueError:
        print("Valor inválido. Por favor, insira um número para o preço do hambúrguer.")


def list_humburguers():
    try:
        if not data_hamburguers:
            print("Nenhum hambúrguer cadastrado.")
        else:
            print(f"lista de hamburguers cadastrados: ")
            for i, hamburguers in enumerate(data_hamburguers):
                print(
                    f'{i + 1} - {hamburguers["name"]} - Price: R${hamburguers["price"]:.2f}'
                )

    except Exception as e:
        print(f"Ocorreu um erro ao listar os hambúrgueres: {e}")
