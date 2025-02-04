# Cifrado Afín
from utils import *

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def getKey():
    op = getOption("Seleccione el tipo de llave a utilizar:\n1. Definida\n2. Generada", 2, 1)
    while True:
        key = generateKey(alphabet, False) if op == 2 else input("Ingresa la llave deseada: ")
        if op == 2:
            print(f"🔑 Llave generada: {key}")
        
        # Verificar que todos los caracteres en Key están dentro de alphabet
        if all([c.lower() in alphabet for c in key]):
            break
        print("La llave contiene caracteres que no forman parte del alfabeto.")
    return key

def cypher(message, key):
    M = len(alphabet)
    N = len(key)
    
    cyph = ""
    for i, char in enumerate(message):
        c = char.lower()
        if c not in alphabet:
            cyph += c.upper() if char.isupper() else c
            continue
        newIndex = (alphabet.index(c) + alphabet.index(key[i % N].lower())) % M
        cyph += alphabet[newIndex].upper() if char.isupper() else alphabet[newIndex]
    return cyph

def deCypher(cyph, key):
    M = len(alphabet)
    N = len(key)
    
    message = ""
    for i, char in enumerate(cyph):
        c = char.lower()
        if c not in alphabet:
            message += c.upper() if char.isupper() else c
            continue
        newIndex = (alphabet.index(c) - alphabet.index(key[i % N].lower())) % M
        message += alphabet[newIndex].upper() if char.isupper() else alphabet[newIndex]
    return message

if __name__ == "__main__":
    print("-"*40)
    print("CIFRADO VIGENÈRE")
    print("-"*40)

    message = input("Ingresa el mensaje a cifrar: ")
    key = getKey()

    cyph = cypher(message, key)

    print("\nRESULTADO:")
    print(f"🔒 Mensaje cifrado: {cyph}\n")
    
    print("-"*40)
    print("DESCIFRADO VIENÈRE")
    print("-"*40)

    message = input("Ingresa el mensaje a descifrar: ")
    key = getKey()

    cyph = deCypher(message, key)

    print("\nRESULTADO:")
    print(f"🔓 Mensaje descifrado: {cyph}\n")