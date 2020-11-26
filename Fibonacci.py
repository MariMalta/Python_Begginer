n = int(input('n: '))
i = 1
j = 2

if( n == 1 or n == 2):
    print('Numero de fibonacci = 1')

while( n > 2):

    v = i + j

    aux = v
    i = j
    j = aux

    n -= 1

print(f'Seu valor de Fibonacci é {v}')
     
