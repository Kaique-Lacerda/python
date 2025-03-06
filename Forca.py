
print ("**********************************************************************")
print ("********************Bem vindo ao jogo da forca!!!*********************")
print ("**********************************************************************")
print ("")

Ps = "sucuzinho"

enforcou = False
acertou = False

while(not enforcou and not acertou):
    
    chute = input("Qual a letra? ")
    chute = chute.strip()

    index = 0

    for letra in Ps:
        if(chute.upper() == letra.upper()):
            print(f"Encontrei a letra {letra} na posição {index}")
        index = index + 1
    print("Jogando...")
print("Fim de Jogo")