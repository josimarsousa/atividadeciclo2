num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))
num3 = int(input('Digite o numero 3: '))

if(num1 < num2 & num3):
    menor = num1
    print('O menor número é: ',menor)
    exit()
if(num2 < num1 & num3):
    menor = num2
    print('O menor número é: ', menor)
    exit()
if(num3 < num1 & num2):
    menor = num3
    print('O menor número é: ', menor)
    exit()




