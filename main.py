while True:
    print ("**********************************************************************")
    print ("***************************CADASTRE AQUI!!!***************************")
    print ("**********************************************************************")
    print ("")

    nome = str(input("  Digite Seu Nome: "));
    idade = int(input("  Escreva Sua Idade: "));
    ende = str(input("  Digite Seu Endereço: "));
    cpf = int(input("  Digite Seu CPF:  "));
    print ("")

    print(f"Você Confirma Seus Dados? \n Nome: {nome} \n Idade: {idade} \n Endereço: {ende} \n CPF: {cpf} \n")
    Confirmação = str(input("Y/N"))

    if (Confirmação == "Y"):
            print("Cadastro Concluido!"
    elif (Confirmação == "N"):
            print("Tente Novamente...")