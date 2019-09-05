print("Progressão aritmérica")

t= int(input("\nDigite o 1º termo: "))
r= int(input("Digite a razão: "))

print(t, end=" -> ")
p = 0
while p < 9:
    t += r
    print(t, end='')
    print(" -> ", end='')
    p += 1
print("FIM")
