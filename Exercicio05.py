#
 
from Exercicio5ConstrutoresEfuncoes import Municipio,distribuirPopulacao,testeAutomatizado,entradaPeloUsuario
def Exercicio05Main():
    listaDeCidades = []
    x = 0

    escolhaRapida = int(input("Digite 0 para usar os testes automáticos e qualquer outro número para realizar as entradas: "))

    while(x < 10):
        
        if(escolhaRapida == 0):
            instanciaDeCidade = testeAutomatizado(x)
        else:
            instanciaDeCidade = entradaPeloUsuario()

        
        #1instanciaDeCidade = entradaPeloUsuario ()
        print(f'\n**********************************************************************')    
        print(f'\n Na cidade de: {instanciaDeCidade.nome}')    
        print(f'\nO número de votos total é: {instanciaDeCidade.totalDeVotos}')    
        print(f'\nO número de votos em branco é: {instanciaDeCidade.votosEmBranco}')
        print(f'\nO número de votos nulos é: {instanciaDeCidade.votosNulos}')
        print(f'\nO número de votos válidos é: {instanciaDeCidade.votosValidos}')
        print(f'\n A porcentagem de votos brancos: {instanciaDeCidade.porcentagemDeVotosEmBranco:.2f} %')
        print(f'\n A porcentagem de votos nulos: {instanciaDeCidade.porcentagemDeVotosNulos:.2f} %')
        print(f'\n A porcentagem de votos válidos: {instanciaDeCidade.porcentagemDeVotosValidos:.2f} %')
        print(f'\n**********************************************************************')
        listaDeCidades.append(instanciaDeCidade)
        x += 1

        cidadeComMaisVotosTotais = max(listaDeCidades,key=lambda x: x.totalDeVotos)

    print(f'**********************************************************************')
    print(f'A cidade com mais eleitores é: {cidadeComMaisVotosTotais.nome} \n ')
    print(f'A quantidade total de votos é: {cidadeComMaisVotosTotais.totalDeVotos} \n ')
    print(f'\n**********************************************************************')


    cidadeComMaisVotosValidos = max(listaDeCidades,key=lambda x: x.votosValidos)
    print(f'**********************************************************************')
    print(f'A cidade com mais votos válidos é: {cidadeComMaisVotosValidos.nome} \n ')
    print(f'A quantidade total de votos é: {cidadeComMaisVotosValidos.votosValidos} \n ')
    print(f'Que equivale a:   {cidadeComMaisVotosValidos.porcentagemDeVotosValidos:.2f} % \n ')
    print(f'\n**********************************************************************')

    cidadeComMaisVotosNulos = max(listaDeCidades,key=lambda x: x.votosNulos)
    print(f'**********************************************************************')
    print(f'A cidade com mais votos Nulos é {cidadeComMaisVotosNulos.nome} \n ')
    print(f'A quantidade total de votos Nulos é: {cidadeComMaisVotosNulos.votosNulos} \n ')
    print(f'Que equivale a:   {cidadeComMaisVotosNulos.porcentagemDeVotosNulos:.2f}  % \n ')
    print(f'\n**********************************************************************')


    cidadeComMaisVotosEmBranco = max(listaDeCidades,key=lambda x: x.votosEmBranco)
    print(f'**********************************************************************')
    print(f'A cidade com mais votos em Branco é: {cidadeComMaisVotosEmBranco.nome} \n ')
    print(f'A quantidade total de votos é: {cidadeComMaisVotosEmBranco.votosEmBranco} \n ')
    print(f'Que equivale a:   {cidadeComMaisVotosEmBranco.porcentagemDeVotosEmBranco:.2f}  % \n ')
    print(f'\n**********************************************************************')


    
    
    

