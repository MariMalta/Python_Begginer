km = float(input('km percorrido: '))
dias = int(input('dias ultilizado:'))

dias = 60 * dias
km = 0.15 * km

total = dias + km 

print(f'total a ser pago R$:{total: .2f}')