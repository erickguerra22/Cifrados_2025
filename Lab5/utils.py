import pandas as pd
import random
import numpy as np

def codificar_foton(bit, base):
    if base == '+':
        return '↕' if bit == 0 else '↔'
    elif base == 'x':
        return '↖' if bit == 0 else '↘'

def medir_foton(foton, base):
    if (foton == '↕' and base == '+') or (foton == '↖' and base == 'x'):
        return 0
    elif (foton == '↔' and base == '+') or (foton == '↘' and base == 'x'):
        return 1
    else:
        return random.randint(0, 1)

def simular_bb84(n_bits, eve_intercepta=False):
    bases = ['+', 'x']
    
    bits_alice = [random.randint(0, 1) for _ in range(n_bits)]
    bases_alice = [random.choice(bases) for _ in range(n_bits)]
    fotones = [codificar_foton(bit, base) for bit, base in zip(bits_alice, bases_alice)]
    
    # Interceptación de Eve (si está activa)
    if eve_intercepta:
        bases_eve = [random.choice(bases) for _ in range(n_bits)]
        bits_eve = [medir_foton(foton, base) for foton, base in zip(fotones, bases_eve)]
        
        fotones = [codificar_foton(bit, random.choice(bases)) for bit in bits_eve]
    
    bases_bob = [random.choice(bases) for _ in range(n_bits)]
    bits_bob = [medir_foton(foton, base) for foton, base in zip(fotones, bases_bob)]
    
    data = []
    for i in range(n_bits):
        coinciden = bases_alice[i] == bases_bob[i]
        data.append({
            'Índice': i+1,
            'Bit de Alice': bits_alice[i],
            'Base de Alice': bases_alice[i],
            'Fotón enviado': fotones[i],
            'Base de Bob': bases_bob[i],
            'Bit generado': bits_bob[i],
            '¿Bases coinciden?': coinciden,
            '¿Usar bit?': coinciden
        })
    
    df = pd.DataFrame(data)
    
    key_bits = df[df['¿Usar bit?']]['Bit generado'].count()
    porcentaje = (key_bits / n_bits) * 100
    
    deteccion_eve = ""
    if eve_intercepta:
        coincidencias = df[df['¿Bases coinciden?']]
        errores = sum(coincidencias['Bit de Alice'] != coincidencias['Bit generado'])
        tasa_error = (errores / len(coincidencias)) * 100 if len(coincidencias) > 0 else 0
        deteccion_eve = f"\nDetección de Eve: {errores} errores en bits coincidentes ({tasa_error:.2f}% de tasa de error)"
    
    return df, key_bits, porcentaje, deteccion_eve