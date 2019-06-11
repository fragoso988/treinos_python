
horas = float(input("Digite o número de horas trabalhadas: "))
valor = float(input("Digite o valor da hora: "))

sbruto = horas * valor

ir = sbruto * 0.11

inss = sbruto * 0.08

sindicato = sbruto * 0.05

sliquido = sbruto - ir - inss - sindicato

print("Salário Bruto: +R${}" .format(sbruto))
print("IR (11%): -R${}" .format(ir))
print("INSS (8%): -R${}" .format(inss))
print("Sindicato (5%): -R${} " .format(sindicato))
print("Salário Liquido: =R${}" .format(sliquido))

