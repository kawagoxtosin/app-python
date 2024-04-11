import os

restaurantes = ['ice te pego','la casa de pastel']

def exibir_nome_do_programa():
 print ("""MARTIN BURGER KING
        """)
def exibir_opcoes():
 print("1- cadastrar restaurante")
 print("2- listar restaurante")
 print("3- ativar restaurante")
 print("4- sair")

def finaliza_app():
     exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
     input('\n Digite a tecla "Enter" para voltar ao menu principal')
     main()

def opcao_invalida():
     print('Opção invalida!\n')
     voltar_ao_menu_principal()

def exibir_subtitulo(texto):
 os.system('clear')
 print(texto)
 print()

def ecolher_opcao():
 try:
        opcao_escolhida = int(input("escolha uma opção: "))

        if opcao_escolhida == 1:
                print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
                print('Listar restaurantes')
        elif opcao_escolhida == 3:
                print('ativar restaurantes')
        elif opcao_escolhida == 4:
                finaliza_app()
        else:
                opcao_invalida()

 except:
      opcao_invalida()

def main():
     os.system('clear')
     exibir_nome_do_programa()
     exibir_opcoes()
     ecolher_opcao()

if __name__ == '__main__':
     main()


