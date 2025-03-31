import math

numero = int(input("Digite um número: "))

if math.fmod(numero, 2) == 0:
    print(f"{numero} é impar")
else:
    print(f"{numero} é par")