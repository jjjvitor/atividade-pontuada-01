import os
os.system("cls")

print("""
Fruta\t	Até 5 Kg\t	Acima de 5 Kg
Morango\t	R$ 2,50 por Kg\t	R$ 2,20 por Kg
Maçã\t	R$ 1,80 por Kg\t	R$ 1,50 por Kg
""")
morango = input("o quanto deseja de morango: ")
maca = input("o quanto desaeja de maca: ")


soma = maca + morango
resultado = 0


match resultado:
    
    case resultado:
        if resultado <= "10,kg" or resultado <= 15.00:
            print(f"resultado: {soma}")
            print(f"total a pagar: {soma}")
    
        elif  resultado  > "10,kg" or resultado > 15.00:
            # Obtendo o valor do desconto de 10%.
            desconto = maca or morango * 0.10
            valor_com_desconto = maca or morango - desconto
            print(f"total a pagar: {soma}")
        else:
            print("opcao invalida")

print("fim")