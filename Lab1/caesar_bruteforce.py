# DESCIFRADO CAESAR POR FUERZA BRUTA

from tabulate import tabulate
from Parte_A.frequencies import theorical, getFrequencies
from Parte_A.caesar import deCypher
from Parte_A.utils import getOption

alphabet = "abcdefghijklmnñopqrstuvwxyz"
print("-"*40)
print("DESCIFRADO CAESAR POR FUERZA BRUTA")
print("-"*40)

cypher = ""
decyph = ""

with open("cyphers/ceasar.txt", "r", encoding="utf-8") as file:
    cyph = file.read()

experimental = getFrequencies(cyph)
maxTheorical = max(theorical, key=theorical.get)

maxExperimentals = []

for i in range(5):
    maxExperimental = max(experimental, key=experimental.get)
    maxExperimentals.append({"letra": maxExperimental, "saltos": (alphabet.index(maxExperimental) - alphabet.index(maxTheorical)) % len(alphabet)})
    experimental.pop(maxExperimental)

print("\n📊 ANÁLISIS DE FRECUENCIAS:\nLas letras más repetidas en el texto, son:")
print(tabulate(maxExperimentals, headers="keys", tablefmt="grid"))

print("\n🔍 DESCIFRADO:")

for item in maxExperimentals:
    print(f"Letra de prueba: {item['letra']} | Saltos: {item['saltos']}:")
    message = deCypher(cyph, item["saltos"])
    print(f"🔓 Mensaje descifrado: {message}\n")
    
op = getOption("¿Mensaje encontrado?\n1. Sí\n2. No", 2, 1)

if op == 2:
    print("\n🔍 Continuando con el resto del alfabeto...")
    for i in range(len(alphabet)):
        if i in [s['saltos'] for s in maxExperimentals]: continue
        print(f"Letra de prueba: {alphabet[i]} | Saltos: {i}:")
        message = deCypher(cyph, i)
        print(f"🔓 Mensaje descifrado: {message}\n")
        
letter = input("Ingresa la letra que resolvió el descifrado: ")
jumps = (alphabet.index(letter) - alphabet.index(maxTheorical)) % len(alphabet)
with open("messages/ceasar_key.txt", "w", encoding="utf-8") as file:
    file.write(f"Letra: {letter} | Saltos: {jumps}\n")
    file.write(f"Mensaje descifrado:\n{deCypher(cyph, jumps)}")
    
print("\n🔑 Clave y mensaje guardados en ceasar_key.txt\n")