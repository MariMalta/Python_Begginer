x = float(input('Metros quadrados a ser pintado: '))

if (x % 54 == 0):
    latas = x / 54
else:
    latas = int(x /54) + 1

total = latas * 80

print(f'Usar {latas} latas e vai custar R$ {total: .2f}')



    

