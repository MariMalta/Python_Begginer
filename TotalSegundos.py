d = int(input('dias: '))
h = int(input('horas: '))
m = int(input('minutos: '))
s = int(input('segundos: '))

d = d*24*60*60 
h = h*60*60 
m = m*60

total_segundos = d + h + m + s


print (f'{total_segundos} segundos')