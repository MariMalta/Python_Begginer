peso = float(input('Peso trazido hoje: '))

if(peso > 50):
    exece = peso - 50
    multa = exece * 4

    print(f'Seu excesso de {exece: .2f} quilos, entao sua multa é R${multa: .2f}')

else:
    exece = 0
    multa = 0
    print("Excesso de {exece} quilos, entao multa de R${multa} reais")

