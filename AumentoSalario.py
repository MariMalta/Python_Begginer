sal = float(input('Salario:'))
aum = float(input('Porcentagem do aumento:'))

NovoSal =  (sal * aum/100) + sal

print(f'Novo Salario R$: {NovoSal}')
