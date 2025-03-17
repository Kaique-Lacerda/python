clientes = []

while True:
    print("\n ==Menu==")
    print("1. Cadastrar novo cliente")
    print("2. Listar clientes cadastrados")
    print("3. Sair")

    opcao = input ("\n Escolha uma opção: ")

    if opcao == '1':
        print("\n --- novo cadastro ---")
        nome = input("Nome completo: ")
        telefone = input("Telefone:")

        cliente = {
            'nome' : nome,
            'telefone' : telefone
        }

        clientes.append(cliente)
        print("\n Cliente cadastracodo com sucesso")

    elif opcao == '2':
        print("\n--- clientes cadastrados ---")
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"\n Cliente{i}:")
                print(f"Nome: {cliente['nome']}")
                print(f"Telefone:{cliente['telefone']}")
    elif opcao == '3':
        print("\n")