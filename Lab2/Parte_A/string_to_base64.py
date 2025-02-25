from Parte_A.bytes_to_string import toDecimal, splitBinary
from Parte_A.string_to_binary import wordToBinary

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def string_to_base64(word):
    binary = wordToBinary(word)
    equals = int((6 - len(binary)%6) / 2)
    binary = f"{binary}{"0"*equals*2}"

    binaryBlocks = splitBinary(binary, 6)

    ascii = [toDecimal(b) for b in binaryBlocks]
    base64List = [base64[n] for n in ascii]
    for i in range(equals):
        base64List.append("=")

    return "".join(base64List)

if __name__ == "__main__":
    print("-"*40)
    print("CADENA DE CARACTERES A BASE64")
    print("-"*40)

    print("\nEjemplo 1: parangaricutirimicuaro")
    word = "parangaricutirimicuaro"

    print(f"\nRESULTADO:\n{string_to_base64(word)}")
    print("-"*40)

    print("\nEjemplo 2: otorrinolaringólogo")
    word = "otorrinolaringólogo"

    print(f"\nRESULTADO:\n{string_to_base64(word)}")
    print("-"*40)