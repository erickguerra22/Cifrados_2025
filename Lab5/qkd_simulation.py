from utils import *

# Ejecución de la simulación
n_bits = int(input("Ingrese el número de bits a simular: "))
print("=== Simulación BB84 sin interceptación ===")
df, key_bits, porcentaje, _ = simular_bb84(n_bits)
print(df)
print(f"\nBits finales de clave: {key_bits} ({porcentaje:.2f}% del total)")

print("\n=== Simulación BB84 con interceptación de Eve ===")
df_eve, key_bits_eve, porcentaje_eve, deteccion = simular_bb84(n_bits, eve_intercepta=True)
print(df_eve)
print(f"\nBits finales de clave: {key_bits_eve} ({porcentaje_eve:.2f}% del total)")
print(deteccion)