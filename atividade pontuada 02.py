import os
os.system("cls")




print("""

codigo   \t  atividade        \\t   valor        
1           natacao             10,00
2           futebol             12,00
3           basquete            13,00
4           volei               14,00

""")
codigo = int(input("digite o codigo desejada: "))

match codigo:
    case a:
        atividade = natacao
        valor = 10,00
    case b:
        atividade = futebol
        valor = 12,00
    case c:
        atividade = basquete
        valor = 13,00
    case d:
        atividade = volei
        valor = 14,00
    case _:
        print("opcao invalida")

print(f"atividade: {atividade}")
print(f"valor: {valor}")
print(f"codigo: {codigo}")
    
    
