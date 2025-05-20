import json
import os

ARQUIVO_CONTAS = "contas.json"

if os.path.exists(ARQUIVO_CONTAS):
    with open(ARQUIVO_CONTAS, "r") as f:
        Contas_no_sistema = json.load(f)
else:
    Contas_no_sistema = [{"usuario": "Adm", "senha": "Admin123"}]

def salvar_contas():
    with open(ARQUIVO_CONTAS, "w") as f:
        json.dump(Contas_no_sistema, f, indent=4)

def validar_senha(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    return tem_maiuscula and tem_numero

def fazer_login():
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")

    for conta in Contas_no_sistema:
        if conta["usuario"] == nome:
            if senha == conta["senha"]:
                print(f"Login bem-sucedido! Bem-vindo, {nome}.")
                return
            else:
                print("Senha incorreta.")
                return
    print("Usuário não encontrado.")

while True:
    print("\nMenu:")
    print("1. Criar nova conta")
    print("2. Mostrar contas existentes")
    print("3. Fazer login")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome_nova = input("Nome de Usuário: ")

        if any(conta["usuario"] == nome_nova for conta in Contas_no_sistema):
            print("Este nome de usuário já existe. Tente outro.")
            continue

        while True:
            senha_nova = input("Senha (precisa conter ao menos uma letra maiúscula e um número): ")
            if validar_senha(senha_nova):
                break
            else:
                print("Senha inválida! Tente novamente.")

        nova_conta = {"usuario": nome_nova, "senha": senha_nova}
        Contas_no_sistema.append(nova_conta)
        salvar_contas()
        print("Conta criada com sucesso!")

    elif opcao == "2":
        print("\nContas:")
        for i, conta in enumerate(Contas_no_sistema):
            print(f"{i}. Usuário: {conta['usuario']}")

    elif opcao == "4":
        print("Até mais!")
        break

    elif opcao == "3":
        fazer_login()

    else:
        print("Opção inválida. Tente novamente.")
