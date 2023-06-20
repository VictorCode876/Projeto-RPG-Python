"""Este projeto serve para se aprofundar mais no conhecimento Python, testando ao máximo o conhecimento que eu ja tenho
adquirido no mesmo"""
import sys
import os
import pickle
from random import randint, choice, random
from time import sleep
import pygame.mixer
from pygame import mixer
from colorama import init, Fore
import pyfiglet
from FunçõesDoJogo import clear_console, linha, efeito_escrita, letreiro_jogo
from ListasImportantes import Efeitos_Armas, ArmasComuns, ArmasLendarias, Inimigos_Floresta, Inimigos_Montanha
from ListasImportantes import Inimigos_Cemiterio, Bosses
# Iniciando Colorama e o Pygame
mixer.init()
init(autoreset=True)
# Variáveis Globais
SfxCura = pygame.mixer.Sound("Músicas e Efeitos\\Efeitos\\Healing.wav")
mixer.music.set_volume(0.5)
# Variáveis lógicas que vão dizer se o Boss está vivo ou morto.
Dullahan = True
Dragao = True
Chimera = True
Dracula = True
Boitata = True
Golem = True
# Informações do Personagem
NomePersonagem = ""
VidaMaxima = 100
VidaPersonagem = VidaMaxima
Classe = 0
Dinheiro = 0
Pocao = 0
ClasseNome = ""
ArmaEquipada = ""
AtaquePersonagem = 0
AtaqueArma = 0
ExperienciaPersonagem = 0
ExperienciaNecessario = 25
Nivel = 1
PontosAtributos = 0
PontosGastos = 0
PONTO_ATRIBUTO_POR_NIVEL = 5
Vitalidade = 0
Defesa = 0
Forca = 0
Destreza = 0
Inteligencia = 0
x = 0
y = 0
TurnosEfeitosPersonagem = 0
AtordoamentoPersonagem = False
Batalha = False
Durante_Local = True
Loja = False
Conversar = False
# Informações dos Inimigos
VidaInimigo = 0
TurnosEfeitosInimigo = 0
AtordoamentoInimigo = False


# Criando Funções
def carregando_musicas(nome, pausar):
    if nome == "Title Theme" and pausar is False:
        mixer.music.load("Músicas e Efeitos\\Músicas\\xDeviruchi - Title Theme.wav")
        mixer.music.play(loops=-1)
    elif nome == "The Adventure Begins" and pausar is False:
        mixer.music.load("Músicas e Efeitos\\Músicas\\xDeviruchi - And The Journey Begins.wav")
        mixer.music.play(loops=-1)
    elif nome == "Take Some Rest" and pausar is False:
        mixer.music.load("Músicas e Efeitos\\Músicas\\xDeviruchi - Take some rest and eat some food!.wav")
        mixer.music.play(loops=-1)
    elif nome == "Battle Begins" and pausar is False:
        MusicasBatalha = ["Músicas e Efeitos\\Músicas\\xDeviruchi - Prepare for Battle!.wav",
                          "Músicas e Efeitos\\Músicas\\Prepare for Battle 2!.mp3",
                          "Músicas e Efeitos\\Músicas\\xDeviruchi - Minigame.wav"]
        mixer.music.load(choice(MusicasBatalha))
        mixer.music.play(loops=-1)
    elif nome == "Decisive Battle" and pausar is False:
        MusicasBosses = ["Músicas e Efeitos\\Músicas\\xDeviruchi - Decisive Battle.wav",
                         "Músicas e Efeitos\\Músicas\\Decisive Battle 2!.mp3",
                         "Músicas e Efeitos\\Músicas\\Decisive Battle 3!.mp3"]
        mixer.music.load(choice(MusicasBosses))
        mixer.music.play(loops=-1)
    elif nome == "Danger!" and pausar is False:
        mixer.music.load("Músicas e Efeitos\\Músicas\\Danger!.mp3")
        mixer.music.play(loops=-1)
    else:
        mixer.music.pause()
    mixer.music.set_volume(0.45)


# Mecânica de efeitos para o jogador
def mecanica_de_efeitos(vida_inimigo, atordoamento_inimigo, defesa_inimigo, ataque_personagem, vida_personagem, turnos):
    """
    Espera: A vida do inimigo, variável lógica de atordoamento, a defesa do inimigo, o ataque do personagem,
    a vida do personagem e a variável de turnos\n
    Modifica: As informações do inimigo durante o combate\n
    Resultado: Status negativos nos inimigos
    :param vida_inimigo:
    :type atordoamento_inimigo: bool
    :param atordoamento_inimigo:
    :param defesa_inimigo:
    :param ataque_personagem:
    :param vida_personagem:
    :param turnos:
    :return:
    """
    global ArmaEquipada, VidaMaxima
    Armas = ArmaEquipada
    # Procurando a arma na lista de Efeitos_Armas
    if Armas in Efeitos_Armas:
        # Randomizando a chance do efeito acertar o inimigo
        if random() < Efeitos_Armas[Armas]['Chance'] or turnos > 0:
            # Fazendo com que a mensagem apareça só quando o turno de efeito for igual a 0
            if turnos == 0 and Armas != "Sanguessuga":
                linha("azul")
                print(Efeitos_Armas[Armas]['Mensagem'])
            # Criando uma cadeia de condições com o nome das armas e seus devidos efeitos
            if Armas in ("Espada Venenosa", "Cajado Venenoso", "Arco Venenoso"):
                vida_inimigo -= 3
                linha("verde")
                print(f"{Fore.GREEN}O inimigo está envenenado. -3 de vida")
                if turnos == 0:
                    turnos += 3
            elif Armas in ("Clava Grande", "Espada de Osso", "Cajado da Terra", "Cajado de Osso", "Arco Bruto",
                           "Arco de Ossos", "Clava", "Arco de Batalha", "Martelo Colossal", "Orbe da Terra",
                           "Arco da Terra Sagrada"):
                atordoamento_inimigo = True
            elif Armas in ("Devoradora de Almas", "Cajado dos Espectros", "Arco Devoradora de Almas",
                           "Cetro dos Pesadelos"):
                ataque_personagem = vida_inimigo
            elif Armas in ("Sanguessuga", "Cajado Carmesim", "Arco Vampiríco", "Espada Sombria", "Livro das Sombras",
                           "Arco do Vampiro Sanguinolento"):
                if vida_personagem < VidaMaxima:
                    vida_personagem += ataque_personagem
                    linha("azul")
                    print("\t\t" + Efeitos_Armas[Armas]['Mensagem'])
            elif Armas == "Cajado do Xamã":
                vida_inimigo -= 15
                linha("verde")
                print(f"{Fore.GREEN}O inimigo está pegando fogo. -15 de vida")
                if turnos == 0:
                    turnos += 4
            elif Armas in ("Lâmina do Dragão", "Machado Grande Flamejante", "Ira Dracônica",
                           "Arco do Inferno Dracônico", "Arco da Chama Lunar"):
                vida_inimigo -= 40
                linha("verde")
                print(f"{Fore.GREEN}O inimigo está queimando. -40 de vida")
                if turnos == 0:
                    turnos += 5
            elif Armas == "Foice do Crepúsculo":
                vida_inimigo -= 25
                linha("verde")
                print(f"{Fore.GREEN}O inimigo está queimando -25 de vida")
                ataque_personagem += defesa_inimigo / 2
            elif Armas == "Lança da Decapitação" or Armas == "Arco do Espectro Negro":
                ataque_personagem += defesa_inimigo
            elif Armas in ("Garras da Besta", "Cajado do Caos", "Arco Fúria da Chimera"):
                linha("verde")
                if random() < 0.3:
                    vida_inimigo -= 15
                    if turnos == 0:
                        print("O inimigo foi envenenado!. - 15 de vida")
                        turnos += 4
                    else:
                        print("O inimigo está envenenado!. - 15 de vida")
                if random() < 0.3:
                    vida_inimigo -= 15
                    if turnos == 0:
                        print("O inimigo está queimando!. - 15 de vida")
                        turnos += 4
                    else:
                        print("O inimigo está queimando!. - 15 de vida")
                if random() < 0.3 and turnos == 0:
                    atordoamento_inimigo = True
                    print("O inimigo foi paralisado!")
    return vida_inimigo, atordoamento_inimigo, defesa_inimigo, ataque_personagem, vida_personagem, turnos
