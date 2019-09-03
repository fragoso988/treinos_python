print(""" ***Desafio 022***
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiusculas;
-O nome com todas minúsculas;
-Quantas letras ao todo(sem considerar espaço);
-Quantas letras tem o primeiro nome.
""")

nome = str(input("Digite seu nome completo: ")).strip()

print("Nome  maisculo: {}" .format(nome.upper()))

print("Nome minusculo {}" .format(nome.lower()))

primeiro_nome = nome.split()

print("Quantidade de letras: {}" .format(len(nome) - nome.count(' ')))

print("Número de letras do primeiro nome: {}" .format(len((primeiro_nome[0]))))

print("""\nDesafio 023
    Faça um programa que leia um número de 0 a 9999 e mostre na tle acada um dos códigos separados.""")


num = int(input("DIgite um número de 1 a 9999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Vamos analisar o número{num}.")
print(f"Unidade: {u}.")
print(f"Dezena: {d}.")
print(f"Centena: {c}.")
print(f"Milhar: {m}.")
    

print("""\nDesafio 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
""")

cidade = input("Digite o nome da cidade: ").strip().upper()

if (cidade[:5] == 'SANTO'):
    print("Sua cidade começa com nome de SANTO: {}" .format(cidade.capitalize()))
else:
    print("Sua cidade não começa com nome de SANTO: {}" .format(cidade.capitalize())) 

print("""\nDesafio 025
    Crie um programa que leia um nome e diga que se há SILVA nele.
    """)

nome = input("Digite um nome: ")

if (nome.upper().find('SILVA') >= 0):
    print("Este nome possui SILVA. {}" .format(nome.capitalize()))
else:
    print("Este nome não há SILVA. {}" .format(nome.capitalize()))    

print("""\nDesafio 026
    Faça um programa que leia uma frase pelo teclado e mostre:
    -Quanas vezes aparece a letra "A";
    -Em que posicção ela aparece a primeira vez;
    -Em que posição ela aparece a ultima vez.
    """)

frase = input("Digite uma frase: ").strip().upper()

print("A letra 'A' apareceu {} vezes" .format(frase.count('A'))) 
print("A letra 'A' apareceu pela primeira vez na posição {}." .format(frase.find('A')))
print("A letra 'A' apareceu pela ultima vez na posição {}." .format(frase.rfind('A')))

print("""
Desafio 027

Faça um programa que leia o nome completo da pessoa e mostre o primeiro e ultimo nome.
""")

nome = input("Digite seu nome completo: ")
nome_split= nome.split()

print(f"\nO primeiro nome é {nome}")
print("Primeiro nome é {}" .format(nome_split[0]))
print("O último nome é {}" .format(nome_split[-1]))

