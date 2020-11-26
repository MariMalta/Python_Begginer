a = int(input('Valor 1: '))
b = int(input('Valor 2: '))

while True:

    r = a % b
    a = b
    b = r
    print(a)
    
    if ( b == 0):
        break



    
