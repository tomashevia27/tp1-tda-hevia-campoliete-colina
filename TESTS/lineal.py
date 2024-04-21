def encontrar_maximo(arr):
    valor_max = peso_max = 0
    for valor,peso, _ in arr:
        if valor>=valor_max and peso>=peso_max:
            valor_max=valor
            peso_max=peso

    return valor_max,peso_max 
