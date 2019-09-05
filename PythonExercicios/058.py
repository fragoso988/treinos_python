from random import randint

sorteio = randint(1,10)

jogo = int(input("Digite um número de 1 a 10: "))
tentativa = 0
while jogo != sorteio:
    jogo = int(input("Valor errado, tente novamente: "))
    tentativa = tentativa +1
print("\nNa {} tentativa você acertou!" .format(tentativa))