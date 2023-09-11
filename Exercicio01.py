def imprimirNumerosAnterioresPosteriores():
    numero = int(input("Digite o número desejado: "))
    numerosAnteriores = []
    numerosPosteriores = []

    i = numero - 50
    while i < numero:
        numerosAnteriores.append(i)
        i += 1
       

    i = numero + 1
    while i < numero + 51:
        numerosPosteriores.append(i)
        i += 1

    print(f'\n Os números anteriores são:{numerosAnteriores} \n')
    print(f'O número digitado foi: {numero} \n')
    print(f'Os números posteriores são:{numerosPosteriores} \n')


