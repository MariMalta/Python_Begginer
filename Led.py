N = int(input())

for a in range(N):
    
    v = str(input())
    i = 0
    
    leds = {'0':6, '6':6, '9':6, '1':2, '2':5, '3':5, '5': 5, '4':4, '7': 3, '8':7}
    
    for x in v:
        
        i += leds.get(x,0)
        
    print(i, "leds")