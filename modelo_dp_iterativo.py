# Dados
demanda = [4, 6, 3, 5, 8]
n = len(demanda)
custo_pedido = 2
custo_armazenamento = 1
custo_falta = 5
estoque_inicial = 5
max_estoque = 15

# dp[dia][estoque] = custo mínimo a partir desse estado
dp = [[float('inf')] * (max_estoque + 1) for _ in range(n + 1)]
dp[n] = [0] * (max_estoque + 1)

for dia in range(n - 1, -1, -1):
    for estoque in range(max_estoque + 1):
        for repor in range(0, 11):
            novo_estoque = estoque + repor - demanda[dia]
            novo_estoque = max(0, min(max_estoque, novo_estoque))

            custo = repor * custo_pedido
            if estoque + repor >= demanda[dia]:
                custo += novo_estoque * custo_armazenamento
            else:
                custo += abs(estoque + repor - demanda[dia]) * custo_falta

            dp[dia][estoque] = min(dp[dia][estoque], custo + dp[dia + 1][novo_estoque])

if __name__ == "__main__":
    print(f"Custo mínimo total (iterativo): {dp[0][estoque_inicial]}")
