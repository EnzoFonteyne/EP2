from cria_baralho import cria_baralho
from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor


def possui_movimentos_possiveis(baralho):
    for i in range (len(baralho)):
        carta = baralho[i]
        valor = extrai_valor(carta)
        naipe = extrai_naipe(carta)
        if i > 2:
            carta3 = baralho[i-3]
            valor3 = extrai_valor(carta3)
            naipe3 = extrai_naipe(carta3)
            if valor == valor3 or naipe == naipe3:
                resultado = True
            
            carta1 = baralho[i-1]
            valor1 = extrai_valor(carta1)
            naipe1 = extrai_naipe(carta1)
            if valor == valor1 or naipe == naipe1:
                resultado = True
        elif i > 0:
            carta1 = baralho[i-1]
            valor1 = extrai_valor(carta1)
            naipe1 = extrai_naipe(carta1)
            if valor == valor1 or naipe == naipe1:
                resultado = True 
        else:
            resultado = False      
    
    return resultado