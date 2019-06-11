
n1 = float(input("Digite a primeira nota: "))

n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print("Sua média é {}" .format(media))

if(9 >= media >= 7):
    print("Aprovado")
elif(media == 10):
    print("Aprovado com Distinção")
else:
    print("Reprovado")

