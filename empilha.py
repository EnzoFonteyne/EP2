def empilha(baralho, origem, destino):
    origem1 = baralho[origem]
    baralho[destino] = origem1
    del baralho[origem]
    return baralho