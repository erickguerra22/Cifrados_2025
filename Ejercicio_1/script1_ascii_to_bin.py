def toBinary(decimal):
    binary = ""
    while len(binary)<8:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

def text_to_bin(word):
    ascii = [ord(c) for c in word]
    bin = [toBinary(d) for d in ascii]

    return"".join(bin)
    
if __name__ == "__main__":
    print("-"*40)
    print("PRIMER SCRIPT")
    print("-"*40)
    word = input("Ingresa el texto a convertir a binario: ")

    print(f"\nRESULTADO:\n{text_to_bin(word)}")
    print("-"*40)
