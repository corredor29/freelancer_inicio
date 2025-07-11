variableA=str(input('1 2 3 piedra papel o tijera jugador 1'))
variableB=str(input('1 2 3 piedra papel o tijera jugador 2'))
if (variableA==variableB):
    print('empate')
elif ((variableA=='tijera' and variableB=='piedra') or (variableA=='piedra' and variableB=='papel') or (variableA=='papel' and variableB=='tijera')):
    print (f'gana variableB')
else: 
    print(f'gana variableA')