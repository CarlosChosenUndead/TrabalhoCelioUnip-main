import random
def menorNumeroDecimal ():
    n1 = int(input("Digite o número desejado: "))
    n2 = int(input("Digite o número desejado: "))
    n3 = int(input("Digite o número desejado: "))
    if ((n1<n2) and (n2 < n3)):
        print(f'O menor número é: {n1} ')
    else:
        if(n2 < n3) :
            print(f'O menor número é: {n2} ')
        else:
            print(f'O menor número é: {n3} ')
    print(n1,n2,n3)

