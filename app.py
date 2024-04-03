import os

print ("""MARTIN BURGER KING
        """)

print("1- cadastrar restaurante")
print("2- listar restaurante")
print("3- ativar restaurante")
print("4- sair")


opcao_escolhida = int(input("escolha uma opção: "))
#print("você escolheu a opção", opcao_escolhida)
#print(f"você escolheu a opção {opcao_escolhida}")

def finaliza_app():
        os.system('cls')
        print('Encerrando o programa\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
        print('Listar restaurantes')
elif opcao_escolhida == 3:
       print('ativar restaurantes')
else:
        finaliza_app()