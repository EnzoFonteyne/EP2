#Precisa importar as outras funções antes de rodar
from cria_baralho import cria_baralho
from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor

def lista_movimentos_possiveis(baralho, posicao):
    carta = baralho[posicao]
    naipe = extrai_naipe(carta)
    valor = extrai_valor(carta)
    movimentos = []
    if posicao > 2:
        movimento3 = baralho[posicao - 3]
        naipe3 = extrai_naipe(movimento3)
        valor3 = extrai_valor(movimento3)
        if naipe == naipe3 or valor == valor3:
            movimentos.append(3)
        
        movimento1 =  baralho[posicao - 1]
        naipe1 = extrai_naipe(movimento1)
        valor1 = extrai_valor(movimento1)
        if naipe == naipe1 or valor == valor1:
            movimentos.append(1)

    elif posicao > 0:
        movimento1 =  baralho[posicao - 1]
        naipe1 = extrai_naipe(movimento1)
        valor1 = extrai_valor(movimento1)
        if naipe == naipe1 or valor == valor1:
            movimentos.append(1)
    else:
        movimentos = []
    return movimentos
    