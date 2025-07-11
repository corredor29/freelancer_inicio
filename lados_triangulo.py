lado1= float(input('ingrese el lado 1'))
lado2= float(input('ingrese el lado 2'))
lado3=float(input('ingrese el lado 3'))
if (lado1==lado2 and lado2==lado3 and lado3==lado1):
    print('es equilatero')
elif (lado1!=lado2 and lado2!=lado3 and lado1!=lado3):
    print('es escaleno')
else:
    print('es isoceles')