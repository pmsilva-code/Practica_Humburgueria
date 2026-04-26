# Practica_Humburgueria
# Prática Hamburgueria

Projeto em Python que implementa um sistema simples de cadastro de hambúrgueres via terminal.

## O que foi feito

- Criação de um menu interativo para o usuário escolher entre adicionar, listar, atualizar e excluir hambúrgueres.
- Implementação das operações básicas de CRUD:
  - `add`: inserir um novo hambúrguer com nome e preço.
  - `list`: exibir a lista de hambúrgueres cadastrados.
  - `update`: alterar o nome e/ou preço de um hambúrguer existente.
  - `delete`: remover um hambúrguer pelo número da lista.
- Uso de terminal limpo antes de cada ação para deixar a interface menos poluída e mais fácil de usar.
- Gestão dos dados em memória usando uma lista Python simples.

## Arquitetura do projeto

- `app/main.py`
  - Ponto de entrada da aplicação.
  - Loop principal que mostra o menu, lê a opção do usuário e chama as funções correspondentes.
  - Chama `utils.clear_terminal.clear_terminal()` para limpar a tela antes de cada ação.

- `app/crud/read.py`
  - Contém a função `show_menu()` responsável por exibir as opções disponíveis.

- `app/crud/insert.py`
  - Função `adding_hamburguers()` para adicionar um novo hambúrguer.
  - Função `list_humburguers()` para exibir todos os hambúrgueres cadastrados.
  - Importa `data_hamburguers` de `app/data/data.py`.

- `app/crud/update.py`
  - Função `update_list_hamburguers()` para atualizar um hambúrguer existente com base no índice.
  - Valida se o número informado está dentro do intervalo válido.

- `app/crud/delete.py`
  - Função `delete_hamburguers()` para excluir um hambúrguer.
  - Exibe a lista atualizada após a exclusão.

- `app/data/data.py`
  - Armazena a lista `data_hamburguers` usada por todo o sistema.

- `app/utils/clear_terminal.py`
  - Função `clear_terminal()` que limpa a tela de terminal de forma compatível com Windows (`cls`) e Linux/Mac (`clear`).

## Linguagem e bibliotecas utilizadas

- Linguagem principal: Python 3
- Não usa bibliotecas externas além da biblioteca padrão do Python.
- Usa o módulo `os` em `app/utils/clear_terminal.py` para executar o comando de limpar terminal.

## Funções e módulos principais

- `application()` em `app/main.py`: loop principal do aplicativo que mostra o menu e chama operações CRUD.
- `show_menu()` em `app/crud/read.py`: exibe o menu de opções para o usuário.
- `adding_hamburguers()` em `app/crud/insert.py`: adiciona um novo hambúrguer à lista.
- `list_humburguers()` em `app/crud/insert.py`: lista os hambúrgueres cadastrados.
- `update_list_hamburguers()` em `app/crud/update.py`: atualiza hambúrguer existente pelo índice.
- `delete_hamburguers()` em `app/crud/delete.py`: remove um hambúrguer pelo índice.
- `data_hamburguers` em `app/data/data.py`: armazenamento em memória dos hambúrgueres.

## Como usar

1. Execute `python app/main.py` ou `python main.py` a partir do diretório principal do projeto.
2. Escolha uma opção do menu digitando o número desejado.
3. Siga as instruções na tela para cadastrar, listar, atualizar ou excluir hambúrgueres.

## Observações

- Os dados são mantidos apenas em memória enquanto o programa estiver em execução.
- Se quiser, posso ajudar a estender o projeto para salvar os dados em arquivo ou banco de dados.
