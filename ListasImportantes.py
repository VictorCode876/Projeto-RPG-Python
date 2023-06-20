from colorama import init, Fore
init(autoreset=True)
# Armas (Guerreiro, Mago e Arqueiro)
ArmasComuns = [
    # Classe Guerreiro
    {
        "Nome": "Espada de Ferro",
        "Ataque": 10,
        "Descrição": "Uma espada de ferro comum."
    },

    {
        "Nome": "Espada do Lobo Curva",
        "Ataque": 15,
        "Descrição": "É uma espada curva com adorno de um lobo."
    },

    {
        "Nome": "Espada Venenosa",
        "Ataque": 8,
        "Descrição": "Se eu fosse você, eu não tocaria na lâmina dessa espada."
                     "\nTem chande causar veneno nos inimigos"
    },

    {
        "Nome": "Clava Grande",
        "Ataque": 30,
        "Descrição": "Clava de madeira enorme, perfeita para atordoar inimigos!"
    },

    {
        "Nome": "Clava",
        "Ataque": 30,
        "Descrição": "Uma clava de madeira normal, tem chance de causar atordoamento."
    },

    {
        "Nome": "Adaga Enferrujada",
        "Ataque": 7,
        "Descrição": "Lixo."
    },

    {
        "Nome": "Devoradora de Almas",
        "Ataque": 18,
        "Descrição": "Você pode escutar o tormento das almas que foram devoradas por esta arma."
                     "\nTem chance de matar um inimigo instantaneamente."
    },

    {
        "Nome": "Sanguessuga",
        "Ataque": 15,
        "Descrição": "Uma espada encharcada em sangue, como se a própria o produzisse."
                     "\nRouba vida do inimigo"
    },

    {
        "Nome": "Espada de Osso",
        "Ataque": 20,
        "Descrição": "Uma espada feito de fêmur, parece ser muito resistente.\nChance de causar atordoamento"
    },
    # Classe Mago
    {
        "Nome": "Cajado de Iniciante",
        "Ataque": 7,
        "Descrição": "Um cajado de um iniciante."
    },

    {
        "Nome": "Cajado da Fera",
        "Ataque": 15,
        "Descrição": "É um cajado com o adorno de uma fera."
    },

    {
        "Nome": "Cajado Venenoso",
        "Ataque": 10,
        "Descrição": "Feito com uma madeira de tom verde.\nTem chande causar veneno nos inimigos"
    },

    {
        "Nome": "Cajado da Terra",
        "Ataque": 25,
        "Descrição": "Um cajado rústico e grande. Suas magias podem causar atordoamento!"
    },

    {
        "Nome": "Cajado do Xamã",
        "Ataque": 20,
        "Descrição": "Um cajado que emite energia negra. Chance de uma chama negra queimar seus inimigos."
    },

    {
        "Nome": "Cajado de Madeira",
        "Ataque": 5,
        "Descrição": "Lixo."
    },

    {
        "Nome": "Cajado dos Espectros",
        "Ataque": 20,
        "Descrição": "Você pode escutar o tormento das almas que foram devoradas por esta arma."
                     "\nTem chance de matar um inimigo instantaneamente."
    },

    {
        "Nome": "Cajado Carmesim",
        "Ataque": 15,
        "Descrição": "Um cajado vermelho sangue decorada com asas de vampiro."
                     "\nRouba vida do inimigo"
    },

    {
        "Nome": "Cajado de Osso",
        "Ataque": 25,
        "Descrição": "Um cajado com uma caveira na ponta.\nChance de causar atordoamento"
    },
    # Classe Arqueiro
    {
        "Nome": "Arco de Madeira",
        "Ataque": 7,
        "Descrição": "Um arco de madeira comum."
    },

    {
        "Nome": "Arco Lupino",
        "Ataque": 20,
        "Descrição": "Um arco envolto em pele de lobo, bem confortavel."
    },

    {
        "Nome": "Arco Venenoso",
        "Ataque": 12,
        "Descrição": "Um arco que imbue suas flechas com veneno.\nTem chance de causar veneno nos inimigos"
    },

    {
        "Nome": "Arco Bruto",
        "Ataque": 30,
        "Descrição": "Um arco grande que deixa suas flechas pesadas.\nTem chance de causar atordoamento"
    },

    {
        "Nome": "Arco de Batalha",
        "Ataque": 20,
        "Descrição": "Um arco que deixa suas flechas um pouco pesadas.\nTem chance de causar atordoamento."
    },

    {
        "Nome": "Arco Desgastado",
        "Ataque": 5,
        "Descrição": "Lixo."
    },

    {
        "Nome": "Arco Devoradora de Almas",
        "Ataque": 25,
        "Descrição": "Você pode escutar o tormento das almas que foram devoradas por esta arma."
                     "\nTem chance de causar dano crítico."
    },

    {
        "Nome": "Arco Vampiríco",
        "Ataque": 18,
        "Descrição": "Um arco preto e branco que fazem suas flechas sangrarem."
                     "\nRouba vida do inimigo."
    },

    {
        "Nome": "Arco de Osso",
        "Ataque": 20,
        "Descrição": "Um arco feito com vários ossos, parece ser muito resistente."
                     "\nChance moderada de causar atordoamento."
    },
]
ArmasLendarias = [
    # Classe Guerreiro
    {
        "Nome": "Lança da Decapitação",
        "Ataque": 75,
        "Descrição": "Uma lança preta com adornos de ouro.\nEla ignora defesa."
    },

    {
        "Nome": "Lâmina do Dragão",
        "Ataque": 65,
        "Descrição": "Uma lâmina abençoada pelo poder do dragão.\nChance alta de causar Queimadura."
    },

    {
        "Nome": "Garras da Besta",
        "Ataque": 60,
        "Descrição": "Garras que contém várias peçonhas.\nChance alta de causar Veneno, Paralisia e Queimadura."
    },

    {
        "Nome": "Espada Sombria",
        "Ataque": 70,
        "Descrição": "Uma espada mais escura que preto.\nAumenta a quantidade de vida recuperada."
    },

    {
        "Nome": "Machado Grande Flamejante",
        "Ataque": 95,
        "Descrição": "Um grande machado de bronze que parece estar quente o tempo todo."
                     "\nEla queimará seus inimigos.\nChance alta de causar Queimadura."
    },

    {
        "Nome": "Martelo Colossal",
        "Ataque": 110,
        "Descrição": "Um martelo gigantesco feito de pedras.\nSeus inimigos irão sofrer atordoamento constante."
                     "\nChance alta de causar Atordoamento."
    },
    # Classe Mago
    {
        "Nome": "Cetro dos Pesadelos",
        "Ataque": 50,
        "Descrição": "Um cetro onde almas o circulam sem parar.\nChance alta de matar inimigos instantaneamente."
    },

    {
        "Nome": "Ira Dracônica",
        "Ataque": 65,
        "Descrição": "Um cajado que emana energia de dragão.\nSeus inimigos irão derreter."
    },

    {
        "Nome": "Cajado do Caos",
        "Ataque": 50,
        "Descrição": "Um cajado difícil de se descrever.\nEla pode inflingir Veneno, Paralisia e Queimadura"
    },

    {
        "Nome": "Livro das Sombras",
        "Ataque": 55,
        "Descrição": "Um livro cheio de magias negras.\nAumenta a quantidade de vida recuperada."
    },

    {
        "Nome": "Foice do Crepúsculo",
        "Ataque": 80,
        "Descrição": "Uma foice mágica preta e laranja remetendo ao Crepúsculo."
                     "\nEla inflige queimadura e ignora metade da defesa"
    },

    {
        "Nome": "Orbe da Terra",
        "Ataque": 100,
        "Descrição": "Um orbe de pedra que circula ao seu redor."
                     "\nSeus inimigos sofreram atordoamento constantemente."
    },
    # Classe Arqueiro
    {
        "Nome": "Arco do Espectro Negro",
        "Ataque": 70,
        "Descrição": "Um arco que vai penetrar todos os espectros de seus inimigos.\nEla ignora defesa."
    },

    {
        "Nome": "Arco do Inferno Dracônico",
        "Ataque": 60,
        "Descrição": "Um arco com uma cabeça de dragão, transformando suas flechas em bolas de fogo."
                     "\nChance alta de causar queimadura."
    },

    {
        "Nome": "Arco Fúria da Chimera",
        "Ataque": 50,
        "Descrição": "Um arco com as três cabeças da Chimera, colocando peçonha nas suas flechas."
                     "\nEla pode inflingir Veneno, Paralisia e Queimadura, com uma chance de 30% para cada efeito."
    },

    {
        "Nome": "Arco do Vampiro Sanguinolento",
        "Ataque": 65,
        "Descrição": "Um arco vermelho com adornos pretos, transformam suas flechas em morcegos."
                     "\nAumenta a quantidade de vida recuperada."
    },

    {
        "Nome": "Arco da Chama Lunar",
        "Ataque": 90,
        "Descrição": "Um arco preto e azul, imbue suas flechas com a Chama Lunar."
                     "\nAs flechas com Chama Lunar causam dano adicional de gelo e queimadura."
    },

    {
        "Nome": "Arco da Terra Sagrada",
        "Ataque": 120,
        "Descrição": "Um arco de pedra com adornos dourados, suas flechas são super pesadas."
                     "\nChance alta de causar atordoamento"
    },
]
Efeitos_Armas = {
    # Classe Guerreiro
    "Espada Venenosa": {
        "Chance": 0.4,
        "Mensagem": f"{Fore.GREEN}O alvo foi envenenado!"
    },

    "Clava Grande": {
        "Chance": 0.5,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    "Clava": {
        "Chance": 0.3,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    "Devoradora de Almas": {
        "Chance": 0.1,
        "Mensagem": f"{Fore.MAGENTA}O inimigo teve sua alma devorada."
    },
    "Sanguessuga": {
        "Chance": 0.8,
        "Mensagem": f"{Fore.RED}O alvo teve sua vida drenada!"
    },
    "Espada de Osso": {
        "Chance": 0.4,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    # Classe Mago
    "Cajado Venenoso": {
        "Chance": 0.5,
        "Mensagem": f"{Fore.GREEN}O alvo foi envenenado!"
    },

    "Cajado da Terra": {
        "Chance": 0.5,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    "Cajado do Xamã": {
        "Chance": 0.3,
        "Mensagem": f"{Fore.YELLOW}O alvo está queimando!"
    },
    "Cajado dos Espectros": {
        "Chance": 0.1,
        "Mensagem": f"{Fore.MAGENTA}O inimigo teve o espectro de sua alma quebrada."
    },
    "Cajado Carmesim": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.RED}O alvo teve sua vida drenada!"
    },
    "Cajado de Osso": {
        "Chance": 0.4,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    # Classe Arqueiro
    "Arco Venenoso": {
        "Chance": 0.5,
        "Mensagem": f"{Fore.GREEN}O alvo foi envenenado!"
    },

    "Arco Bruto": {
        "Chance": 0.5,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    "Arco de Batalha": {
        "Chance": 0.3,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    "Arco Devoradora de Almas": {
        "Chance": 0.1,
        "Mensagem": f"{Fore.MAGENTA}O inimigo teve sua alma devorada."
    },
    "Arco Vampiríco": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.RED}O alvo teve sua vida drenada!"
    },
    "Arco de Osso": {
        "Chance": 0.4,
        "Mensagem": f"{Fore.YELLOW}O alvo foi atordoado!"
    },
    # Classe Guerreiro Armas Lendarias
    "Lança da Decapitação": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.BLUE}O alvo teve sua defesa penetrada!"
    },

    "Lâmina do Dragão": {
        "Chance": 0.8,
        "Mensagem": f"{Fore.RED}O alvo está queimando nas chamas dracônicas!"
    },
    "Garra da Besta": {
        "Chance": 0.6,
        "Mensagem": f"{Fore.YELLOW}O alvo foi Envenenado, Paralizado e está Queimando!"
    },
    "Espada Sombria": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.MAGENTA}Você roubou boa parte da vida do inimigo."
    },
    "Machado Grande Flamejante": {
        "Chance": 0.6,
        "Mensagem": f"{Fore.RED}O inimigo está queimando vivo!"
    },
    "Martelo Colossal": {
        "Chance": 0.7,
        "Mensagem": f"{Fore.YELLOW}A pancada foi tão forte que o inimigo nem viu da onde veio. "
                    f"O alvo foi atordoado!"
    },
    # Classe Mago Armas Lendárias
    "Cetro dos Pesadelos": {
        "Chance": 0.3,
        "Mensagem": f"{Fore.GREEN}A alma do inimigo agora circula o seu cetro."
    },

    "Ira Dracônica": {
        "Chance": 0.8,
        "Mensagem": f"{Fore.YELLOW}O alvo está sendo torrado nas chamas dracônicas"
    },
    "Cajado do Caos": {
        "Chance": 0.6,
        "Mensagem": f"{Fore.YELLOW}O alvo foi Envenenado, Paralizado e está Queimando!"
    },
    "Livro das Sombras": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.MAGENTA}Você drenou boa parte da vida do inimigo."
    },
    "Foice do Crepúsculo": {
        "Chance": 0.7,
        "Mensagem": f"{Fore.RED}Você penetrou a armadura do inimigo e castou uma combustão no impacto!"
    },
    "Orbe da Terra": {
        "Chance": 0.8,
        "Mensagem": f"{Fore.YELLOW}O orbe fez um ótimo trabalhou e o deixou atordoado!"
    },
    # Classe Arqueiro Armas Lendarias
    "Arco do Espectro Negro": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.BLUE}A defesa do inimigo foi penetrada!"
    },

    "Arco do Inferno Dracônico": {
        "Chance": 0.7,
        "Mensagem": f"{Fore.YELLOW}Nem o sol é tão quente quanto essas chamas."
    },
    "Arco Fúria da Chimera": {
        "Chance": 0.6,
        "Mensagem": f"{Fore.YELLOW}O alvo foi Envenenado, Paralizado e está Queimando!"
    },
    "Arco do Vampiro Sanguinolento": {
        "Chance": 1.0,
        "Mensagem": f"{Fore.MAGENTA}Você roubou boa parte da vida do inimigo."
    },
    "Arco da Chama Lunar": {
        "Chance": 0.8,
        "Mensagem": f"{Fore.RED}O brilho da Chama Lunar é tão lindo quanto a lua."
    },
    "Arco da Terra Sagrada": {
        "Chance": 0.7,
        "Mensagem": f"{Fore.YELLOW}HEADSHOT! Alvo atordoado!"
    },

}

