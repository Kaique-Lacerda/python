
print ("**********************************************************************")
print ("********************Bem vindo ao jogo da forca!!!*********************")
print ("**********************************************************************")
print ("")

Ps = "sucuzinho".upper()

La = ["_","_","_","_","_"]
print(La)

enforcou = False
acertou = False
erros = 0

while(not enforcou and not acertou):
    
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    if(chute in Ps):
        index = 0

        for letra in Ps:
            if(chute.upper() == letra.upper()):
                La[index] = letra
            index = index + 1
    else:
        erros = erros + 1

    enforcou = erros == 6
    acertou = "_" not in La
    print(La)

if(acertou):
    print("GGWP")
else:
    print(erros)
    print(La)
print("Fim de Jogo")