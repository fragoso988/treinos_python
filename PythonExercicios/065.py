print("""Exercício Python 065: 
Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.""")

n = int(input("Digite um número: "))
cont_media = n
maior = n
menor = n
cont = 1
continuar = 0
while continuar != 'N':
    continuar = input("Deseja continuar?[S/N]: ").upper()

    if continuar not in ['N','S']:
        print("Opção inválida, digite novamente!")
    if continuar == 'S':
        n = int(input("Digite um número: "))
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        cont_media = cont_media + n
        cont = cont + 1
    

media = cont_media/cont
print("Você digitou {} números, a média deles é {}." .format(cont,media))
print("O maior número digitado foi {} e o menor {}" .format(maior,menor))


