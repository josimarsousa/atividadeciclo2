# -*- coding: latin1 -*-

a = int(input("Digite o valor da a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

#verifica a condicao de a
condicao = a >(b+c)

if(condicao == False):
    if (a != b) &( a != c) & (b != c):
        print('Este � um triangulo escaleno')
        calces = (b*c)/2
        print('Sua �rea �: ', calces)
    if (a == b) | (a == c) | (b == c):
        print('Este triangulo � isosceles')
        calcis = (b*c)/2
        print('Sua �rea �: ', calcis)
    if(a == b) & (a == c) & ( b == c):
        print('Este triangulo � equilatero')
        calceq = (b*c)/2
        print('Sua �rea �: ', calceq)
else:#se a for maior que b+c entao nao � um triangulo
    print('nao forma triangulo algum')
    print('valores digitados:',a,',',b,',',c, 'onde b + c s�o menores que a.')
