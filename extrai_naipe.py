def extrai_naipe(carta):
    resultado = carta[1]
    if carta[0] == '1':
        resultado = carta[2]
    return resultado