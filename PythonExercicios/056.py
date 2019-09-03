print("Desafio 056")

pess = 0
maior_idade = 0
soma_idade = 0
cont_f = 0

for i in range(1, 5):
    print('\n')
    nome = input("Digite o nome da {}º pessoa: " .format(i))
    idade = int(input("Idade: "))
    sexo = input("Sexo[M/F]: ")
    sexo = sexo.upper()
    soma_idade = soma_idade + idade

    if (sexo == 'M' and idade > maior_idade):
        maior_idade = idade
        nome_maior_idade = nome
    if (sexo == 'F' and idade < 20):
        cont_f = cont_f + 1

media_idade = soma_idade/4

print("\nA média de idades é {}." .format(media_idade))
print("A maior idade de um homem é {} e seu nome é {}." .format(maior_idade, nome_maior_idade))
print("O número de mulheres com menos de 20 anos é {}" .format(cont_f))