# Mecânica de efeitos para inimigos
def mecanica_de_efeitos_inimigos(nome_inimigo, vida_inimigo, ataque_inimigo, atordoamento_personagem, vida_personagem,
                                 defesa_personagem, turnos):
    """
    Espera: O nome do inimigo, a vida do inimigo, o ataque do inimigo, a variável booleana de atordoamento do personagem
    a vida do personagem, a defesa do personagem e a variável de turnos que o efeito irá durar no personagem\n
    Modifica: As informações do personagem durante o combate\n
    Resultado: Status negativo no personagem
    :param nome_inimigo:
    :param vida_inimigo:
    :param ataque_inimigo:
    :param atordoamento_personagem:
    :param vida_personagem:
    :param defesa_personagem:
    :param turnos:
    :return:
    """
    # Cria uma lista com todos os inimigos
    todos_inimigos = Inimigos_Montanha + Inimigos_Floresta + Inimigos_Cemiterio + Bosses

    # Verifica se o inimigo passado como argumento está na lista de inimigos
    for inimigo in todos_inimigos:
        if nome_inimigo == inimigo["Nome"]:

            # Verifica se o inimigo vai causar efeito ou não
            chance_efetiva = inimigo['Chance'] + (turnos * 0.03)  # aumenta a chance a cada turno que passa
            if random() < chance_efetiva:

                # Executa o efeito correspondente ao inimigo
                if inimigo['Efeito'] == "Atordoamento":
                    atordoamento_personagem = True

                elif inimigo['Efeito'] == "Veneno":
                    dano = 3 + (turnos * 0.5)  # aumenta o dano a cada turno que passa
                    vida_personagem -= dano
                    if turnos == 0:
                        linha("verde")
                        print(f"{Fore.GREEN}Você foi envenenado! -{dano} de vida.")
                        linha("verde")
                    else:
                        linha("verde")
                        print(f"{Fore.GREEN}Você ainda está envenenado! -{dano} de vida.")
                        linha("verde")
                    turnos += 3

                elif inimigo['Efeito'] == "Sangramento":
                    dano = 5 + (turnos * 0.75)  # aumenta o dano a cada turno que passa
                    vida_personagem -= dano
                    if turnos == 0:
                        linha("verde")
                        print(f"{Fore.GREEN}Você sofreu sangramento! -{dano} de vida.")
                        linha("verde")
                    else:
                        linha("verde")
                        print(f"{Fore.GREEN}Você ainda está sangrando! -{dano} de vida.")
                        linha("verde")
                    turnos += 2

                elif inimigo['Efeito'] == "Roubo de Vida":
                    if ataque_inimigo > 0:
                        dano = ataque_inimigo
                        vida_inimigo += dano
                        linha("verde")
                        print(f"Ele roubou sua vida! +{dano} de vida para o inimigo.")
                        linha("verde")

                elif inimigo['Efeito'] == "Roubo de Alma":
                    dano = vida_personagem  # o dano é igual à vida máxima do personagem
                    vida_personagem = 0
                    linha("magenta")
                    print("Sua alma foi arrancada de seu corpo.")
                    linha("magenta")
                    ataque_inimigo = dano

                elif inimigo['Efeito'] == "Queimadura":
                    dano = 20 + (turnos * 1)  # aumenta o dano a cada turno que passa
                    vida_personagem -= dano
                    if turnos == 0:
                        linha("verde")
                        print(f"{Fore.GREEN}Você está queimando!. -{dano} de vida.")
                        linha("verde")
                        turnos += 3
                    else:
                        linha("verde")
                        print(f"{Fore.GREEN}Você ainda está queimando!. -{dano} de vida.")
                        linha("verde")
                elif inimigo['Efeito'] == "TriEfeitos":
                    dano = 25 + (turnos * 1)  # aumenta o dano a cada turno que passa
                    vida_personagem -= dano
                    if turnos == 0:
                        atordoamento_personagem = True
                        linha("verde")
                        print(f"{Fore.GREEN}Você foi envenenado e esta queimando! -{dano} de vida.")
                        print(f"{Fore.YELLOW}Você está atordoado!.")
                        linha("verde")
                        turnos += 3
                    else:
                        linha("verde")
                        print(f"{Fore.GREEN}Você ainda está envenenado e queimando! -{dano} de vida.")
                        linha("verde")

            elif inimigo['Efeito'] == "Ignorar Defesa":
                ataque_inimigo += defesa_personagem
                linha("verde")
                print("Ele perfurou sua defesa!.")
                linha("verde")
    return nome_inimigo, vida_inimigo, ataque_inimigo, atordoamento_personagem, vida_personagem, defesa_personagem, \
        turnos

# Armas Lendárias e Armas 'Comuns' para cada classe
def mudar_arma_classe():
    """
    Espera: O jogador definir sua classe\n
    Modifica: O 'Loot' que está dentro da lista dos inimigos\n
    Retorna: As armas que os inimigos vão dropar
    :return:
    """
    global ArmaEquipada, AtaquePersonagem
    Todos_Inimigos = Inimigos_Montanha + Inimigos_Floresta + Inimigos_Cemiterio
    for ArmaInimigo in Todos_Inimigos:
        if Classe == 1:
            ArmaEquipada = ArmasComuns[0]["Nome"]
            AtaquePersonagem = ArmasComuns[0]["Ataque"]
            AtaquePersonagem += Forca // 3
            Arma_Guerreiro = {
                "Lobo": "Espada do Lobo Curva",
                "Aranha": "Espada Venenosa",
                "Cobra": "Espada Venenosa",
                "Ogro": "Clava Grande",
                "Orc": "Clava",
                "Goblin": "Adaga Enferrujada",
                "Poltergeist": "Devoradora de Almas",
                "Vampiro": "Sanguessuga",
                "Esqueleto": "Espada de Osso",
            }
            ArmaInimigo['Loot'] = Arma_Guerreiro[ArmaInimigo['Nome']]
        elif Classe == 2:
            ArmaEquipada = ArmasComuns[9]["Nome"]
            AtaquePersonagem = ArmasComuns[9]["Ataque"]
            AtaquePersonagem += Inteligencia // 3
            Arma_Mago = {
                "Lobo": "Cajado da Fera",
                "Aranha": "Cajado Venenoso",
                "Cobra": "Cajado Venenoso",
                "Ogro": "Cajado da Terra",
                "Orc": "Cajado do Xamã",
                "Goblin": "Cajado de Madeira",
                "Poltergeist": "Cajado dos Espectros",
                "Vampiro": "Cajado Carmesim",
                "Esqueleto": "Cajado de Osso",
            }
            ArmaInimigo["Loot"] = Arma_Mago[ArmaInimigo["Nome"]]
        else:
            ArmaEquipada = ArmasComuns[18]["Nome"]
            AtaquePersonagem = ArmasComuns[18]["Ataque"]
            AtaquePersonagem += Destreza // 3
            Arma_Arqueiro = {
                "Lobo": "Arco Lupino",
                "Aranha": "Arco Venenoso",
                "Cobra": "Arco Venenoso",
                "Ogro": "Arco Bruto",
                "Orc": "Arco de Batalha",
                "Goblin": "Arco Desgastado",
                "Poltergeist": "Arco Devoradora de Almas",
                "Vampiro": "Arco Vampiríco",
                "Esqueleto": "Arco de Osso",
            }
            ArmaInimigo["Loot"] = Arma_Arqueiro[ArmaInimigo["Nome"]]

    for ArmaBoss in Bosses:
        if Classe == 1:
            Arma_Guerreiro = {
                "Dullahan": "Lança da Decapitação",
                "Dragão Negro": "Lâmina do Dragão",
                "Chimera": "Garras da Besta",
                "Drácula": "Espada Sombria",
                "Boitatá": "Machado Grande Flamejante",
                "Golem": "Martelo Colossal",
            }
            ArmaBoss["ArmaLendária"] = Arma_Guerreiro[ArmaBoss["Nome"]]
        elif Classe == 2:
            Arma_Mago = {
                "Dullahan": "Cetro dos Pesadelos",
                "Dragão Negro": "Ira Dracônica",
                "Chimera": "Cajado do Caos",
                "Drácula": "Livro das Sombras",
                "Boitatá": "Foice do Crepúsculo",
                "Golem": "Orbe da Terra",
            }
            ArmaBoss["ArmaLendária"] = Arma_Mago[ArmaBoss["Nome"]]
        else:
            Arma_Arqueiro = {
                "Dullahan": "Arco do Espectro Negro",
                "Dragão Negro": "Arco do Inferno Dracônico",
                "Chimera": "Arco Fúria da Chimera",
                "Drácula": "Arco do Vampiro Sanguinolento",
                "Boitatá": "Arco da Chama Lunar",
                "Golem": "Arco da Terra Sagrada",
            }
            ArmaBoss["ArmaLendária"] = Arma_Arqueiro[ArmaBoss["Nome"]]


# Função para determinar atributos dependendo da classe escolhida
def classes_atributos():
    """
    Espera: O jogador escolher uma classe\n
    Modifica: Os atributos\n
    Retorna: Os atributos da classe
    :return:
    """
    global Vitalidade, Defesa, Forca, Destreza, Inteligencia, ClasseNome, AtaquePersonagem
    if Classe == 1:
        ClasseNome = "Guerreiro"
        Vitalidade = 10
        Defesa = 5
        Forca = 15
        Destreza = 5
        Inteligencia = 5

    elif Classe == 2:
        ClasseNome = "Mago"
        Vitalidade = 5
        Defesa = 5
        Forca = 5
        Destreza = 5
        Inteligencia = 15
    elif Classe == 3:
        ClasseNome = "Arqueiro"
        Vitalidade = 7
        Defesa = 5
        Forca = 5
        Destreza = 15
        Inteligencia = 5


# Função para atualizar a vida máxima
def atualizar_vida_maxima():
    """
    Espera: O término da criação de personagem do jogador ou o personagem subir de nível\n
    Modifica: A vida do personagem do jogador\n
    Retorna: Aumento de Vida Máxima do personagem
    :return:
    """
    global VidaMaxima, VidaPersonagem
    VidaMaxima = 100
    VidaMaxima += 10 * Nivel + 5 * Vitalidade
    VidaPersonagem = VidaMaxima


