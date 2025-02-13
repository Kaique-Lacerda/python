print ("*******************")
print ("Bem Vindo ao jogo!!")
print ("*******************")

numero_secreto = 89
total_tentativas = 10
rodada =  1

while (rodada <= total_tentativas):
print(f"tentativa {rodada} de {total_tentativas}")

chute_str = input ("digite seu número:")
print ("você digitou o numero:", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    ("NICE FILHOTE")
else:
    if (maior):
        ("É MAIOR")
    elif(menor):
        ("É MENOR") 
    rodada = rodada + 1
    print("fim de jogo")