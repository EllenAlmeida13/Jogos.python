def jogar():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("***Bem vindX ao jogo da Forca!***")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    palavra_secreta = "banana"

    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    #letras_faltando = str(letras_acertadas.count("_"))

    enforcou = False
    acertou = False


    # enquanto 
    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                #print('Ainda faltam acertar {} letras'.format(letras_faltando))
                #print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        #print("jogando..")
        print(letras_acertadas)

    print("Acabou o joguinho")

if(__name__ == "__main__"):
    jogar()