# Função para o nivel subir ao pegar experiência o suficiente
def atualizar_nivel():
    """
    Espera: O personagem ganhar experiência o suficiente para subir de nível\n
    Modifica: O nível e a quantidade de PontosAtributos\n
    Retorna: Aumento de nível e PontosAtributos
    :return:
    """
    global ExperienciaPersonagem, ExperienciaNecessario, Nivel, PontosAtributos
    NivelAtual = Nivel
    while ExperienciaPersonagem > 0 and ExperienciaNecessario <= ExperienciaPersonagem:
        ExperienciaPersonagem -= ExperienciaNecessario
        Nivel += 1
        PontosAtributos += PONTO_ATRIBUTO_POR_NIVEL
        atualizar_vida_maxima()
        ExperienciaNecessario += 25
    if NivelAtual != Nivel:
        print(
            f"Você subiu de nível!\nVocê foi do nível {NivelAtual} para o nível {Nivel}"
        )

    print(f"Sua experiência: {ExperienciaPersonagem}")
    print(f"Experiência necessária para upar: {ExperienciaNecessario}")


# Função do combate contra boss + drop de item lendario
def combate_contra_boss():
    """
    Espera: O personagem cumprir com todas as condições\n
    Modifica: O tipo de inimigo que vai aparecer\n
    Retorna: Um chefe para o jogador derrotar
    :return:
    """
    global VidaPersonagem, ExperienciaPersonagem, MENU, PLAY, Boitata, Dullahan, Dragao, Dracula, Golem, Chimera
    global ArmaEquipada, AtaquePersonagem, AtaqueArma, Dinheiro, AtordoamentoPersonagem, TurnosEfeitosPersonagem
    global TurnosEfeitosInimigo, AtordoamentoInimigo, Defesa, Pocao
    if x == 6 and y == 0 and Nivel >= 15 and Boitata and not Dullahan:
        Boss = Bosses[4]
        Boitata = False
    elif x == 6 and y == 1 and Nivel >= 20 and Chimera and not Boitata:
        Boss = Bosses[2]
        Chimera = False
    elif x == 6 and y == 2 and Nivel >= 25 and Dracula and not Chimera:
        Boss = Bosses[3]
        Dracula = False
    elif x == 2 and y == 3 and Nivel >= 30 and Dragao and not Dracula:
        Boss = Bosses[1]
        Dragao = False
    elif x == 6 and y == 3 and Nivel >= 35 and Golem and not Dragao:
        Boss = Bosses[5]
        Golem = False
    elif x == 6 and y == 4 and Nivel >= 10 and Dullahan is True:
        Boss = Bosses[0]
        Dullahan = False
    else:
        return
    carregando_musicas("The Adventure Begins", True)
    InimigoHit = pygame.mixer.Sound("Músicas e Efeitos\\Efeitos\\EnemieHit.wav")
    CharacterHit = pygame.mixer.Sound("Músicas e Efeitos\\Efeitos\\CharacterHit.wav")
    MusicaPerigo = True
    NomeBoss = Boss["Nome"]
    VidaBoss = Boss["Vida"]
    DefesaBoss = Boss["Defesa"]
    DanoReal = AtaquePersonagem - Boss['Defesa']
    Local_Atual = BIOMAS[MAPA[y][x]]["Titulo"]
    if Boss["Nome"] == "Dullahan":
        efeito_escrita("Caminhando neste nevoeiro denso, você sente que esta sendo observado...\n", 0.07)
        sleep(1)
        efeito_escrita("Você para de caminhar e começa a olhar ao seu redor, tudo parece quieto demais...\n", 0.07)
        sleep(1)
        efeito_escrita("Em algum momento você percebe que um brilho azul se destaca dentre a nevoa.\n", 0.07)
        sleep(1)
        efeito_escrita("Você não sabe o que é, mas você sabe que está vindo na sua direção\n", 0.07)
        sleep(1)
        efeito_escrita("E quanto mais perto fica, mais você escuta os sons de um galope...\n", 0.07)
        sleep(1)
        efeito_escrita("De repente, os galopes param e o que antes era dificil de se enxergar, se revela na sua frente",
                       0.07)
        sleep(1)
        efeito_escrita("\nDullahan a criatura lendária está diante de você.", 0.10)
    elif Boss["Nome"] == "Dragão Negro":
        efeito_escrita("Enquanto você a montanha, você encontra uma caverna estranha...\n", 0.07)
        sleep(1)
        efeito_escrita("Afinal o brilho dourado dos tesouros é o que chama a atenção em um lugar tão escuro.\n", 0.07)
        sleep(1)
        efeito_escrita("Entrando na caverna você percebe que o ambiente é mais quente do que o normal.\n", 0.07)
        sleep(1)
        efeito_escrita("Mesmo assim, você prossegue em direção ao tesouro.\n", 0.07)
        sleep(1)
        efeito_escrita("Porém no meio do caminho, você tropeça em algo mas rapidamente se levanta\n", 0.07)
        sleep(1)
        efeito_escrita("Ao se levantar, você percebe duas grandes esferas vermelhas te encarando.\n", 0.07)
        sleep(1)
        efeito_escrita("De relance, parecem ser grandes rubis mas pouco a pouco vai se mostrando "
                       "que essas esferas são os olhos de um ser...\n", 0.07)
        sleep(1)
        efeito_escrita("Ser esse que por estar em um ambiente tão escuro se torna invisivel...\n", 0.07)
        sleep(1)
        efeito_escrita("Com o contraste entre esse ser e os tesouros ao fundo, você finalmente enxerga\n", 0.07)
        sleep(1)
        efeito_escrita("O Dragão Negro está diante de você.", 0.10)
    elif Boss["Nome"] == "Chimera":
        efeito_escrita("Andando pelas ruínas do que um dia foi uma bela vila, você encontra diversas carcaças"
                       "de animais\n", 0.07)
        sleep(1)
        efeito_escrita("Algumas carcaças parecem velhas, já outras parecem recentes\n", 0.07)
        sleep(1)
        efeito_escrita("Uma coisa é certa, você precisa cair o fora dai o mais rapido possíveln\n", 0.07)
        sleep(1)
        efeito_escrita("Infelizmente, já era tarde demais pois entre você e a saída havia uma criatura\n", 0.07)
        sleep(1)
        efeito_escrita("Ou talvez, 3 criaturas? De qualquer forma, Chimera está diante de você", 0.10)
        sleep(1)
    elif Boss["Nome"] == "Drácula":
        efeito_escrita("Desde que você chegou nesse lugar, um grande castelo podia ser visto de qualquer lugar\n", 0.07)
        sleep(1)
        efeito_escrita("E agora, você está adentrando este castelo\n", 0.07)
        sleep(1)
        efeito_escrita("E para sua surpresa o castelo contém só uma sala\n", 0.07)
        sleep(1)
        efeito_escrita("Sala essa que contém um longo tapete que leva pra um trono, muito luxuoso.\n", 0.07)
        sleep(1)
        efeito_escrita("Além disso o lugar não é tão bem iluminado.\n", 0.07)
        sleep(1)
        efeito_escrita("Indo mais fundo no castelo, as portas se fecham e o pouco de luz que havia se apaga\n", 0.07)
        sleep(1)
        efeito_escrita("Milhares de morcegos começam a aparecer dentro do castelo, "
                       "se aglomerando em um só lugar\n", 0.07)
        sleep(1)
        efeito_escrita("Você já está em posição de luta, e pouco a pouco é revelado o "
                       "ser que está diante de você\n", 0.07)
        sleep(1)
        efeito_escrita("Se prepare, pois Dracula não vai te deixar sair tão facil assim", 0.10)
    elif Boss["Nome"] == "Boitatá":
        efeito_escrita("Árvores mortas e carbonizadas, isso é tudo o que você vê.\n", 0.07)
        sleep(1)
        efeito_escrita("Mas estranhamente, você sente que tem muitos olhares direcionados a você...\n", 0.07)
        sleep(1)
        efeito_escrita("O ambiente se torna mais quente e os olhares mais fortes.\n", 0.07)
        sleep(1)
        efeito_escrita("A criatura que destruiu essa área, ainda não foi embora...\n", 0.07)
        sleep(1)
        efeito_escrita("A criatura lhe da o bote, mas você desvia e finalmente vê o culpado pela queima\n", 0.07)
        sleep(1)
        efeito_escrita("Boitatá está diante de você.", 0.10)
    else:
        efeito_escrita("Explorando a mina, você encontra um local enorme, e muitas pedras espalhadas\n", 0.07)
        sleep(1)
        efeito_escrita("Vasculhando mais um pouco o local, você encontra um baú escondido.\n", 0.07)
        sleep(1)
        efeito_escrita("Como qualquer bom aventureiro, você abre o baú, mas infelizmente o mesmo está vazio\n", 0.07)
        sleep(1)
        efeito_escrita("Porque na verdade, o baú era uma armadilha pois algo foi ativado.\n", 0.07)
        sleep(1)
        efeito_escrita("As pedras espalhadas começam a se juntar e pouco a pouco um golem vai se formando\n", 0.07)
        sleep(1)
        efeito_escrita("Se ele não morrer aqui, outras pessoas vão morrer.", 0.10)
    sleep(3)
    clear_console()
    while VidaBoss > 0 and VidaPersonagem > 0:
        if VidaPersonagem > 100 and MusicaPerigo:
            MusicaPerigo = False
            carregando_musicas("Decisive Battle", False)
        elif VidaPersonagem <= 100 and not MusicaPerigo:
            MusicaPerigo = True
            carregando_musicas("Danger!", False)
        linha("amarelo")
        print(f"Local:{Local_Atual}")
        linha("amarelo")
        print(f"Poções de cura: {Pocao}")
        linha("amarelo")
        print(f"{NomePersonagem} HP: {Fore.GREEN}{VidaPersonagem}/{VidaMaxima}")
        print(f"{NomeBoss} HP: {Fore.RED}{VidaBoss}/{Boss['Vida']}")
        print(f"Defesa do {NomeBoss}: {DefesaBoss}")
        linha("amarelo")
        # Caso o jogador não esteja atordoado.
        if not AtordoamentoPersonagem:
            OpcaoTurno = int(input("O que você irá fazer neste turno?:\n" "1.Atacar\n" "2.Curar\n"))
            # Combate do Jogador
            if OpcaoTurno == 1:
                if TurnosEfeitosPersonagem > 0:
                    TurnosEfeitosPersonagem -= 1
                # Caso a arma tenha algum efeito, a função 'mecanica_de_efeitos()' modifica as informações do inimigo
                VidaBoss, AtordoamentoInimigo, DefesaInimigo, DanoReal, VidaPersonagem, \
                    TurnosEfeitosInimigo = mecanica_de_efeitos(VidaBoss, AtordoamentoInimigo, DefesaBoss,
                                                               DanoReal, VidaPersonagem, TurnosEfeitosInimigo)
                # Atacando o Boss
                VidaBoss -= DanoReal

                linha("azul")
                sleep(1)
                # Mostra para o jogador o resultado
                CharacterHit.play()
                print(f"Você atacou {Fore.RED + NomeBoss} {Fore.WHITE}e arrancou "
                      f"{Fore.GREEN}{DanoReal} {Fore.WHITE}de vida")
                sleep(1)
            elif OpcaoTurno == 2 and Pocao >= 0:
                linha("azul")
                # Caso o jogador esteja sem poção de cura
                if Pocao <= 0:
                    efeito_escrita("Você está sem", 0.05)
                    print(f"{Fore.RED} poção de cura!")
                # Caso o jogador esteja com a vida cheia
                elif VidaPersonagem == VidaMaxima:
                    sleep(1)
                    print("Você já esta com a vida cheia!")
                    sleep(1)
                # Curando o personagem
                else:
                    SfxCura.play()
                    Pocao -= 1
                    VidaPersonagem = VidaPersonagem + 50
                    print("Você recuperou 50 de vida!")
                    # Código para a vida do personagem não ultrapassar a vida máxima
                    VidaPersonagem = min(VidaPersonagem, VidaMaxima)
            else:
                clear_console()
                linha("azul")
                sleep(1)
                print("Opção Inválida!\n" + Fore.RED + "Turno Perdido!")
                sleep(1)
        else:
            clear_console()
            linha("vermelho")
            sleep(1)
            print("Você está atordoado!")
            AtordoamentoPersonagem = False
        linha("azulvermelho")

        # Combate do Inimigo
        if VidaBoss > 0 and not AtordoamentoInimigo:
            if TurnosEfeitosInimigo > 0:
                TurnosEfeitosInimigo -= 1
            AtaqueBoss = randint(Boss["Dano"], Boss["Ataque"])
            AtaqueBoss -= Defesa // 3
            if AtaqueBoss < 0:
                AtaqueBoss = 0
            NomeBoss, VidaBoss, AtaqueBoss, AtordoamentoPersonagem, VidaPersonagem, Defesa, \
                TurnosEfeitosPersonagem = mecanica_de_efeitos_inimigos(NomeBoss, VidaBoss, AtaqueBoss,
                                                                       AtordoamentoPersonagem, VidaPersonagem,
                                                                       Defesa, TurnosEfeitosPersonagem)
            VidaPersonagem -= AtaqueBoss
            sleep(1)
            InimigoHit.play()
            print(f"{NomeBoss} te atacou e arrancou {Fore.RED}{AtaqueBoss} de vida")
            sleep(1)
            linha("vermelho")
        else:
            AtordoamentoInimigo = False
        input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        clear_console()

    if VidaBoss <= 0:
        print(f"Você derrotou o {NomeBoss} e ganhou {Boss['XP']} pontos de experiência")
        print(f"Você também ganhou {Fore.YELLOW} {Boss['Dinheiro']} moedas!")
        linha("azul")
        Dinheiro += Boss['Dinheiro']
        ExperienciaPersonagem += Boss["XP"]
        atualizar_nivel()
        CHANCE_OBTER_ARMA = 15
        if randint(1, 100) <= CHANCE_OBTER_ARMA:
            linha("amarelo")
            print(f"Você obteve a arma lendária! {Fore.YELLOW + Boss['ArmaLendária']}")
            for i, ArmaLendaria in enumerate(ArmasLendarias):
                if Boss["ArmaLendária"] == ArmaLendaria["Nome"]:
                    linha("amarelo")
                    # Pegando o dano da Arma
                    AtaqueArma = ArmaLendaria["Ataque"]
                    print(ArmaLendaria["Descrição"])
                    break
                Equipar = input("Deseja equipar?[S/N]:").strip().upper()
                while Equipar != "S" and Equipar != "N":
                    linha("vermelho")
                    print("Opção inválida!")
                    Equipar = input("Deseja equipar?[S/N]:").strip().upper()
                if Equipar == "S":
                    print(f"Você equipou {Fore.LIGHTYELLOW_EX} {Boss['ArmaLendária']}!")
                    ArmaEquipada = Boss['ArmaLendária']
                    AtaquePersonagem = AtaqueArma
                    if ClasseNome == "Guerreiro":
                        AtaquePersonagem += Forca // 3
                    elif ClasseNome == "Mago":
                        AtaquePersonagem += Inteligencia // 3
                    else:
                        AtaquePersonagem += Destreza // 3
                else:
                    linha("vermelho")
                    print(f"Você jogou {Boss['ArmaLendária']} fora!")
    else:
        linha("vermelho")
        print("Você Morreu")
        linha("vermelho")
        sleep(2)
        carregando_musicas("Title Theme", False)
        PLAY = False
        MENU = True
    TurnosEfeitosPersonagem = 0
    TurnosEfeitosInimigo = 0
    input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
    carregando_musicas("The Adventure Begins", False)
    clear_console()


