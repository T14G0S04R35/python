import os
os.system("cls || clear")

soma = 0
              #(5)
for i in range(1,6):            #{i+1}  
    numero = int(input(f"Digite o {i}º numero: "))
    soma += numero

    print(f"Soma: {soma}")