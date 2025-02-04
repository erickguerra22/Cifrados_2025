from random import choice
import string

print("-"*40)
print("NOVENO SCRIPT")
print("-"*40)

characters = string.printable.strip()

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
        
message = input("Ingresa el mensaje a cifrar: ")
key = generateKey(len(message))
cyph = cypher(message, key)

print("\nRESULTADO:")
print(f"🔑 Llave generada: {key}\n")
print(f"🔒 Mensaje cifrado: {cyph}\n")
print(f"🔓 Mensaje descifrado: {decypher(cyph, key)}\n")