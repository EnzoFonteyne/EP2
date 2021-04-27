def empilha(baralho, origem, destino):
    origem1 = baralho[origem]
    detino1 = baralho[destino]
    baralho[destino] = origem1
    del baralho[origem]
    return baralho