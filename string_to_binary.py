def toBinary(decimal, blockLenght=8):
    binary = ""
    while len(binary)<blockLenght:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

def wordToBinary(word):
    ascii = [ord(c) for c in word]
    bin = [toBinary(d) for d in ascii]
    return "".join(bin)

if __name__ == "__main__":
    print("-"*40)
    print("CADENA DE CARACTERES A BITS")
    print("-"*40)

    print("\nEjemplo 1: parangaricutirimicuaro")
    word = "parangaricutirimicuaro"

    ascii = [ord(c) for c in word]
    bin = [toBinary(d) for d in ascii]

    print(f"\nRESULTADO:\n{"".join(bin)}")
    print("-"*40)

    print("\nEjemplo 2: otorrinolaringólogo")
    word = "otorrinolaringólogo"

    ascii = [ord(c) for c in word]
    bin = [toBinary(d) for d in ascii]

    print(f"\nRESULTADO:\n{"".join(bin)}")
    print("-"*40)
