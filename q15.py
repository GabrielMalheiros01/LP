qtd = float(input("Digite o valor da sua hora:"))
horas = float(input("Digite o número de horas trabalhadas no mês:"))
total = qtd*horas
liq = ((total - ((11*total)/100))-((8*total)/100)-((5*total)/100))

print("Nesse mês seu salário bruto foi de::",total)
print("Nesse mês vc pagou ao INSS:",(8*total)/100)
print("Nesse mês vc pagou ao sindicato:",(5*total)/100)
print("Nesse mês seu salário liquido foi de::",liq)
