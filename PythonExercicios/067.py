print("""Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. \n\n""")

while True:
    print("~"*40)
    n = int(input("Quer ver a tabuada de qual número? "))
    print("~"*40)
    if n < 0:
        break
    for i in range(1, 11):
        print("{} x {} = {}" .format(n, i, (n*i)))
print("\n Tabuada encerrada")