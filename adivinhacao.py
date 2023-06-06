import random

def jogar():
    print(50* '*')
    print("***Bem vindo no jogo de adivinhação!!!***")
    print(50* '*')

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    rodadas = 1
    pontos = 1000

    print("Por favor, escolha um nivel de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Definir nivel: "))

    if(dificuldade == 1):
        tentativas = 20
    elif(dificuldade == 2):
        tentativas = 10
    elif(dificuldade == 3):
        tentativas = 5
    else:
        print("Digite uma opção valida!!!")

    while(rodadas <= tentativas):
        print("Tentativas: {} de {}".format(rodadas, tentativas))
        chute_str = input("Digite um numero: ")

        chute = int(chute_str)

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Na mosca, Você acertou e fez {}!!!".format(pontos))
            break
        else:
            if(chute_maior):
                print("Seu chute foi maior que o numero secreto, tente novamente! ")
            elif(chute_menor):
                print("Seu chute foi menor que o numero secreto, tente novamente! ")    
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodadas = rodadas + 1


        


    print("Fim do Jogo")
    if tentativas == tentativas:
        print("O numero secreto era {}".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()