# Listas de Inimigos
Inimigos_Floresta = [
    {
        "Nome": "Lobo",
        "Vida": 35,
        "Defesa": 5,
        "Ataque": 20,
        "Dano": 15,
        "XP": 10,
        "Dinheiro": 8,
        "Loot": "",
        "Efeito": "Sangramento",
        "Chance": 0.2
    },
    {
        "Nome": "Aranha",
        "Vida": 25,
        "Defesa": 3,
        "Ataque": 15,
        "Dano": 10,
        "XP": 8,
        "Dinheiro": 5,
        "Loot": "",
        "Efeito": "Veneno",
        "Chance": 0.3
    },
    {
        "Nome": "Cobra",
        "Vida": 30,
        "Defesa": 2,
        "Ataque": 20,
        "Dano": 10,
        "XP": 12,
        "Dinheiro": 7,
        "Loot": "",
        "Efeito": "Veneno",
        "Chance": 0.3
    },
]
Inimigos_Montanha = [
    {
        "Nome": "Ogro",
        "Vida": 100,
        "Defesa": 15,
        "Ataque": 40,
        "Dano": 25,
        "XP": 35,
        "Dinheiro": 20,
        "Loot": "",
        "Efeito": "Atordoamento",
        "Chance": 0.3
    },
    {
        "Nome": "Orc",
        "Vida": 75,
        "Defesa": 10,
        "Ataque": 30,
        "Dano": 20,
        "XP": 30,
        "Dinheiro": 16,
        "Loot": "",
        "Efeito": "Atordoamento",
        "Chance": 0.2
    },
    {
        "Nome": "Goblin",
        "Vida": 30,
        "Defesa": 5,
        "Ataque": 20,
        "Dano": 15,
        "XP": 10,
        "Dinheiro": 7,
        "Loot": "",
        "Efeito": "Nenhum",
        "Chance": 0.0
    },
]
Inimigos_Cemiterio = [
    {
        "Nome": "Poltergeist",
        "Vida": 60,
        "Defesa": 12,
        "Ataque": 25,
        "Dano": 12,
        "XP": 20,
        "Dinheiro": 20,
        "Loot": "",
        "Efeito": "Roubo de Alma",
        "Chance": 0.02
    },

    {
        "Nome": "Vampiro",
        "Vida": 100,
        "Defesa": 6,
        "Ataque": 18,
        "Dano": 8,
        "XP": 30,
        "Dinheiro": 30,
        "Loot": "",
        "Efeito": "Roubo de Vida",
        "Chance": 0.6
    },
    {
        "Nome": "Esqueleto",
        "Vida": 45,
        "Defesa": 8,
        "Ataque": 20,
        "Dano": 10,
        "XP": 15,
        "Dinheiro": 12,
        "Loot": "",
        "Efeito": "Atordoamento",
        "Chance": 0.04
    },
]

