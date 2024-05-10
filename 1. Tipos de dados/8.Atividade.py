import os
os.system("cls || clear")


resultado = 0

a = int(input("Digite o prineiro numero: "))
opcao = input("Digite a opção desejada: ")
b = int(input("Digite o segundo numero: "))

match(opcao):
      case 1:
         "+":
         resultado = a + b
      case 2:
         "-":
         resultado = a - b
      case 3:
         "*":
         resultado = a * b
      case 4:
         "/":
         resultado = a / b
      case _:  
        print("opção inválida.")

print(f"Resultado: {resultado}.")  

