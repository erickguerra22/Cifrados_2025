from utils import *
from caesar import cypher as caesarCypher, deCypher as caesarDeCypher, getK
from afin import cypher as afinCypher, deCypher as afinDeCypher, getValues
from vigenere import cypher as vigenereCypher, deCypher as vigenereDeCypher, getKey
from random import randint
import math

# PRUEBAS DE CIFRADO Y DESCIFRADO

alphabet = "abcdefghijklmnñopqrstuvwxyz"
print("-"*40)
print("PRUEBAS DE CIFRADO Y DESCIFRADO")
print("-"*40)

cyph = ""
decyph = ""
menu = """Seleccione el algoritmo a probar:
    1. Caesar
    2. Afín
    3. Vigenère
    4. Cancelar"""
    
op = getOption("¿Qué tipo de pruebas realizar?\n1. Automáticas\n2. Manuales", 4, 1)
auto = True if op == 1 else False
iteration = 1

while True:
    message = input("Ingresa el mensaje a cifrar: ") if not auto else "ESTE ES UN MENSAJE DE PRUEBA"
    if auto and iteration == 1: print(f"\n💬 Mensaje a probar: {message}\n")
    op = getOption(menu, 4, 1) if not auto else iteration
    iteration += 1

    if op == 1:
        print("-"*40)
        print("CIFRADO CAESAR")
        print("-"*40)
        k = getK() if not auto else randint(1, 25)
        
        if auto: print(f"\n🦘 Saltos: {k}\n")
        
        cyph = caesarCypher(message, k)
        decyph = caesarDeCypher(cyph, k)
        
    if op == 2:
        print("-"*40)
        print("CIFRADO AFÍN")
        print("-"*40)
        
        a, b = getValues() if not auto else (randint(1, 25), randint(1, 25))
        
        while auto and math.gcd(a, len(alphabet)) > 1:
            a = randint(1, 25)
            
        if auto: print(f"\n🔢 a: {a} | b: {b}\n")
        
        cyph = afinCypher(message, a, b)
        decyph = afinDeCypher(cyph, a, b)
        
    if op == 3:
        print("-"*40)
        print("CIFRADO VIGENÈRE")
        print("-"*40)
        
        key = getKey() if not auto else generateKey(alphabet, True)
        
        if auto: print(f"\n🔑 Llave: {key}\n")
        
        cyph = vigenereCypher(message, key)
        decyph = vigenereDeCypher(cyph, key)
    
    if op != 4:
        print("\nRESULTADO:")
        print(f"🔒 Mensaje cifrado: {cyph}\n")
        print(f"🔓 Mensaje descifrado: {decyph}\n")
    
    op = getOption("¿Deseas continuar?\n1. Sí\n2. No", 2, 1) if not auto else 1 if iteration < 4 else 2
    
    if op == 2:
        break