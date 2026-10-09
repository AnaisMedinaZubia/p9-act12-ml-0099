# medina Anais NC 0099
import pandas as pd

# 10.
datos10 = {
    'distancia_km': [4.1, 2.6, 5.9, 1.7, 3.4],
    'trafico_nivel': [2, 1, 3, 2, 1],
    'edad_repartidor': [35, 27, 43, 31, 24],
    'tiempo_entrega_min': [34, 19, 55, 15, 23]
}

df = pd.DataFrame(datos10)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Medina Anais NC 0099")