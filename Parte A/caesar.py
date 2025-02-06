# Cifrado Caesar
from utils import *

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def getK():
    k = getOption("Ingresa el desplazamiento para el cifrado: ", float('inf'), float('-inf'))
    return k

def cypher(message, k):
    cyph = ""
    for char in message:
        c = char.lower()
        if c not in alphabet:
            cyph += c.upper() if char.isupper() else c
            continue
        newIndex = (alphabet.index(c) + k) % len(alphabet)
        cyph += alphabet[newIndex].upper() if char.isupper() else alphabet[newIndex]
    return cyph

def deCypher(cyph, k):
    message = ""
    for char in cyph:
        c = char.lower()
        if c not in alphabet:
            message += c.upper() if char.isupper() else c
            continue
        newIndex = (alphabet.index(c) - k) % len(alphabet)
        message += alphabet[newIndex].upper() if char.isupper() else alphabet[newIndex]
    return message

if __name__ == "__main__":
    print("-"*40)
    print("CIFRADO CAESAR")
    print("-"*40)

    message = input("Ingresa el mensaje a cifrar: ")
    k = getK()

    cyph = cypher(message, k)

    print("\nRESULTADO:")
    print(f"🔒 Mensaje cifrado: {cyph}\n")
    
    print("-"*40)
    print("DESCIFRADO CAESAR")
    print("-"*40)

    message = input("Ingresa el mensaje a descifrar: ")
    k = getK()

    cyph = deCypher(message, k)

    print("\nRESULTADO:")
    print(f"🔓 Mensaje descifrado: {cyph}\n")