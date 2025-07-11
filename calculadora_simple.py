variable_A=float(input('indique el valor A:'))
variable_B=float(input('indique el valor B:'))
operacion=str(input('indique la operacion(+,-,/,*):'))
match operacion:
    case "+":
        resultado= variable_A+variable_B
        print(f'el resultado es {resultado}')
    case'-':
        resultado= variable_A-variable_B
        print(f'el resultado es {resultado}')
    case'*':
        resultado= variable_A*variable_B
        print(f'el resultado es {resultado}')
    case'/':
        resultado= variable_A/variable_B
        print(f'el resultado es {resultado}')
    case _: 
        print('no aplica ninguna operacion (+,-,/,*)')
    
