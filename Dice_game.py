import random
import sys


class Status:
    global wins
    global loses
    global dificuldade
    wins = 0
    loses = 0
    dificuldade = 1


class Colors_sounds:
    import colorama
    from colorama import Fore
    from playsound import playsound

    global colors, sounds, playsound
    colors = (
        Fore.RED,
        Fore.GREEN,
        Fore.BLUE,
        Fore.BLACK,
        Fore.WHITE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.YELLOW,
    )
    sounds = "RATTLE2.wav", "roll.wav"


def roll_the_dice_game():
    try_again = ""

    global wins
    global loses
    global dificuldade

    playsound(sounds[0])
    guess = random.randrange(1, 60)
    playsound(sounds[1])
    dice_roll = random.randrange(1, 20)

    if guess <= dice_roll:
        guess = random.randrange(1, 60)

    print(colors[2] + f"Sem tempo limite, dificuldade: {dificuldade}")
    print(colors[2] + "Para parar o jogo, basta digitar STOP como resposta.")
    print(
        colors[2]
        + "Você poderá checar seus erros e acertos ao parar o jogo, no começo e ao final de cada rodada."
    )
    print()
    print(colors[5] + f"Score atual -> Acertos: {wins} Erros: {loses}")
    print(colors[1] + "O número sorteado é:" + colors[7], guess)
    print(colors[1] + "O dado sorteado é:" + colors[7], dice_roll)
    print()
    print(
        colors[0] + "Qual o número que somado com" + colors[7],
        dice_roll,
        colors[0] + "terá seu resultado final" + colors[7],
        guess,
        "?",
    )
    resposta = input("Resposta: ")

    try:
        if int(resposta) + dice_roll == guess:
            print(colors[5] + "Você acertou!")
            wins = wins + 1
            print(colors[5] + f"Score atual -> Acertos: {wins} Erros: {loses}")
            roll_the_dice_game()
        else:
            print(colors[5] + "Você errou!")
            loses = loses + 1
            print(colors[5] + f"Score atual -> Acertos: {wins} Erros: {loses}")
            print()
            try_again = input("Deseja tentar novamente?: S/N ")
            if try_again == "S" or try_again == "s":
                roll_the_dice_game()
            else:
                print()
                print(colors[5] + f"Score final -> Acertos: {wins} Erros: {loses}")
                print(colors[3] + "Você escolheu sair do jogo!")
                sys.exit()
    except ValueError:
        if resposta == "STOP" or resposta == "stop":
            print()
            print(colors[5] + f"Score final -> Acertos: {wins} Erros: {loses}")
            print(colors[3] + "Você escolheu sair do jogo!")
            sys.exit()
        else:
            print(colors[1] + "Apenas números são aceitos, gerando novos números...")
            roll_the_dice_game()


roll_the_dice_game()
