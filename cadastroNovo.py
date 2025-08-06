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

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")