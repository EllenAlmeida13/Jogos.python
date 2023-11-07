import random

def jogar():

    print("---------------------------------")
    print("Bem vind ao jogo de Adivinhação!")
    print("---------------------------------")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000


    print("Qual nível tu quer jogar?")
    print("(1) Fazinho (2) Meio fazinho (3) Dificizinho")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 30
    elif(nivel == 2):
        total_de_tentativas = 15
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errouuuuuuu! O seu chute foi mais alto que o número secreto.")
            elif(menor):
                print("Você errouuuuuu! toma um suquinho porque o seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Acabouuuuu")

if(__name__ == "__main__"):
    jogar()
