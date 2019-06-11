print('Desafio 005')

n = int(input('Digite um número: '))

print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}.\n' .format(n, (n-1), (n+1)))

print('\n'*3)
print('*'*20)
print('\n'*3)

print('Desafio 006')

n = int(input('Digite um número: '))

print('o número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.\n' .format(n, (n*2), (n*3), (n**(1/2))))

print('\n')
print('*'*20)
print('\n')

print('Desafio 007')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('Nota 1: {:.1f}' .format(n1))
print('Nota 2: {:.1f}' .format(n2))
print('Média: {:.1f}' .format(((n1+n2)/2)))

print('\n')
print('*'*20)
print('\n')

print('Desafio 008')

m = int(input('Digite o metro: '))

print(f'Metros: {m}')
print('Centimetros: {}' .format((n*100)))
print('Milimetross: {}' .format((n*1000)))

print('\n')
print('*'*20)
print('\n')

print('Desafio 009')
print('Tabuada')

n = int(input('Digite um número: '))

print('{} * {} = {}' .format(n,1,(n*1)))
print('{} * {} = {}' .format(n,2,(n*2)))
print('{} * {} = {}' .format(n,3,(n*3)))
print('{} * {} = {}' .format(n,4,(n*4)))
print('{} * {} = {}' .format(n,5,(n*5)))
print('{} * {} = {}' .format(n,6,(n*6)))
print('{} * {} = {}' .format(n,7,(n*7)))
print('{} * {} = {}' .format(n,8,(n*8)))
print('{} * {} = {}' .format(n,9,(n*9)))
print('{} * {} = {}' .format(n,10,(n*10)))

print('\n')
print('*'*20)
print('\n')

print('Desafio 010')

valor = float(input('Digite quanto você possui em dinheiro: '))

dolar = 3.27

print('Você possui R${:.2f}, consegue comprar US${:.2f}'.format(valor,(valor/dolar)))


print('\n')
print('*'*20)
print('\n')



print('Desafio 011')

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

area = altura * largura

print(f'Sua parede tem a dimensão de {altura:.2f}x{largura:.2f} e sua área é de {area:.2f}m².')

tinta = area / 2

print(f'Para pintar esta área você precisará de {tinta}l de tinta.')

print('\n')
print('*'*20)
print('\n')

print('Desafio 012')

valor = float(input('Digite o valor do produto: '))

desc = valor - ((valor * 5)/100)

print(f'O valor do produto é R${valor:.2f} com 5% de desconto fica R${desc:.2f}')

print('\n')
print('*'*20)
print('\n')

print('Desafio 013')

valor = float(input('Digite o valor do salário atual: '))

acr = valor + ((valor * 15)/100)

print(f'Salário atual: R${valor:.2f}')
print(f'Novo salário: {acr:.2f}')