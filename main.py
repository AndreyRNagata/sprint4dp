from modelo_dp import dp, estoque_inicial
from modelo_dp_iterativo import dp as dp_iterativo

resultado_topdown = dp(0, estoque_inicial)
resultado_bottomup = dp_iterativo[0][estoque_inicial]

print("=== COMPARAÇÃO ===")
print(f"Recursivo (Top-Down): {resultado_topdown}")
print(f"Iterativo (Bottom-Up): {resultado_bottomup}")

if resultado_topdown == resultado_bottomup:
    print("✅ Ambos os métodos produzem o mesmo resultado.")
else:
    print("⚠️ Resultados diferentes!")
