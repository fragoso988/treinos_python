from math import factorial
print("Fatorial")
n = int(input("Digite um número: "))
c = n
while c > 0:
    print('{} '.format(c), end ='')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1
print(factorial(n))

print("\n\n\nAgora com o For\n\n\n")

f= 0
for f in range(n,1, -1):
    print('{} '.format(f), end ='')
    print(' x ' if f > 1 else ' = ', end = '')
    f -= 1
print(factorial(n))


