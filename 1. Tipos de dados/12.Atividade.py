import os
os.system("cls || clear")

numero = int(input("Digite o numero: "))
pares = int(input("Numeros pares:"))
impares = int(input("numeros impares: "))

for i in range(1,6):
numero = int(input(f"Digite o {i+1}º numero: "))
if numero %2 == 0:
    pares+1
else:
    impares=1