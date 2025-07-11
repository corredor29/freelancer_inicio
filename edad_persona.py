edad=int(input('indique la edad de la persona:'))
if (edad >=0 and edad <=12):
    print("es niño ")
elif (edad>=13 and edad <=17):
    print('es adolescente')
elif (edad >=18 and edad <=59):
    print('es adulto')
else: 
    print( 'es mayor de edad')
