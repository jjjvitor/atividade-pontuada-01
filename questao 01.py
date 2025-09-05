import os
os.system("cls")

valor_a = float(input("digite o primeiro valor: "))
valor_b = float(input("digite o segundo valor: "))
valor_c = float(input("digite o terceiro valor: "))

soma = (valor_a + valor_b)

print(f"soma: {soma}")


if soma  <= valor_c:
    print("e menor que c")
elif soma > valor_c:
    print("e maior que c ")
else:
    print("resultado invalido")
    
         



    


