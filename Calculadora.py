print("Bem-Vindo a calculadora 2000.2 do kaique!!")

valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))

continuar = input("digite Y para  continuar: ")

print("Qual o tipo de conta para ser realiza?")

print(" 1. Soma \n 2. Subtração \n 3. Divisão \n 4. multiplicação")
tipoconta = input("1, 2, 3 ou 4: ")

if tipoconta == "1":
    resultadosoma = valor1 + valor2
    print(resultadosoma),

elif tipoconta == "2":
    resultadosubtracao = valor1 - valor2
    print(resultadosubtracao),

elif tipoconta == "3":
    resultadodivisao = valor1 / valor2
    print(resultadodivisao),

elif tipoconta == "4":
    resultadomulti = valor1 * valor2
    print(resultadomulti)