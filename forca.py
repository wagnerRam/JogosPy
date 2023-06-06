def jogar():
    print(50* '*')
    print('***Bem Vindo ao Jogo da Forca!!!***')
    print(50* '*')

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei {} na posição {}". format(letra, index))
            index = index + 1
        print("Jogando ...")
        

    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()
