variable_A=float(input('indique el valor A:'))
variable_B=float(input('indique el valor B:'))
operacion=str(input('indique la operacion(+,-,/,*,p,n-p,m-i):'))

def sumar(a,b):
    print(f'el resultado es {a+b}')

def restar(a,b):
    print(f'el resultado es {a-b}')

def dividir(a,b):
    print(f'el resultado es {a/b}')

def multiplicar(a,b):
    print(f'el resultado es {a*b}')

def par_o_impar(a):
    residuo=a%2
    if (residuo==0):
        print('es par')
    else:
        print('es impar')
        
def positivo_o_negativo_0(a):
    if (a<0):
        print('es negativo')
    elif(a>0):
        print('es positivo')
    else:
        print('es cero')
def mayor_igual(a,b):
    if (a>b):
        print('la variable A es mayor')
    elif(a==b):
        print('son iguales')
    else:
        print('la variable b es mayor')

match operacion:
    case '+':
        sumar(variable_A,variable_B)
    case '-':
        restar(variable_A,variable_B)
    case '/':
        dividir(variable_A,variable_B)
    case '*':
        multiplicar(variable_A,variable_B)
    case'p':
        par_o_impar(variable_A)
    case'n-p':
        positivo_o_negativo_0(variable_A)
    case'm-i':
        mayor_igual(variable_A,variable_B)
    case _: 
        print('no aplica ninguna operacion (+,-,/,*,p,n-p,m-i)')
    
    

