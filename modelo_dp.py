from functools import lru_cache

# Dados de exemplo
demanda = [4, 6, 3, 5, 8]   # demanda diária de insumos
n = len(demanda)

# Custos
custo_pedido = 2
custo_armazenamento = 1
custo_falta = 5
estoque_inicial = 5

@lru_cache(maxsize=None)
def dp(dia, estoque):
    if dia == n:
        return 0

    melhor = float('inf')

    for repor in range(0, 11):
        novo_estoque = estoque + repor - demanda[dia]
        custo = repor * custo_pedido

        if novo_estoque >= 0:
            custo += novo_estoque * custo_armazenamento
        else:
            custo += abs(novo_estoque) * custo_falta

        total = custo + dp(dia + 1, max(0, novo_estoque))
        melhor = min(melhor, total)

    return melhor


if __name__ == "__main__":
    resultado = dp(0, estoque_inicial)
    print(f"Custo mínimo total (recursivo): {resultado}")
