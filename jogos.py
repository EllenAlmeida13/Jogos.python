import forca
import adivinhacao

def escolhe_jogo():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("       Escolha o seu jogo!       ")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogoquinho tu quer jogar? "))

    if(jogo == 1):
        print("Jogando forca, escolhe esse que é legalzinho")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação, esocolhe esse nao porque nao gosto de adivinhar")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()