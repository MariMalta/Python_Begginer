a = float(input('lado 1: '))
b = float(input('lado 2: '))
c = float(input('lado 3 '))

if(a > b + c or b > a + c or c > a + b):
    print('Não pode ser um triangulo')

else:
    if(a == b == c):
        print('triangulo equilatero')

    if(a == b or b == c or c == a):
        print('triangulo isosceles')

    else: 
        print('triangulo escaleno')
