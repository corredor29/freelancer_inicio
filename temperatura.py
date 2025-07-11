temperatura=float(input('ingrese la temperatura'))
unidad=str(input('ingrese la temperatura (celsius)(fahrenheit)'))
match unidad:
    case 'celsius':
        resultado=(temperatura*9/5) +32
        print((f'el resultado es {resultado}'))
    case 'fahrenheit':
        resultado=(temperatura-32) *5/9
        print((f'el resultado es {resultado}'))
    case _:
        print('ingrese una unidad valida (celsius o fahrenheit)')