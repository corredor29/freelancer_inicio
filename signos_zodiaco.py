mes=int(input('ingrese el mes'))
dia=int(input('ingrese el dia'))
if ((mes==3 and dia >=21) or (mes==4 and dia<=19)):
    print('tu signo es aries')
elif(mes==4 and dia>=20) or (mes==5 and dia<=20):
    print('tu signo es tauro')
elif(mes==5 and dia>=21) or (mes==6 and dia<=20):
    print('tu signo es gemenis')
elif(mes==6 and dia>=21) or (mes==7 and dia<=22):
    print('cancer')
elif(mes==7 and dia>=23) or (mes==8 and dia<=22):
    print('tu signo es leo')
elif(mes==8 and dia>=23) or (mes==9 and dia<=22):
    print('tu signo es virgo')
elif(mes==9 and dia>=23) or (mes==10 and dia<=22):
    print(' tu signo es libra')
elif(mes==10 and dia>=23) or (mes==11 and dia<=21):
    print('tu signo es escorpio')
elif(mes==11 and dia>=22) or (mes==12 and dia<=21):
    print('tu signo es sagitario')
elif(mes==12 and dia>=22) or (mes==1 and dia<=19):
    print('tu signo es capricornio')
elif(mes==1 and dia>=20) or (mes==2 and dia<=18):
    print('tu signo es acuario')
elif(mes==2 and dia>=19) or (mes==3 and dia<=20):
    print('tu signo es pircis')
else: 
    print('El dia o mes son incorrectos')