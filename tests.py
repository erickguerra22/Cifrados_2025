from utils import *
from caesar import cypher as caesarCypher, deCypher as caesarDeCypher, getK
from afin import cypher as afinCypher, deCypher as afinDeCypher, getValues
from vigenere import cypher as vigenereCypher, deCypher as vigenereDeCypher, getKey

# PRUEBAS DE CIFRADO Y DESCIFRADO

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

while True:
    message = input("Ingresa el mensaje a cifrar: ")
    op = getOption(menu, 4, 1)

    if op == 1:
        print("-"*40)
        print("CIFRADO CAESAR")
        print("-"*40)
        k = getK()
        
        cyph = caesarCypher(message, k)
        decyph = caesarDeCypher(cyph, k)
        
    if op == 2:
        print("-"*40)
        print("CIFRADO AFÍN")
        print("-"*40)
        
        a, b = getValues()
        
        cyph = afinCypher(message, a, b)
        decyph = afinDeCypher(cyph, a, b)
        
    if op == 3:
        print("-"*40)
        print("CIFRADO VIGENÈRE")
        print("-"*40)
        
        key = getKey()
        
        cyph = vigenereCypher(message, key)
        decyph = vigenereDeCypher(cyph, key)
    
    if op != 4:
        print("\nRESULTADO:")
        print(f"🔒 Mensaje cifrado: {cyph}\n")
        print(f"🔓 Mensaje descifrado: {decyph}\n")
    
    op = getOption("¿Deseas continuar?\n1. Sí\n2. No", 2, 1)
    
    if op == 2:
        break