# Função do combate contra inimigos + drop dos itens
def combate_contra_inimigo():
    """
    Espera: O personagem estar em um local que permite batalha\n
    Modifica: O tipo de inimigo que vai enfrentar o personagem\n
    Retorna: Um inimigo para o jogador derrotar
    :return:
    """
    global VidaPersonagem, ExperienciaPersonagem, PLAY, MENU, VidaInimigo, TurnosEfeitosInimigo, AtordoamentoInimigo
    global AtaquePersonagem, ArmaEquipada, AtaqueArma, AtordoamentoPersonagem, Defesa, TurnosEfeitosPersonagem
    global Dinheiro, Pocao
    Local_Atual = BIOMAS[MAPA[y][x]]["Titulo"]
    if Local_Atual in [
        "FLORESTA",
        "FLORESTA DENSA",
        "PÂNTANO",
        "FLORESTA MORTA",
        "COLINAS",
        "TRILHA",
        "PLANÍCIES",
    ] or not Boitata and Local_Atual in ["FLORESTA QUEIMADA"]:
        Inimigo = choice(Inimigos_Floresta)
    elif Local_Atual in [
        "MONTANHA",
        "DESFILADEIRO",
        "PEDREIRA",
        "CAMPO DE PEDRAS"
    ] or not Golem and Local_Atual in ["MINA DE PEDRAS"] or not Dragao and Local_Atual in ["CAVERNA"]:
        Inimigo = choice(Inimigos_Montanha)
    else:
        Inimigo = choice(Inimigos_Cemiterio)
    if VidaPersonagem > 100:
        MusicaPerigo = True
    else:
        MusicaPerigo = False
    InimigoHit = pygame.mixer.Sound("Músicas e Efeitos\\Efeitos\\EnemieHit.wav")
    CharacterHit = pygame.mixer.Sound("Músicas e Efeitos\\Efeitos\\CharacterHit.wav")
    VidaInimigo = Inimigo["Vida"]
    DefesaInimigo = Inimigo["Defesa"]
    NomeInimigo = Inimigo['Nome']
    DanoReal = AtaquePersonagem - Inimigo["Defesa"]
    while VidaInimigo > 0 and VidaPersonagem > 0:
        # Fazendo com que o jogo troque para uma música mais tensa caso o jogador esteja com a vida abaixo de 100
        if VidaPersonagem > 100 and MusicaPerigo:
            MusicaPerigo = False
            carregando_musicas("Battle Begins", False)
        elif VidaPersonagem <= 100 and not MusicaPerigo:
            MusicaPerigo = True
            carregando_musicas("Danger!", False)
        # Apresentando as Informações da batalha
        linha("amarelo")
        print(f"Local:{Local_Atual}")
        linha("amarelo")
        print(f"Poções de cura: {Pocao}")
        linha("amarelo")
        print(f"{NomePersonagem} HP: {Fore.GREEN}{VidaPersonagem}/{VidaMaxima}")
        print(f"{NomeInimigo} HP: {Fore.RED}{VidaInimigo}/{Inimigo['Vida']}")
        print(f"Defesa do {NomeInimigo}: {DefesaInimigo}")
        linha("amarelo")
        # Caso o jogador não esteja atordoado.
        if not AtordoamentoPersonagem:
            OpcaoTurno = input("O que você irá fazer neste turno?:\n" "1.Atacar\n" "2.Curar\n3.Fugir\n#")
            # Combate do Jogador
            if OpcaoTurno == "1":
                # Fazendo com que o turno de efeito negativo passe
                if TurnosEfeitosPersonagem > 0:
                    TurnosEfeitosPersonagem -= 1
                # Caso a arma tenha algum efeito, a função 'mecanica_de_efeitos()' modifica as informações do inimigo
                VidaInimigo, AtordoamentoInimigo, DefesaInimigo, DanoReal, VidaPersonagem, \
                    TurnosEfeitosInimigo = mecanica_de_efeitos(VidaInimigo, AtordoamentoInimigo, DefesaInimigo,
                                                               DanoReal, VidaPersonagem, TurnosEfeitosInimigo)
                # Atacando o inimigo
                VidaInimigo -= DanoReal

                linha("azul")
                sleep(1)
                # Mostra para o jogador o resultado
                CharacterHit.play()
                print(f"Você atacou {Fore.RED + NomeInimigo} {Fore.WHITE}e arrancou "
                      f"{Fore.GREEN}{DanoReal} {Fore.WHITE}de vida")
                sleep(1)
            elif OpcaoTurno == "2" and Pocao >= 0:
                linha("azul")
                # Caso o jogador esteja sem poção de cura
                if Pocao <= 0:
                    efeito_escrita("Você está sem", 0.05)
                    print(f"{Fore.RED} poção de cura!")
                # Caso o jogador esteja com a vida cheia
                elif VidaPersonagem == VidaMaxima:
                    sleep(1)
                    print("Você já esta com a vida cheia!")
                    sleep(1)
                # Curando o personagem
                else:
                    SfxCura.play()
                    Pocao -= 1
                    VidaPersonagem = VidaPersonagem + 50
                    print("Você recuperou 50 de vida!")
                    # Código para a vida do personagem não ultrapassar a vida máxima
                    VidaPersonagem = min(VidaPersonagem, VidaMaxima)
                # Caso o jogador queira fugir da batalha
            elif OpcaoTurno == "3":
                # Aleatorizando a chace do jogador conseguir fugir
                if random() < 0.3:
                    print("Você fugiu com sucesso!")
                    sleep(1)
                    return Durante_Local is True, carregando_musicas("The Adventure Begins", False), clear_console()
                else:
                    print("Você não conseguiu escapar...")
                    sleep(1)
                # Caso o jogador digite uma opção inválida.
            else:
                linha("azul")
                print("Opção Inválida!\n" + Fore.RED + "Turno Perdido!")
                sleep(1)
        # Caso o jogador esteja atordoado
        else:
            linha("vermelho")
            print("Você está atordoado!")
            AtordoamentoPersonagem = False
        linha("azulvermelho")

        # Combate do Inimigo
        # Caso o inimigo não esteja atordoado
        if VidaInimigo > 0 and not AtordoamentoInimigo:
            # Fazendo com que o turno de efeito negativo passe
            if TurnosEfeitosInimigo > 0:
                TurnosEfeitosInimigo -= 1
            # Pegando o dano do inimigo e subtraindo com a defesa do jogador
            AtaqueInimigo = randint(Inimigo["Dano"], Inimigo["Ataque"])
            AtaqueInimigo -= Defesa // 3
            if AtaqueInimigo < 0:
                AtaqueInimigo = 0

            # Caso o inimigo tenha a possibilidade de aplicar um efeito negativo no jogador
            NomeInimigo, VidaInimigo, AtaqueInimigo, AtordoamentoPersonagem, VidaPersonagem, Defesa, \
                TurnosEfeitosPersonagem = mecanica_de_efeitos_inimigos(NomeInimigo, VidaInimigo, AtaqueInimigo,
                                                                       AtordoamentoPersonagem, VidaPersonagem,
                                                                       Defesa, TurnosEfeitosPersonagem)
            # Atacando o personagem
            VidaPersonagem = VidaPersonagem - AtaqueInimigo
            sleep(1)
            # Apresentando o resultado para o jogador
            InimigoHit.play()
            print(f"{NomeInimigo} te atacou e arrancou {Fore.RED}{AtaqueInimigo} {Fore.WHITE}de vida")
            sleep(1)
            linha("vermelho")
        # Caso o inimigo esteja atordoado
        else:
            AtordoamentoInimigo = False
        input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        clear_console()

    # Condição de vitória
    if VidaInimigo <= 0:
        # Pegando informações de experiência e dinheiro
        print(f"Você derrotou o {NomeInimigo} e ganhou {Inimigo['XP']} pontos de experiência")
        print(f"Você também ganhou {Fore.YELLOW} {Inimigo['Dinheiro']} moedas!")
        linha("azul")
        Dinheiro += Inimigo['Dinheiro']
        ExperienciaPersonagem += Inimigo["XP"]
        atualizar_nivel()
        # Sistema de drop de itens
        if ArmaEquipada != Inimigo['Loot']:
            CHANCE_OBTER_ARMA = 30
            if randint(1, 100) <= CHANCE_OBTER_ARMA:
                clear_console()
                linha("amarelo")
                print(f"O inimigo dropou uma arma! {Fore.YELLOW + Inimigo['Loot']}")
                if 'Loot' in Inimigo:
                    for i, arma in enumerate(ArmasComuns):
                        if arma['Nome'] == Inimigo['Loot']:
                            linha("amarelo")
                            # Pegando o dano da Arma
                            AtaqueArma = arma['Ataque']
                            print(arma["Descrição"])
                            break
                    Equipar = input("Deseja equipar?[S/N]:").strip().upper()
                    while Equipar != "S" and Equipar != "N":
                        linha("vermelho")
                        print("Opção inválida!")
                        Equipar = input("Deseja equipar?[S/N]:").strip().upper()
                    if Equipar == "S":
                        print(f"Você equipou {Fore.LIGHTBLUE_EX} {Inimigo['Loot']}!")
                        ArmaEquipada = Inimigo['Loot']
                        AtaquePersonagem = AtaqueArma
                        if ClasseNome == "Guerreiro":
                            AtaquePersonagem += Forca // 3
                        elif ClasseNome == "Mago":
                            AtaquePersonagem += Inteligencia // 3
                        else:
                            AtaquePersonagem += Destreza // 3
                    else:
                        linha("vermelho")
                        print(f"Você jogou {Inimigo['Loot']} fora!")
    # Condição de derrota
    else:
        carregando_musicas("Title Theme", False)
        linha("vermelho")
        print("Você Morreu")
        linha("vermelho")
        sleep(2)
        PLAY = False
        MENU = True
    # Fazendo as trocas de músicas
    input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
    carregando_musicas("Battle Begins", True)
    carregando_musicas("The Adventure Begins", False)
    clear_console()


