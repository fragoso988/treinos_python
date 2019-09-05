from time import sleep

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

f = 0

while f != 5:
    print("""\nEscolha qual função quer executar:
    [1] Somar
    [2] Multiplicar
    [3] Subtrair
    [4] Novos números
    [5] Sair do programa\n""") 
    f=int(input("Digite a função: "))
    if f == 1:
        print("{} + {} = {}" .format(n1, n2, (n1+n2)))
    elif f == 2:
        print("{} * {} = {}" .format(n1, n2, (n1 * n2)))
    elif f == 3:
        print("{} - {} = {}" .format(n1, n2, (n1 - n2)))
    elif f ==4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif f == 0 or f > 5:
        print("Função incorreta, digite novamente!\n")
print("\nFinalizando...\n")
sleep(5)    
print("Programa encerrado.")
