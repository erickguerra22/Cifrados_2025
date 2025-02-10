# DESCIFRADO VIGENÈRE POR FUERZA BRUTA

from tabulate import tabulate
from Parte_A.frequencies import theorical, getFrequencies
from Parte_A.vigenere import deCypher
from Parte_A.utils import getOption
import math

alphabet = "abcdefghijklmnñopqrstuvwxyz"
print("-"*40)
print("DESCIFRADO VIGENÈRE POR FUERZA BRUTA")
print("-"*40)

cypher = ""
decyph = ""

with open("cyphers/vigenere.txt", "r", encoding="utf-8") as file:
    cyph = file.read()

experimental = getFrequencies(cyph)

maxTheorical = max(theorical, key=theorical.get)

maxExperimentals = []

for i in range(len(alphabet)):
    maxExperimental = max(experimental, key=experimental.get)
    maxExperimentals.append({"letra": maxExperimental, "frecuencia en texto": experimental[maxExperimental]})
    experimental.pop(maxExperimental)

print("\n📊 ANÁLISIS DE FRECUENCIAS:\nEste es el orden del alfabeto según su frecuencia en el texto:")
print(tabulate(maxExperimentals, headers="keys", tablefmt="grid"))

iteration = 0

print("\n🔍 DESCIFRADO:")
found = False
n = 0

while not found:
    iteration += 1

    print(f"\n🔢 ENCONTRANDO VALOR DE A:\nIniciando iteración {iteration}")
    a_values = []
    while len(a_values) < 5:
        if math.gcd(n, len(alphabet)) <= 1:
            a_values.append(n)
        n += 1
    n = a_values[-1] + 1
    print(f"Se probarán los siguientes valores para 'a': {a_values}\n")
    
    for item in maxExperimentals:
        print(f"LETRA DE PRUEBA: {item['letra']}\n")
        for a in a_values:
            b = (alphabet.index(item['letra']) - (alphabet.index(maxTheorical) * a) % len(alphabet)) % len(alphabet)
    
            print(f"Valores// a: {a} | b: {b}:")
            
            message = deCypher(cyph,a,b)
            print(f"🔓 Mensaje descifrado: {message}\n")
            
        op = getOption("¿Mensaje encontrado?\n1. Sí\n2. No", 2, 1)
    
        if op == 2:
            print("\n🔍 Continuando con siguiente iteración...")
            
        else:
            a = int(input("Ingresa el valor de 'a' encontrado: "))
            b = int(input("Ingresa el valor de 'b' encontrado: "))
            with open("messages/vigenere_key.txt", "w", encoding="utf-8") as file:
                file.write(f"A: {a} | B: {b}\n")
                file.write(f"Mensaje descifrado:\n{deCypher(cyph, a, b)}")
                
            print("\n🔑 Clave y mensaje guardados en vigenere_key.txt\n")
            found = True
            break
            