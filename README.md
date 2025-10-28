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

A abordagem recursiva define a função `dp(dia, estoque)` como o custo mínimo a partir de um estado.  
A cada chamada, a função avalia todas as possíveis quantidades de reposição (`repor`), calcula o custo associado e escolhe a opção com menor custo total.

A **Programação Dinâmica** é aplicada através da **memorização**, utilizando o decorador `@lru_cache` para armazenar resultados já calculados e evitar recomputações desnecessárias.

**Principais estruturas utilizadas:**
- Funções recursivas (`def dp(...)`)
- Cache automático com `functools.lru_cache`
- Estrutura condicional para tratamento de excesso e falta de estoque

📈 **Vantagem:**  
Clareza conceitual e facilidade de implementação.  

📉 **Desvantagem:**  
Pode gerar estouro de pilha para instâncias muito grandes.

---

### ⚙️ 2. **Versão Iterativa (Bottom-Up)**

**Arquivo:** `modelo_dp_iterativo.py`

Nesta versão, a tabela `dp[dia][estoque]` é construída de forma iterativa, partindo do último dia até o primeiro.  
Cada célula representa o custo mínimo de operação a partir de um determinado dia e nível de estoque.

A abordagem **bottom-up** elimina chamadas recursivas e garante que os resultados futuros estejam disponíveis quando forem necessários para calcular estados anteriores.

**Principais estruturas utilizadas:**
- Lista bidimensional (`dp = [[...]]`)
- Laços `for` aninhados para percorrer dias, estoques e quantidades de reposição
- Comparações e atualização incremental de custos mínimos

📈 **Vantagem:**  
Mais eficiente e escalável para grandes volumes de dados.  

📉 **Desvantagem:**  
Requer maior uso de memória para armazenar a tabela completa.

---

### 🔍 3. **Comparação das Duas Versões**

**Arquivo:** `main.py`

Ambas as abordagens — recursiva e iterativa — devem produzir **o mesmo resultado ótimo**.  
O script principal executa as duas versões e compara seus resultados para validar a modelagem.

```python
if resultado_topdown == resultado_bottomup:
    print("✅ Ambos os métodos produzem o mesmo resultado.")
else:
    print("⚠️ Resultados diferentes.")