# Função de salvar jogo
def salvar_jogo():
    """
    Espera: O salvamento automatico ou o salvamento manual\n
    Modifica: Pega todas as informações do personagem
    Retorna: Um arquivo com todas as informações necessárias convertido em '.dat'
    :return:
    """
    info = {
        "NomePersonagem": NomePersonagem,
        "ClasseNome": ClasseNome,
        "Nivel": Nivel,
        "ArmaEquipada": ArmaEquipada,
        "ExperienciaPersonagem": ExperienciaPersonagem,
        "ExperienciaNecessario": ExperienciaNecessario,
        "VidaPersonagem": VidaPersonagem,
        "VidaMaxima": VidaMaxima,
        "AtaquePersonagem": AtaquePersonagem,
        "x": x,
        "y": y,
        "Dinheiro": Dinheiro,
        "Pocao": Pocao,
        "PontosAtributos": PontosAtributos,
        "Vitalidade": Vitalidade,
        "Defesa": Defesa,
        "Forca": Forca,
        "Destreza": Destreza,
        "Inteligencia": Inteligencia,
        "InimigosFloresta": Inimigos_Floresta,
        "InimigosMontanha": Inimigos_Montanha,
        "InimigosCemiterio": Inimigos_Cemiterio,
        "Bosses": Bosses,
        "Dullahan": Dullahan,
        "Dragão": Dragao,
        "Chimera": Chimera,
        "Boitatá": Boitata,
        "Dracula": Dracula,
        "Golem": Golem,
    }

    with open("save.dat", "wb") as arquivo_salvo:
        pickle.dump(info, arquivo_salvo)


