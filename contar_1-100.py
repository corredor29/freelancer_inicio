def pares_1_100():
    for i in range(1,100):
        residuo=i%2
        if(residuo==0):
            print(i)
            
def suma_1_10():
    numeros=1,2,3,4,5,6,7,8,9,10
    suma=0
    for i in numeros:
        suma=i+suma 
    print(suma)

def piramide_asteriscos(n):
    for i in range(n+1):
        for p in range(i):
            print('*', end='')
        print('')
    
piramide_asteriscos(5)
