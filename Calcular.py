valor = float(input('Valor por hrs trabalhadas: '))
hrs = int(input('Numero de hrs trabalhadas: '))

sb = valor * hrs
ir = sb * 11/100
inss = sb * 8/100
sin = sb * 5/100
sl = sb - ir - inss - sin

print(f'Salario bruto = {sb: .2f}')
print(f'Importo de renda = {ir: .2f}')
print(f'INSS = {inss: .2f}')
print(f'Sindicado = {sin: .2f}')
print(f'Salario Liquido = {sl: .2f}')





