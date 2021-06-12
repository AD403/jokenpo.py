import random
import time
import os
import colorama
from colorama import Fore

colorama.init(convert=True)


def iniciar():
    print(Fore.BLUE + "="*33, Fore.BLUE +
          "\nSEJA BEM VINDO AO JOGO DE JOKENPÔ")
    print(Fore.BLUE + "="*33)


def mecanica(escolha_user, escolha_bot, nome):
    if(escolha_user == escolha_bot):
        time.sleep(1)
        print(Fore.YELLOW +
              f"EMPATOU {nome} escolheu {escolha_user} e o Bot também\033[m")

    elif((escolha_user == 'pedra' and escolha_bot == 'tesoura') or (escolha_user == 'tesoura' and escolha_bot == 'papel') or (escolha_user == 'papel' and escolha_bot == 'pedra')):
        time.sleep(1)
        print(Fore.GREEN +
              f"PARABÉNS, VOCÊ GANHOU! {nome} escolheu {escolha_user} e o Bot escolheu {escolha_bot}\033[m")

    elif((escolha_user == 'tesoura' and escolha_bot == 'pedra') or (escolha_user == 'papel' and escolha_bot == 'tesoura') or (escolha_user == 'pedra' and escolha_bot == 'papel')):
        time.sleep(1)
        print(Fore.RED +
              f"VOCÊ PERDEU :( {nome} escolheu {escolha_user} e o Bot escolheu {escolha_bot}\033[m")


def main():
    iniciar()

    time.sleep(2)
    nome = input("Digite seu nome: ")
    print()

    time.sleep(1)
    print(Fore.MAGENTA + f"CASO QUEIRA SAIR APERTE ENTER\033[m")
    print()

    while(True):
        time.sleep(1)
        escolha_user = input(
            f'{nome} escolha uma das opções - pedra/papel/tesoura: ')
        print()
        escolha_bot = random.choice(['pedra', 'papel', 'tesoura'])

        if(escolha_user == ""):
            print(Fore.CYAN + "FIM DO JOGO")
            break

        elif(escolha_user != 'pedra' and escolha_user != 'papel' and escolha_user != 'tesoura'):
            time.sleep(1)
            print(
                Fore.RED + f"Escolha inválida, por favor digite outra opção\n\033[m")
            continue

        else:
            escolha_user = escolha_user.strip().lower()
            mecanica(escolha_user, escolha_bot, nome)
            time.sleep(5)
            os.system('cls')


main()
