n = int(input('n: '))
k = 1

while(k * (k + 1) * (k + 2) < n):
    k += 1

if( k * (k + 1) * (k + 2) == n):
    print('numero triangular')
else:
    print('nao e triangular')