def loja():
    global Dinheiro, Pocao, Defesa, Loja
    while Loja:
        clear_console()
        linha("verde")
        print("Seja Bem-Vindo a loja de 1 real..."
              f"\n{Fore.LIGHTBLACK_EX}Onde nada custa 1 real\nSério que bordão idiota...")
        linha("verde")
        print(f"Dinheiro: {Dinheiro}")
        print(f"Poção: {Pocao}")
        linha("verde")
        print(f"{Fore.BLUE}Fala ai 'Aventureiro' vai comprar o que?:")
        print(f"1 - {Fore.RED}Poção" + " - 5 Reais")
        print(f"2 - {Fore.MAGENTA}Melhorar Armadura (+1 Defesa) - 100 Reais")
        print(f"3 - {Fore.YELLOW}Tupperware - 5000 reais")
        print(f"4 - Sair")
        linha("verde")
        OpcaoLoja = input("#")

        if OpcaoLoja == "1":
            if Dinheiro >= 5:
                Pocao += 1
                Dinheiro -= 5
                print(f"{Fore.LIGHTBLACK_EX}Só usa poção quem não se garante na batalha...")
            else:
                print("Foi mal parceiro, esse produto não está por 1 real")
            input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        elif OpcaoLoja == "2":
            if Dinheiro >= 100:
                Defesa += 1
                Dinheiro -= 100
                print("Espero que isso te ajude.")
            else:
                print("Foi mal parceiro, esse produto não está por 1 real")
            input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        elif OpcaoLoja == "3":
            if Dinheiro >= 5000:
                print("Isso não vai te ajudar em nada nas suas batalhas, pq krls tu comprou isso?")
            else:
                print("Pq você quer comprar isso? De qualquer forma você nem tem dinheiro suficiente para comprar.")
            input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        elif OpcaoLoja == "4":
            print("Obrigado pela preferência...")
            Loja = False
            input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")


def vila():
    global Conversar, Nivel
    # Aumentando a tela do terminal
    os.system('mode con: cols=150 lines=24')
    while Conversar:
        clear_console()
        if Nivel < 10:
            print("Oh, você deve ser o aventureiro que a guilda central nos mandou!")
            sleep(1)
            print("Graças a Deus eles atenderam ao nosso pedido, esta área está cheia de monstro ultimamente!")
            sleep(1)
            print("É impossivel fazer qualquer comércio fora daqui com estes monstros por ai.")
            sleep(1)
            print("Mas agora que eles mandaram um aventureiro experiente não temos mais com o que nos preocupar.")
            sleep(2)
            print("O que? Você... Você é um aventureiro iniciante?.")
            sleep(1)
            print("Mas... mas eu pedi um aventureiro experiente! Esta área está cheia de monstros perigosos!")
            sleep(1)
            print("Eu sei que nossa vila é pequena mas ela é tem vidas aqui também! Eles poderiam ter mandado alguem"
                  " experiente...")
            sleep(1)
            print("Olha me desculpa, não quero te desmerecer nem nada, porém aqui é realmente perigoso, você realmente"
                  " pode dar conta disso?")
            sleep(1)
            print("Certo, mas antes de você começar a caçar os monstros grandes, vá caçar os pequenos!")
            print(f">{Fore.LIGHTBLACK_EX}Volte quando estiver no nível 10.")
        elif 10 <= Nivel <= 14:
            if Dullahan:
                print("Hmm... Vejo que você está mais forte... Acho que você pode lidar com o primeiro monstro.")
                sleep(1)
                print("Tem uma floresta não muito longe daqui que habita um grande mal, preciso que você lide com ele"
                      " antes que ele machuque mais alguém!")
                sleep(1)
                print("Aqui estão as coordenadas X = 6 e Y = 4")
            else:
                print("Você realmente deu conta do trabalho, estou impressionado!")
                sleep(1)
                print("Muito obrigado pelo seus esforços, mas você precisa ficar mais forte para o próximo monstro!")
                sleep(1)
                print(f"{Fore.LIGHTBLACK_EX}>Volte quando estiver nível 15.")
        elif 15 <= Nivel <= 19 and not Dullahan:
            if Boitata:
                print("Você está mais forte, isso é bom. Isso significa que você pode lidar com seu próximo alvo.")
                sleep(1)
                print("Sabe, tinhamos um lindo pomar de maçãs, mas infelizmente uma criatura a destruiu por completo")
                sleep(1)
                print("Ela era enorme e tinha olhos por todo o corpo! Só de lembra já me arrepio todo.")
                sleep(1)
                print("Enfim, por favor vá lidar com essa monstruosidade, aqui estão as Coordenadas: X = 6 e Y = 0")
            else:
                print("Você derrotou aquela coisa? Isso é incrível, agora podemos cultivar nosso pomar de novo!")
                sleep(1)
                print("Oh... a área está completamente queimada? Entendo...")
                sleep(1)
                print("De qualquer forma obrigado, volte quando estiver mais forte.")
                sleep(1)
                print(f"{Fore.LIGHTBLACK_EX}>Volte quando estiver nível 20.")
        elif 20 <= Nivel <= 24 and not Boitata:
            if Chimera:
                print("Vejo que você é mesmo empenhado. Isso me lembra da outra vila que tinha aqui por perto...")
                sleep(1)
                print("Todos viviam sorridentes até aquela coisa diabólica aparecer e destruir a vila por completo")
                sleep(1)
                print("Muitos não sobreviveram, alguns partiram para a Capital e outros se mudaram para essa vila...")
                sleep(1)
                print("Por favor, vingue vingue aqueles que estão de luto. Coordenadas: X = 6 e Y = 1")
            else:
                print("Você... Você realmente deu um fim aquela besta?")
                sleep(1)
                print(f"{Fore.LIGHTBLACK_EX}Lágrimas escorrem da face do humilde senhor.")
                sleep(1)
                print("Muito obrigado mesmo, você realmente vingou aqueles que estavam de luto "
                      "e também os que faleceram naquela tragédia...")
                sleep(1)
                print("Eu... agora preciso de um tempo, volte quando estiver mais forte.")
                sleep(1)
                print(f"{Fore.LIGHTBLACK_EX}>Volte quando estiver nível 25.")
        elif 25 <= Nivel <= 29 and not Chimera:
            if Dracula:
                print("Pelo o que eu sei, desde a fundação dessa vila, aquele castelo já existia.")
                sleep(1)
                print("Ninguem nunca soube quem vive la e sinceramente acho que é melhor assim afinal"
                      " a curiosidade já matou o gato.")
                sleep(1)
                print("Mas você como um ótimo aventureiro, poderia dar uma olha lá, só para ter certeza de que nenhum"
                      " monstro vive por lá")
                sleep(1)
                print("Aqui estão as Coordenadas: X = 6 and Y = 2")
            else:
                print("Então realmente tinha um monstro por lá, um pouco estranho visto que nunca atacou a vila...")
                sleep(1)
                print("Por algum motivo sinto que nós fomos o caçador ao invés da caça...")
                sleep(1)
                print("De qualquer forma, obrigado.")
                sleep(1)
                print(f"{Fore.LIGHTBLACK_EX}>Volte quando estiver nível 30.")
        elif 30 <= Nivel <= 34 and not Dracula:
            if Dragao:
                print("Existe uma montanha com uma caverna não muito longe daqui, "
                      "recentemente muitas pessoas desaparecem quando passam por lá.")
                sleep(1)
                print("Já mandamos muitas equipes de busca mas eles também não voltaram...")
                sleep(1)
                print("O que significa que isso é mais um trabalho para você, eu sei que você pode dar conta!")
                sleep(1)
                print("Coordenadas: X = 2 e Y = 3")
            else:
                print("UM DRAGÃO?!, não há dúvidas do porque as pessoas começaram a desaparecer!")
                sleep(1)
                print("Bom, pelo menos agora esses desaparecimentos foram resolvidos...")
                sleep(1)
                print("E aqueles que se foram, descansem em paz...")
                sleep(1)
                print("Obrigado, volte quando estiver mais forte.")
                sleep(1)
                print(f"{Fore.LIGHTBLACK_EX}>Volte quando estiver nível 35.")
        elif Nivel >= 35 and not Dragao:
            if Golem:
                print("Essa será a sua última tarefa, você evoluiu bastante "
                      "desde a primeira vez que você pisou por aqui.")
                sleep(1)
                print("Então estou realmente contando com você, ou melhor, todos nós desta vila estamos.")
                sleep(1)
                print("O lugar em questão é a nossa mina, durante uma das nossas excavações "
                      "encontramos algo assustador.")
                sleep(1)
                print("Então tome cuidado ao entrar lá, aqui estão as Coordenadas: X = 6 e Y = 3")
            else:
                print("Você derrotou aquele Golem gigantesco?!")
                sleep(1)
                print("Mal da para acreditar, se isto for verdade então o seu trabalho aqui acabou.")
                sleep(1)
                print("Todos nós deste humilde vilarejo o agradecemos muito pelo seus feitos")
                sleep(1)
                print("Você realmente salvou a nossa vila, muito obrigado!")
                sleep(1)
        OpcaoVila = input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para sair.")

        if OpcaoVila == "":
            os.system('mode con: cols=120 lines=30')
            Conversar = False


