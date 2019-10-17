from random import randint

print("""Exercício Python 068: 
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. \n\n\n\n\n""")

cont = 0
while True:
    print("~"*30)
    vcn = int(input("Digite um número: "))
    vc = input("Par ou Ímpar?[P/I]: ").upper()
    print("~"*30)

    npc = randint(1, 10)
    valor = npc + vcn
    if ((valor % 2) == 0):
        print("VocÊ jogou {}, o computador {}, total é de {}, DEU PAR" .format(vcn, npc, valor))
        resultado = 'P'
    else:
        print("VocÊ jogou {}, o computador {}, total é de {}, DEU ÍMPAR".format(vcn, npc, valor))
        resultado = 'I'
    if vc == resultado:
        print("Você venceu!\nVamos jogar novamente...")
        cont = cont + 1
    else:
        print("Você perdeu!")
        break
print("~" * 30)
print("Game Over!! Você foi derrotado após {} vitórias" .format(cont))

