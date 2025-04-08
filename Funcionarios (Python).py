import json
import os

ARQUIVO = "funcionarios.json"
SENHA_ADMIN = "admin123"  # senha do modo admin

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(funcionarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)

def menu():
    print("\n=== Sistema de Organização de Funcionários ===")
    print("1. Adicionar funcionário")
    print("2. Listar funcionários")
    print("3. Buscar funcionário por nome")
    print("4. Remover funcionário (Admin)")
    print("5. Relatório de salários")
    print("6. Sair")

def adicionar_funcionario(funcionarios):
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo: ")
    try:
        salario = float(input("Salário: R$ "))
    except ValueError:
        print("Salário inválido. Tente novamente.")
        return
    funcionario = {"nome": nome, "cargo": cargo, "salario": salario}
    funcionarios.append(funcionario)
    salvar_dados(funcionarios)
    print(f"Funcionário {nome} adicionado com sucesso.")

def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    filtro_cargo = input("Deseja filtrar por cargo? (deixe em branco para listar todos): ").strip().lower()
    lista_filtrada = funcionarios
    if filtro_cargo:
        lista_filtrada = [f for f in funcionarios if filtro_cargo in f['cargo'].lower()]
    if not lista_filtrada:
        print("Nenhum funcionário encontrado com este cargo.")
        return
    print("\n--- Lista de Funcionários ---")
    for i, f in enumerate(lista_filtrada, start=1):
        print(f"{i}. Nome: {f['nome']}, Cargo: {f['cargo']}, Salário: R${f['salario']:.2f}")

def buscar_funcionario(funcionarios):
    nome_busca = input("Digite o nome para buscar: ").strip().lower()
    encontrados = [f for f in funcionarios if nome_busca in f['nome'].lower()]
    if encontrados:
        print("\n--- Funcionários Encontrados ---")
        for f in encontrados:
            print(f"Nome: {f['nome']}, Cargo: {f['cargo']}, Salário: R${f['salario']:.2f}")
    else:
        print("Funcionário não encontrado.")

def remover_funcionario(funcionarios):
    senha = input("Digite a senha de admin para remover funcionário: ")
    if senha != SENHA_ADMIN:
        print("Senha incorreta! Acesso negado.")
        return

    nome_remover = input("Digite o nome do funcionário para remover: ").strip().lower()
    for f in funcionarios:
        if f['nome'].lower() == nome_remover:
            confirmacao = input(f"Tem certeza que deseja remover {f['nome']}? (s/n): ").strip().lower()
            if confirmacao == "s":
                funcionarios.remove(f)
                salvar_dados(funcionarios)
                print(f"Funcionário {f['nome']} removido com sucesso.")
            else:
                print("Remoção cancelada.")
            return
    print("Funcionário não encontrado.")

def relatorio_salarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado para gerar relatório.")
        return
    total = sum(f['salario'] for f in funcionarios)
    media = total / len(funcionarios)
    print("\n--- Relatório de Salários ---")
    print(f"Total pago em salários: R${total:.2f}")
    print(f"Média salarial: R${media:.2f}")

# Programa principal
funcionarios = carregar_dados()

while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        adicionar_funcionario(funcionarios)
    elif opcao == "2":
        listar_funcionarios(funcionarios)
    elif opcao == "3":
        buscar_funcionario(funcionarios)
    elif opcao == "4":
        remover_funcionario(funcionarios)
    elif opcao == "5":
        relatorio_salarios(funcionarios)
    elif opcao == "6":
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