# Lista dos Bosses
Bosses = [
    {
        "Nome": "Dullahan",
        "Vida": 400,
        "Ataque": 90,
        "Defesa": 20,
        "Dano": 60,
        "Dinheiro": 230,
        "XP": 150,
        "ArmaLendária": "",
        "Efeito": "Ignorar Defesa",
        "Chance": 1.0
    },
    {
        "Nome": "Dragão Negro",
        "Vida": 550,
        "Ataque": 130,
        "Defesa": 25,
        "Dano": 80,
        "Dinheiro": 500,
        "XP": 275,
        "ArmaLendária": "",
        "Efeito": "Queimadura",
        "Chance": 0.3
    },
    {
        "Nome": "Chimera",
        "Vida": 450,
        "Ataque": 100,
        "Defesa": 15,
        "Dano": 70,
        "Dinheiro": 330,
        "XP": 225,
        "ArmaLendária": "",
        "Efeito": "TriEfeitos",
        "Chance": 0.2
    },
    {
        "Nome": "Drácula",
        "Vida": 400,
        "Ataque": 60,
        "Defesa": 15,
        "Dano": 50,
        "Dinheiro": 430,
        "XP": 250,
        "ArmaLendária": "",
        "Efeito": "Roubo de vida",
        "Chance": 1.0
    },
    {
        "Nome": "Boitatá",
        "Vida": 500,
        "Ataque": 110,
        "Defesa": 20,
        "Dano": 80,
        "Dinheiro": 250,
        "XP": 200,
        "ArmaLendária": "",
        "Efeito": "Queimadura",
        "Chance": 0.3
    },
    {
        "Nome": "Golem",
        "Vida": 700,
        "Ataque": 150,
        "Defesa": 30,
        "Dano": 100,
        "Dinheiro": 600,
        "XP": 500,
        "ArmaLendária": "",
        "Efeito": "Atordoamento",
        "Chance": 0.5
    },
]
