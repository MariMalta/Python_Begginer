a,b,c = map(int,input().split(' '))

maiorAB = (a + b + abs(a-b)) / 2

maiorAB = int(maiorAB)

if c >= maiorAB:
    print(f'{c} eh o maior')
    
else:
    print(f'{maiorAB} eh o maior')
