import random
from time import sleep

print("""********JO KÊN PO DOS INFERNO**************
******Escolha uma das opçoes abaixo:*******
=-=-=-=-=-=-=-=PEDRA=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-=PAPEL=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-TESOURA=-=-=-=-=-=-=-=-=-=-=-""")

player = input("\n\n\nDigite a opção escolhida: ")
player = player.upper()

options = ['PEDRA', 'PAPEL', 'TESOURA']

npc = random.choice(options)

print("\nIniciando a partida...")

print("\nJO KEN PO")
sleep(6)

print("\n\nVocê jogou {} o adversário jogou {}." .format(player, npc))

if(player == 'PEDRA' and npc == 'TESOURA' or player == 'TESOURA' and npc == 'PAPEL' or player == 'PAPEL' and npc == 'PEDRA'):
    print("\nVOCÊ VENCEU!")
elif(npc == 'PEDRA' and player == 'TESOURA' or npc == 'TESOURA' and player == 'PAPEL' or npc == 'PAPEL' and player == 'PEDRA'):
    print("\nVOCÊ PERDEU!")
elif(player == npc):
    print("\nEMPATE!")
else:
    print("\nJogada inválida. Leia o enunciado, pelo amor de dels!!!")