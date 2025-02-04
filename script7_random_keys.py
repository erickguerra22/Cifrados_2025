from random import randint

print("-"*40)
print("SEPTIMO SCRIPT")
print("-"*40)

length = 0
while True:
    try:
        length = int(input("Ingresa el tamaño deseado para la llave: "))
        if length < 1:
            print("El tamaño de la llave debe ser mayor a 0.\n")
        else: break
    except:
        print("El valor debe ser un número entero.\n")
    
key = ""

for _ in range(length):
    key += chr(randint(32,126))

print("\nRESULTADO:\n")
print(f"🔑 Llave generada: {key}")