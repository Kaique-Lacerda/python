usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o email do usuário: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("Lista de usuários:")
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}")
print()

def remover_usuario():
    listar_usuarios()
    if not usuarios:
        return

    try:
        indice = int(input("Digite o número do usuário a ser removido: ")) - 1
        if 0 <= indice < len(usuarios):
            removido = usuarios.pop(indice)
            print("Usuário removido com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Remover usuário")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            remover_usuario()
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()