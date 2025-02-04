from random import choice
import string

print("-"*40)
print("OCTAVO SCRIPT")
print("-"*40)

characters = string.printable.strip()

length = 0
while True:
    try:
        length = int(input("Ingresa el tamaño deseado para la llave: "))
        if length < 1:
            print("El tamaño de la llave debe ser mayor a 0.\n")
        else: break
    except:
        print("El valor debe ser un número entero.\n")

def generateKey(length):
    key = ""
    for _ in range(length):
        key += choice(characters)
    return key

def cypher(message, key):
    cypher = ""
    for i in range(len(message)):
        cypher += characters[(characters.index(message[i]) + characters.index(key[i % len(key)])) % len(characters)] 
    return cypher

def decypher(cypher, key):
    message = ""
    for i in range(len(cypher)):
        message += characters[(characters.index(cypher[i]) - characters.index(key[i % len(key)])) % len(characters)]
    return message
        
key = generateKey(length)
message = input("Ingresa el mensaje a cifrar: ")
cyph = cypher(message, key)

print("\nRESULTADO:")
print(f"🔑 Llave generada: {key}\n")
print(f"🔒 Mensaje cifrado: {cyph}\n")
print(f"🔓 Mensaje descifrado: {decypher(cyph, key)}\n")