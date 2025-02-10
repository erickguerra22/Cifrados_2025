from tabulate import tabulate
from collections import Counter
from Parte_A.frequencies import theorical, getFrequencies
from Parte_A.vigenere import deCypher
from Parte_A.caesar import deCypher as caesarDeCypher
from Parte_A.utils import getOption
import numpy as np

theoricalIC = 0.075
alphabet = "abcdefghijklmnñopqrstuvwxyz"
maxTheorical = max(theorical, key=theorical.get)

def getIc(text):
    N = len(text)
    if N <= 1:
        return 0
    
    experimental = getFrequencies(text)
    frequencies = [freq * len(text) for freq in experimental.values()]
    sum_freq = sum(freq * (freq - 1) for freq in frequencies)
    return sum_freq / (N * (N - 1))

print("-"*40)
print("DESCIFRADO VIGENÈRE POR FUERZA BRUTA")
print("-"*40)

with open("cyphers/vigenere.txt", "r", encoding="utf-8") as file:
    cypher = file.read()

# Obtener longitudes de llave desde la más probable hasta la menos
keyLengths = []

for N in range(1,len(alphabet)):
    nIcs = []
    for i in range(N):
        subtext = cypher[i::N]
        if len(subtext) > 1:
            nIcs.append(getIc(subtext))

    keyLengths.append((N, np.mean(nIcs)))

keyLengths = sorted(keyLengths, key=lambda x: -x[1])

print(f"Longitudes más probables: {keyLengths}")

def getBestShift(substring):
    bestShift = 0
    minError = float('inf')
    
    for shift in range(len(alphabet)):
        shifted = caesarDeCypher(substring, shift)
        freq = getFrequencies(shifted)
        
        err = sum((freq.get(char, 0) - theorical[char])**2 
                  for char in theorical)
        
        if err < minError:
            minError = err
            bestShift = shift
            
    return bestShift

def clearRepeatedKey(key):
    for i in range(1, len(key)):
        fragment = key[:i]
        if key == fragment * (len(key) // len(fragment)):
            return fragment
    return key

print("\n🔍 DESCIFRADO:")
for N in [x[0] for x in keyLengths]:        
    substrings = [cypher[i::N] for i in range(N)]
    
    key = ""
    for substring in substrings:
        shift = getBestShift(substring)
        key += alphabet[shift]

    key = clearRepeatedKey(key)

    print(f"🗝️ CLAVE A PROBAR: {key} CON LONGITUD: {N}")
    decyph = deCypher(cypher, key)
    print(f"🔓 Mensaje descifrado: {decyph}\n")
    
    op = getOption("¿Mensaje encontrado?\n1. Sí\n2. No", 2, 1)
    if op == 1:
        with open("messages/vigenere_key.txt", "w", encoding="utf-8") as file:
            file.write(f"CLAVE: {key}\n")
            file.write(f"Mensaje descifrado:\n{decyph}")
        print("\n🔑 Clave y mensaje guardados en vigenere.txt\n")
        exit()
    print("\n🔍 Continuando con siguiente iteración...")

print("\n❌ No se ha podido descifrar el mensaje")
