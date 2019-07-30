print("""Desafio 049
Tabuada""")

n = int(input("Digite o valor: "))

for c in range(0, 11):
    print(" {} x {:2} = {}" .format(n, c, (n*c)))