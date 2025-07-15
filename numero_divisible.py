entero=int(input('digite el numero entero'))
divisible2=entero%2
divisible3=entero%3
if(divisible2==0 and divisible3==0):
    print('es divisible por 2 y 3')
elif(divisible2==0 and divisible3!=0):
    print('es divisible solo por 2')
elif(divisible2!=0 and divisible3==0):
    print('es divisible solo por 3')
else:
    print('no es divisible ni por 2 ni por 3')
