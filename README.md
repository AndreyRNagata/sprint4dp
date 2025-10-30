# 🧮 Dynamic Programming - Modelo de Reposição de Estoque

## 📖 Contexto do Problema

Nas unidades de diagnóstico, o consumo diário de insumos (reagentes e descartáveis) não é registrado com precisão, o que dificulta o controle de estoque e a previsão de reposição.  
Dessa forma, podem ocorrer **faltas de materiais** ou **desperdícios** devido a excesso de produtos armazenados.

O objetivo deste projeto é **modelar o processo de reposição de estoque usando Programação Dinâmica (Dynamic Programming)**, propondo uma solução que minimize o custo total de operação, considerando custos de pedido, armazenamento e falta de insumo.

---

## 🧩 Formulação do Problema

Cada dia representa um **estado** do sistema. O gestor deve decidir **quanto repor** de insumo para atender à demanda do dia, minimizando custos ao longo de um período de `n` dias.

### **Elementos do Modelo**

| Elemento | Descrição |
|-----------|------------|
| **Estado** | `(dia, estoque)` → representa o dia atual e o nível de estoque disponível. |
| **Decisão** | Quantidade de insumo a **repor** no início do dia. |
| **Transição** | `novo_estoque = estoque + repor - demanda[dia]` |
| **Função Objetivo** | Minimizar o custo total de operação. |

### **Custos Considerados**

- **Custo de Pedido:** custo fixo por unidade reposta.  
- **Custo de Armazenamento:** custo por unidade que sobra no estoque ao final do dia.  
- **Custo de Falta:** custo por unidade não atendida da demanda.

A função de custo pode ser descrita como:

\[
Custo_{total} = Custo_{pedido} + Custo_{armazenamento} + Custo_{falta}
\]

O objetivo é encontrar a política de reposição que **minimize o custo total** ao longo de `n` dias.

---

## ⚙️ Estruturas e Algoritmos Utilizados

### 🧠 1. **Versão Recursiva com Memorização (Top-Down)**

**Arquivo:** `modelo_dp.py`

A função principal é definida como:

```python
@lru_cache(maxsize=None)
def dp(dia, estoque):
    if dia == n:
        return 0
````

* A linha `@lru_cache(maxsize=None)` aplica **memorização automática**, guardando resultados já calculados.
* O estado `(dia, estoque)` define a subestrutura ótima do problema.

O laço principal testa todas as quantidades de reposição possíveis:

```python
for repor in range(0, 11):
    novo_estoque = estoque + repor - demanda[dia]
```

Aqui, `repor` é a **decisão** que o gestor toma.
Para cada decisão, o código calcula o **novo estado** (`novo_estoque`) e o **custo associado**:

```python
custo = repor * custo_pedido
if novo_estoque >= 0:
    custo += novo_estoque * custo_armazenamento
else:
    custo += abs(novo_estoque) * custo_falta
```

Por fim, o custo total daquele caminho é avaliado com uma chamada recursiva:

```python
total = custo + dp(dia + 1, max(0, novo_estoque))
melhor = min(melhor, total)
```

Esse trecho implementa a **função objetivo** de minimizar o custo total, armazenando o menor custo obtido entre todas as opções possíveis.

📈 **Vantagens:**

* Clareza conceitual.
* Simples de implementar e entender.

📉 **Desvantagens:**

* Pode atingir o limite de recursão para grandes horizontes de tempo.

---

### ⚙️ 2. **Versão Iterativa (Bottom-Up)**

**Arquivo:** `modelo_dp_iterativo.py`

Nesta versão, o problema é resolvido **de trás para frente**, preenchendo uma tabela `dp` que guarda o custo mínimo para cada estado.

Inicialização da tabela:

```python
dp = [[float('inf')] * (max_estoque + 1) for _ in range(n + 1)]
dp[n] = [0] * (max_estoque + 1)
```

Aqui, `dp[dia][estoque]` representa o **custo mínimo** a partir do dia e estoque indicados.
A última linha (`dp[n]`) é inicializada com `0`, pois não há custos após o último dia.

O cálculo iterativo segue:

```python
for dia in range(n - 1, -1, -1):
    for estoque in range(max_estoque + 1):
        for repor in range(0, 11):
```

Esses laços simulam **todas as combinações possíveis de dia, estoque e decisão**.
A atualização do custo é feita da mesma forma que na recursiva:

```python
novo_estoque = estoque + repor - demanda[dia]
novo_estoque = max(0, min(max_estoque, novo_estoque))
custo = repor * custo_pedido
if estoque + repor >= demanda[dia]:
    custo += novo_estoque * custo_armazenamento
else:
    custo += abs(estoque + repor - demanda[dia]) * custo_falta

dp[dia][estoque] = min(dp[dia][estoque], custo + dp[dia + 1][novo_estoque])
```

📈 **Vantagens:**

* Elimina chamadas recursivas.
* Ideal para conjuntos de dados grandes.

📉 **Desvantagens:**

* Ocupa mais memória (tabela completa de estados).

---

### 🔍 3. **Comparação das Duas Versões**

**Arquivo:** `main.py`

O código principal executa as duas abordagens e compara seus resultados:

```python
resultado_topdown = dp(0, estoque_inicial)
resultado_bottomup = dp_iterativo[0][estoque_inicial]
```

Após calcular ambos, o programa verifica se produzem o mesmo valor ótimo:

```python
if resultado_topdown == resultado_bottomup:
    print("✅ Ambos os métodos produzem o mesmo resultado.")
else:
    print("⚠️ Resultados diferentes!")
```

Esse passo é essencial para **validar a corretude do modelo de Programação Dinâmica**.

---

## 🧾 Execução

```bash
python main.py
```

### Saída esperada:

```
=== COMPARAÇÃO ===
Recursivo (Top-Down): 49
Iterativo (Bottom-Up): 49
✅ Ambos os métodos produzem o mesmo resultado.
```

---

## 📊 Conclusão

Este projeto mostra como a **Programação Dinâmica** pode ser usada para otimizar a reposição de estoque em unidades laboratoriais.
A formulação do problema permite que o sistema encontre automaticamente a melhor política de reposição, equilibrando custos de compra, armazenamento e falta.

Ambas as versões — **Top-Down e Bottom-Up** — foram implementadas e **produzem o mesmo resultado ótimo**, confirmando a validade do modelo.

---
