import sys
import os
from time import sleep
from colorama import init, Fore
import pyfiglet
# Iniciando colorama
init(autoreset=True)
# Função para limpar o console


def clear_console():
    os.system("cls")


# Função para criar uma linha
def linha(cor):
    """
    Espera: O nome da cor a ser mostrada\n
    Modifica: A cor do texto\n
    Retorna: Linha colorida
    :param cor:
    :return:
    """
    if cor == "vermelho":
        print(f"{Fore.RED}Xx------------------------------------------------xX")
    elif cor == "amarelo":
        print(f"{Fore.YELLOW}Xx------------------------------------------------xX")
    elif cor == "azul":
        print(f"{Fore.BLUE}Xx------------------------------------------------xX")
    elif cor == "preto":
        print(f"{Fore.BLACK}Xx------------------------------------------------xX")
    elif cor == "verde":
        print(f"{Fore.GREEN}Xx------------------------------------------------xX")
    elif cor == "magenta":
        print(f"{Fore.MAGENTA}Xx------------------------------------------------xX")
    elif cor == "ciano":
        print(f"{Fore.CYAN}Xx------------------------------------------------xX")
    elif cor == "azulvermelho":
        print(
            f"{Fore.BLUE}Xx------------------------{Fore.RED}------------------------xX"
        )
    else:
        print(f"{Fore.WHITE}Xx------------------------------------------------xX")


# Função para digitação de texto mais elegante
def efeito_escrita(text, delay):
    """
    Espera: O texto a ser exibido e o tempo que cada letra será exibida\n
    Modifica: A saída de texto no terminal\n
    Retorna: O texto aparecendo letra por letra no terminal.
    :param text:
    :param delay:
    :return:
    """
    for char in text:
        print(f"{char}", end="")
        sys.stdout.flush()
        sleep(delay)


# Função para o letreiro do jogo
RPYG = pyfiglet.figlet_format("RPYG GAME").strip()


def letreiro_jogo():
    linha("azul")
    print(f"{Fore.GREEN} {RPYG}\n")
    linha("vermelho")
