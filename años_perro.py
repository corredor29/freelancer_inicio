edad_perro=int(input('ingrese la edad del perro'))
if (edad_perro<=2 and edad_perro>0):
    resultado=edad_perro*10.5
    print(f'la edad del perro es {resultado} ')
elif (edad_perro>=3):
    resultado=((edad_perro-2)*4)+21
    
    print(f'la edad del perro es {resultado}')
else:
    print('coloque una edad valida del perro ')