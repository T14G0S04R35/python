import os
os.system("cls || clear")

print("Solicitando dados para o usuario.")
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não dode vota")
elif idade < 18:   
    print("Vota opicional.")
elif idade < 65: 
    print("Voto obrigatorio")
else:    
    print("Não odrigatorio")