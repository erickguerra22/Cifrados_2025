def toBinary(decimal, block_length=8):
    return format(decimal, f'0{block_length}b')

def wordToBinary(word):
    result = ""
    for char in word:
        binary = format(ord(char), '08b')
        result += binary
    return result

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
