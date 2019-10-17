print("""Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. \n\n\n""")

maior = 0
homem = 0
m20 = 0
while True:
    print('~'*30)
    print("CADASTRE UMA PESSOA")
    print('~'*30)

    sexo = input("Sexo[M/F]: ").upper()
    idade = int(input("Idade: "))

    if idade > 18:
        maior = maior + 1
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade < 20:
        m20 = m20 + 1
    print('~'*30)
    next = input("Quer continuar?[S/N]: ").upper()
    if next == 'N':
        break
print(f"Pessoas maiores de 18 anos: {maior}")
print(f"Homens: {homem}")
print(f"Mulheres menores de 20 anos: {m20}")