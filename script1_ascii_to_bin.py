print("-"*40)
print("PRIMER SCRIPT")
print("-"*40)
word = input("Ingresa el texto a convertir a binario: ")

def toBinary(decimal):
    binary = ""
    while len(binary)<8:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

ascii = [ord(c) for c in word]
bin = [toBinary(d) for d in ascii]

print(f"\nRESULTADO:\n{"".join(bin)}")
print("-"*40)