# Salas do Jogo
RUN = True
MENU = True
PLAY = False
# MAPA do Jogo
# Tamanho do mapa 6x4
MAPA = [
    ["Floresta", "Floresta", "Floresta", "Floresta Densa", "Pântano", "Floresta Morta", "Floresta Queimada"],
    ["Planícies", "Colinas", "Floresta", "Floresta", "Vila Abandonada", "Ruínas", "Ruínas do Santuário"],
    ["Trilha", "Trilha", "Vila", "Loja", "Trilha", "Montanha", "Castelo"],
    ["Campo de pedras", "Montanha", "Caverna", "Desfiladeiro", "Pedreira", "Depósito de Pedras", "Mina de Pedras"],
    ["Trilha", "Floresta", "Bosque brumoso", "Floresta dos Espiritos", "Cemitério", "Cemitério",
     "Floresta Densa Brumosa"],
]
Y_Len = len(MAPA) - 1
X_Len = len(MAPA[0]) - 1

BIOMAS = {
    "Floresta": {"Titulo": "FLORESTA", "Inimigo": True},
    "Floresta Densa": {"Titulo": "FLORESTA DENSA", "Inimigo": True},
    "Pântano": {"Titulo": "PÂNTANO", "Inimigo": True},
    "Floresta Morta": {"Titulo": "FLORESTA MORTA", "Inimigo": True},
    "Floresta Queimada": {"Titulo": "FLORESTA QUEIMADA", "Inimigo": True},
    "Planícies": {"Titulo": "PLANÍCIES", "Inimigo": True},
    "Colinas": {"Titulo": "COLINAS", "Inimigo": True},
    "Vila Abandonada": {"Titulo": "VILA ABANDONADA", "Inimigo": True},
    "Ruínas": {"Titulo": "RUÍNAS", "Inimigo": False},
    "Ruínas do Santuário": {"Titulo": "RUÍNAS DO SANTUÁRIO", "Inimigo": True},
    "Trilha": {"Titulo": "TRILHA", "Inimigo": True},
    "Vila": {"Titulo": "VILA DE SYLVERDALE", "Inimigo": False},
    "Loja": {
        "Titulo": f"LOJA DO 1 REAL\n{Fore.LIGHTBLACK_EX}Onde nada realmente custa 1 real.",
        "Inimigo": False,
    },
    "Montanha": {"Titulo": "MONTANHA", "Inimigo": True},
    "Castelo": {"Titulo": "CASTELO", "Inimigo": True},
    "Campo de pedras": {"Titulo": "CAMPO DE PEDRAS", "Inimigo": True},
    "Caverna": {"Titulo": "CAVERNA", "Inimigo": True},
    "Desfiladeiro": {"Titulo": "DESFILADEIRO", "Inimigo": True},
    "Pedreira": {"Titulo": "PEDREIRA", "Inimigo": True},
    "Depósito de Pedras": {"Titulo": "DEPÓSITO DE PEDRAS", "Inimigo": True},
    "Mina de Pedras": {"Titulo": "MINA DE PEDRAS", "Inimigo": True},
    "Bosque brumoso": {"Titulo": "BOSQUE BRUMOSO", "Inimigo": True},
    "Floresta dos Espiritos": {"Titulo": "FLORESTA DOS ESPÍRITOS", "Inimigo": True},
    "Cemitério": {"Titulo": "CEMITÉRIO", "Inimigo": True},
    "Floresta Densa Brumosa": {"Titulo": "FLORESTA DENSA BRUMOSA", "Inimigo": True},
}
# Letreiro do Jogo
os.system(f"title RPYG Game")
RPYG = pyfiglet.figlet_format("RPYG GAME").strip()
# Iniciando variável + criando a opção de desativar efeito de escrita.
clear_console()
MUSICA_TROCOU = False
escolha = ""
desativa_efeito_escrita = True
# Iniciando loop principal
while RUN:
    # Sub loop, para o MENU.
    carregando_musicas("Title Theme", False)
    while MENU:
        # Letreiro do Jogo.
        letreiro_jogo()
        # Exibindo as opções para o jogador.
        efeito_escrita("1.Novo Jogo\n2.Continuar\n3.Regras\n4.Sair\n", 0.05)
        linha("amarelo")
        # Caso nenhuma das escolhas satisfaçam as condições.
        if escolha not in ["", "1", "2", "3", "4", "5"]:
            print("Opção Inválida")
        # Pede para o jogador escolher uma das opções apresentadas acima.
        escolha = input("#")

        if escolha == "1":
            clear_console()
            letreiro_jogo()
            efeito_escrita("Bem-vindo a este jogo RPG feito no python! Levei muitas horas pra fazer,"
                           " então espero que goste!", 0.05)
            efeito_escrita("\nPara começarmos qual será o nome do seu personagem?:", 0.05)
            # Pedindo o nome do personagem
            NomePersonagem = input()
            clear_console()
            letreiro_jogo()
            # Criação do Personagem
            efeito_escrita("Qual será a sua classe?:", 0.05)
            Classe = int(input("\n1.Guerreiro \n2.Mago \n3.Arqueiro \n#"))
            linha("verde")
            # Puxa os atributos da classe
            classes_atributos()
            # Informa eles em seguida
            efeito_escrita("Aqui está os atributos desta classe:", 0.05)
            print("\nVitalidade:", Vitalidade,
                  "\nDefesa:", Defesa,
                  "\nForça:", Forca,
                  "\nDestreza:", Destreza,
                  "\nInteligência:", Inteligencia)
            linha("verde")
            mudar_arma_classe()
            # Caso Jogador queira escolher outra classe
            Opcao = str(input("Deseja ir com essa classe?[S/N]:")).strip().upper()[0]
            while Opcao != "S":
                if Opcao == "N":
                    clear_console()
                    letreiro_jogo()
                    efeito_escrita("Ok, qual vai ser então?:", 0.05)
                    # Perguntando novamente qual classe o jogador irá escolher
                    Classe = int(input("\n1.Guerreiro \n2.Mago \n3.Arqueiro \n#"))
                    linha("verde")
                    # Puxa os atributos da classe
                    classes_atributos()
                    efeito_escrita("Aqui está os atributos desta classe:", 0.05)
                    print("\nVitalidade:", Vitalidade,
                          "\nDefesa:", Defesa,
                          "\nForça:", Forca,
                          "\nDestreza:", Destreza,
                          "\nInteligência:", Inteligencia)
                    linha("verde")
                    # Perguntando se o jogador quer ir com esta classe mesmo.
                    Opcao = str(input("Deseja ir com essa classe?[S/N]:")).strip().upper()[0]
                else:
                    # Caso nenhuma das opções sejam reconhecidas
                    efeito_escrita("Opção Inválida!", 0.05)
                    sleep(3)
                    Opcao = "N"
            # Ajustes finais ao personagem
            atualizar_vida_maxima()
            mudar_arma_classe()
            clear_console()
            letreiro_jogo()
            # Mostrando todas as informações do personagem
            efeito_escrita("Certo, então aqui está todas as informações do seu personagem:\n", 0.05)
            linha("magenta")
            efeito_escrita(f"Nome do personagem: {NomePersonagem}\n", 0.05)
            efeito_escrita(f"Nivel do personagem: {Nivel}\n", 0.05)
            linha("magenta")
            efeito_escrita(f"Classe do personagem: {ClasseNome}\n", 0.05)
            efeito_escrita(f"Arma Equipada: {ArmaEquipada}\n", 0.05)
            efeito_escrita(f"Dano: {AtaquePersonagem}\n", 0.05)
            linha("magenta")
            efeito_escrita(f"Atributos da classe:", 0.05)
            print("\nVitalidade:", Vitalidade,
                  "\nDefesa:", Defesa,
                  "\nForça:", Forca,
                  "\nDestreza:", Destreza,
                  "\nInteligência:", Inteligencia)
            linha("magenta")
            sleep(5)
            clear_console()
            # Saindo do menu e entrando na GAMEPLAY
            carregando_musicas("Title Theme", True)
            carregando_musicas("The Adventure Begins", False)
            MENU = False
            PLAY = True
        elif escolha == "2":
            # Carregando arquivo de save
            try:
                with open("save.dat", "rb") as arquivo:
                    data = pickle.load(arquivo)
                    NomePersonagem = data["NomePersonagem"]
                    ClasseNome = data["ClasseNome"]
                    ArmaEquipada = data["ArmaEquipada"]
                    Nivel = data["Nivel"]
                    ExperienciaPersonagem = data["ExperienciaPersonagem"]
                    ExperienciaNecessario = data["ExperienciaNecessario"]
                    VidaPersonagem = data["VidaPersonagem"]
                    VidaMaxima = data["VidaMaxima"]
                    AtaquePersonagem = data["AtaquePersonagem"]
                    x = data["x"]
                    y = data["y"]
                    Dinheiro = data["Dinheiro"]
                    Pocao = data["Pocao"]
                    PontosAtributos = data["PontosAtributos"]
                    Vitalidade = data["Vitalidade"]
                    Defesa = data["Defesa"]
                    Forca = data["Forca"]
                    Destreza = data["Destreza"]
                    Inteligencia = data["Inteligencia"]
                    Inimigos_Floresta = data["InimigosFloresta"]
                    Inimigos_Montanha = data["InimigosMontanha"]
                    Inimigos_Cemiterio = data["InimigosCemiterio"]
                    Bosses = data["Bosses"]
                    Dullahan = data["Dullahan"]
                    Dragao = data["Dragão"]
                    Chimera = data["Chimera"]
                    Boitata = data["Boitatá"]
                    Dracula = data["Dracula"]
                    Golem = data["Golem"]
                    carregando_musicas("Title Theme", True)
                    carregando_musicas("The Adventure Begins", False)
                    MENU = False
                    PLAY = True
            # Caso não exista nenhum save
            except FileNotFoundError:
                efeito_escrita("Nenhum save foi encontrado!.", 0.05)
                sleep(1)
                clear_console()
            # Caso esteja faltando alguma informação no save
            except MemoryError:
                efeito_escrita("Save corrompido!.", 0.05)
                sleep(1)
                clear_console()
        elif escolha == "3":
            clear_console()
            letreiro_jogo()
            # Explicando como funciona o jogo
            efeito_escrita("\nO objetivo do jogo é derrotar os 6 Bosses disponíveis no jogo.\n", 0.05)
            sleep(0.5)
            efeito_escrita("Antes de enfrenta-los upe de nível e fique mais forte aumentando os status de seu"
                           " personagem \ne pegando equipamentos melhores.\n", 0.05)
            input(f"> {Fore.LIGHTBLACK_EX}Pressione ENTER para voltar.")
            clear_console()
        elif escolha == "4":
            sys.exit()
    # Sub loop, contém a GAMEPLAY.
    while PLAY:
        clear_console()
        if 3 >= x >= 2 == y and not MUSICA_TROCOU:
            carregando_musicas("The Adventure Begins", True)
            carregando_musicas("Take Some Rest", False)
            MUSICA_TROCOU = True
        elif 3 != x != 2 == y and MUSICA_TROCOU:
            MUSICA_TROCOU = False
            carregando_musicas("Take Some Rest", True)
            carregando_musicas("The Adventure Begins", False)
        # Salvamento Automático
        salvar_jogo()
        # Jogo Começa ou Retoma
        if desativa_efeito_escrita:
            # Checando se tem um inimigo no local
            if not Durante_Local:
                if BIOMAS[MAPA[y][x]]["Inimigo"]:
                    if randint(0, 100) <= 30:
                        Batalha = True
                        combate_contra_inimigo()
                    if Nivel >= 15:
                        Batalha = True
                        combate_contra_boss()
            linha("amarelo")
            efeito_escrita("\t0 - Salvar e Sair\n", 0.01)
            efeito_escrita("\t1 - Desativar o efeito de escrita\n", 0.01)
            if PontosAtributos == 0:
                efeito_escrita("\t2 - Ver status do personagem\n", 0.01)
            else:
                efeito_escrita("\t2 - Melhorar status do personagem!\n", 0.01)
            efeito_escrita("\t3 - Usar poção de cura\n", 0.01)
            linha("amarelo")

            # Exibe o nome do local em que o jogador está no momento
            efeito_escrita("LOCAL:" + BIOMAS[MAPA[y][x]]["Titulo"] + "\n", 0.01)
            # Informações do personagem
            linha("verde")
            efeito_escrita(
                f"Nome:{NomePersonagem}\n"
                f"Nivel:{Nivel}\n"
                f"XP:{ExperienciaPersonagem}/{ExperienciaNecessario}\n"
                f"Dinheiro: {Dinheiro}\n"
                f"Poções: {Pocao}\n"
                f"HP:{VidaPersonagem}/{VidaMaxima}\n"
                f"Dano: {AtaquePersonagem}\n"
                f"Coord: {x},{y}\n", 0.01,)
            linha("verde")
        else:
            # Checando se tem um inimigo no local.
            if not Durante_Local:
                # Checando se o bioma em que o jogador está permite uma batalha.
                if BIOMAS[MAPA[y][x]]["Inimigo"]:
                    # Roletando a chance do jogador entrar em batalha com um inimigo.
                    if randint(0, 100) <= 30:
                        Batalha = True
                        combate_contra_inimigo()
                    # Liberando a batalha contra os bosses.
                    if Nivel >= 10:
                        Batalha = True
                        combate_contra_boss()
            # Interações especiais que o jogador pode fazer.
            linha("amarelo")
            print("\t0 - Salvar e Sair")
            print("\t1 - Ativar efeito de escrita")
            if PontosAtributos == 0:
                print("\t2 - Ver status do personagem")
            else:
                print("\t2 - Melhorar status do personagem!")
            print("\t3 - Usar poção de cura")
            linha("amarelo")
            # Exibe o nome do local em que o jogador está no momento.
            print("LOCAL:" + BIOMAS[MAPA[y][x]]["Titulo"])
            # Informações do personagem.
            linha("verde")
            print(
                f"Nome:{NomePersonagem}\n"
                f"Nivel:{Nivel}\n"
                f"XP:{ExperienciaPersonagem}/{ExperienciaNecessario}\n"
                f"Dinheiro: {Dinheiro}\n"
                f"Poções: {Pocao}\n"
                f"HP:{VidaPersonagem}/{VidaMaxima}\n"
                f"Dano: {AtaquePersonagem}\n"
                f"Coord: {x},{y}"
            )
            linha("verde")
        # Movimentação pelo MAPA.
        if y > 0:
            print("N - Norte")
        if x < X_Len:
            print("L - Leste")
        if y < Y_Len:
            print("S - Sul")
        if x > 0:
            print("O - Oeste")
        if MAPA[y][x] == "Loja" or MAPA[y][x] == "Vila":
            print("7 - Entrar")
        # Escolha do jogador.
        dest = input("#").upper().strip()

        # Tratando um bug, onde caso o usuário não digitasse nada o jogo crashava.
        if dest:
            dest = dest[0]
        else:
            Durante_Local = True
            clear_console()

        # Salva o jogo e volta para o menu.
        if dest == "0":
            clear_console()
            cont = 0
            Durante_Local = True
            PLAY = False
            MENU = True
            salvar_jogo()
        elif dest == "1":
            Durante_Local = True
            # Desativa ou Ativa a função efeito_escrita()
            if desativa_efeito_escrita:
                desativa_efeito_escrita = False
            else:
                desativa_efeito_escrita = True
        elif dest == "2":
            Durante_Local = True
            # Um loop onde só acabará depois que o jogador gastar todos os seus pontos.
            while PontosAtributos > 0:
                clear_console()
                linha("amarelo")
                print("1.Vitalidade:", Vitalidade,
                      "\n2.Defesa:", Defesa,
                      "\n3.Força:", Forca,
                      "\n4.Destreza:", Destreza,
                      "\n5.Inteligência:", Inteligencia)
                linha("amarelo")
                # Mostrando quantos pontos o jogador ainda tem.
                print(f"Pontos restantes: {PontosAtributos}")
                # Perguntando para o jogador qual atributo ele irá upar.
                Atributo = input("Qual atributo irá upar?:")
                # Perguntando quantos pontos ele irá gastar.
                PontosGastos = int(input("Quantos pontos irá gastar?: "))
                if PontosGastos > PontosAtributos or PontosGastos < 0:
                    print("Você não tem essa quantidade de pontos.")

                if Atributo == "1":
                    Vitalidade += PontosGastos
                    PontosAtributos -= PontosGastos
                    atualizar_vida_maxima()
                elif Atributo == "2":
                    Defesa += PontosGastos
                    PontosAtributos -= PontosGastos
                elif Atributo == "3":
                    Forca += PontosGastos
                    PontosAtributos -= PontosGastos
                    if ClasseNome == "Guerreiro":
                        aumento_de_ataque = PontosGastos // 3
                        AtaquePersonagem += aumento_de_ataque
                elif Atributo == "4":
                    Destreza += PontosGastos
                    PontosAtributos -= PontosGastos
                    if ClasseNome == "Arqueiro":
                        aumento_de_ataque = PontosGastos // 3
                        AtaquePersonagem += aumento_de_ataque
                elif Atributo == "5":
                    Inteligencia += PontosGastos
                    PontosAtributos -= PontosGastos
                    if ClasseNome == "Mago":
                        aumento_de_ataque = PontosGastos // 3
                        AtaquePersonagem += aumento_de_ataque
            clear_console()
            # Mostrando os status do personagem.
            linha("amarelo")
            print("Vitalidade:", Vitalidade,
                  "\nDefesa:", Defesa,
                  "\nForça:", Forca,
                  "\nDestreza:", Destreza,
                  "\nInteligência:", Inteligencia)
            linha("amarelo")
            input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        elif dest == "3":
            Durante_Local = True
            if Pocao > 0:
                if Pocao > 0 and VidaPersonagem < VidaMaxima:
                    Pocao -= 1
                    SfxCura.play()
                    VidaPersonagem += 50
                    VidaPersonagem = min(VidaPersonagem, VidaMaxima)
                else:
                    print("Sua vida já está cheia!.")
                    input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
            else:
                print("Você não tem poção de cura!")
                input(f">{Fore.LIGHTBLACK_EX}Pressione ENTER para continuar.")
        elif dest == "N":
            # Indo para cima no mapa
            if y > 0:
                y -= 1
                Durante_Local = False
        elif dest == "L":
            # Indo para direita no mapa
            if x < X_Len:
                x += 1
                Durante_Local = False
        elif dest == "S":
            # Indo para baixo no mapa
            if y < Y_Len:
                y += 1
                Durante_Local = False
        elif dest == "O":
            # Indo para esquerda no mapa
            if x > 0:
                x -= 1
                Durante_Local = False
        elif dest == "7":
            if MAPA[y][x] == "Loja":
                Loja = True
                loja()
            if MAPA[y][x] == "Vila":
                Conversar = True
                vila()
