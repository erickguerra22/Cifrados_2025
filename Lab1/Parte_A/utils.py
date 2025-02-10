from random import randint

def getOption(message, bigger, lower):
    op = 0
    while True:
        try:
            op = int(input(f"\n{message}\nR// "))
            if op > bigger or op < lower:
                print("Opción no válida.\n")
            else: break
        except:
            print("El valor debe ser un número entero.\n")
    return op

def generateKey(alphabet, auto):
    length = 0
    while True:
        try:
            length = int(input("Ingresa el tamaño deseado para la llave: \nR// ")) if not auto else randint(1, 25)
            if length < 1:
                print("El tamaño de la llave debe ser mayor a 0.\n")
            else: break
        except:
            print("El valor debe ser un número entero.\n")
        
    key = ""

    for _ in range(length):
        key += chr(randint(32,126)) if alphabet is None else alphabet[randint(0, len(alphabet)-1)]
        
    return key