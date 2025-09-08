import os
os.system("cls")


print("""
      
escolha o sexo
       
("f" feminino)\t ("m" masculino)
      
escolha o estado_civil
      
("casado")\t   ("casada")
      
("solteiro")\t  ("solteira")

""")

nome = input("digite seu nome: ")
sexo = input("digite seu sexo: ")
estado_civil = input("digite seu estado civil: ")

if sexo == "f" and estado_civil == "casada":
    input("quantos anos de casada: ")

else:
    ("opcao invalida")


    print(f"nome: {nome}")
    print(f"sexo: {sexo}")
    print(f"estado civil: {estado_civil}")
    


print("fim")

