import json

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def cadastrar_usuario(usuarios):
    nome = input("Nome: ")
    email = input("Email: ")

    usuario = {
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    print("Usuario salvo com sucesso!\n")

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuario cadastrado. \n")
        return
    
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nome']} - {u['email']}")
    print()

def menu():
    usuarios = carregar_usuarios()

    while True:
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção invalida\n")

menu()