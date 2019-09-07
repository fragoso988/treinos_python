print("Progressão aritmérica")

t= int(input("\nDigite o 1º termo: "))
r= int(input("Digite a razão: "))

print(t, end=" -> ")
p = 0
x = 9
while p < x:
    t += r
    print(t, end='')
    print(" -> ", end='')
    p += 1
    if (p == x):
        print("PAUSA")
        xx = int(input("\nQuantos termos você quer mostrar a mais? "))
        x = x + xx
print("\nProgressão finalizada com {} termos mostrados." .format(x))
    
