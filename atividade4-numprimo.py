def numprimo(numero):
    i = 1
    somaresto = 0
    while(i<=numero):
        calculo = numero/i
        resto = int(numero%i)
        if(resto >= 1):
            resto=1
            somaresto = somaresto + 1
        i += 1
    if numero-somaresto==2:
        print('O número', numero, 'é primo')
    else:
        print('O número', numero, 'não é primo.')


primo = int(input('Digite um numero:'))
numprimo(primo)





