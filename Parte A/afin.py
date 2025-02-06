# Cifrado Afín
import math
from utils import *

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def getValues():
    a = 0
    while True:
        try:
            a = int(input("Ingresa el valor de a: \nR// "))
            if math.gcd(a, len(alphabet)) <= 1:
                break
            print("El valor de 'a' no debe tener factor común con 'M'.\n")
        except:
            print("El valor debe ser un número entero.\n")
        
    b = getOption("Ingresa el valor de b: ", float('inf'), float('-inf'))
    return a, b

def cypher(message, a, b):
    M = len(alphabet)
    cyph = ""
    for char in message:
        c = char.lower()
        if c not in alphabet:
            cyph += c.upper() if char.isupper() else c
            continue
        newIndex = (alphabet.index(c)*a + b) % M
        cyph += alphabet[newIndex].upper() if char.isupper() else alphabet[newIndex]
    return cyph

def deCypher(cyph, a, b):
    M = len(alphabet)
    message = ""
    for char in cyph:
        c = char.lower()
        if c not in alphabet:
            message += c.upper() if char.isupper() else c
            continue
        newIndex = (pow(a, -1, M) * (alphabet.index(c) - b)) % len(alphabet)
        message += alphabet[newIndex].upper() if char.isupper() else alphabet[newIndex]
    return message

if __name__ == "__main__":
    print("-"*40)
    print("CIFRADO AFÍN")
    print("-"*40)

    message = input("Ingresa el mensaje a cifrar: ")
    a, b = getValues()

    cyph = cypher(message, a, b)

    print("\nRESULTADO:")
    print(f"🔒 Mensaje cifrado: {cyph}\n")
    
    print("-"*40)
    print("DESCIFRADO AFÍN")
    print("-"*40)

    message = input("Ingresa el mensaje a descifrar: ")
    a, b = getValues()

    cyph = deCypher(message, a, b)

    print("\nRESULTADO:")
    print(f"🔓 Mensaje descifrado: {cyph}\n")