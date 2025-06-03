from tabulate import tabulate
from Lab2.Parte_A.string_to_binary import wordToBinary
from Lab2.Parte_A.bytes_to_string import toDecimal, splitBinary

def xor_strings(word, key, method="fill"):
    bin1 = wordToBinary(word)
    bin2 = wordToBinary(key)
        
    if method == "fill":
        if len(bin2) < len(bin1):
            bin2 = bin2.zfill(len(bin1))
        elif len(bin2) > len(bin1):
            bin2 = bin2[-len(bin1):]
    else:
        bin2 = bin2 * (len(bin1) // len(bin2)) + bin2[:len(bin1) % len(bin2)]
    
    result = ''
    for i in range(len(bin1)):
        result += '1' if bin1[i] != bin2[i] else '0'
    
    return bin1, bin2, result

if __name__ == "__main__":
    print("-"*40)
    print("XOR ENTRE DOS CADENAS DE TEXTO")
    print("-"*40)


    word = input("Ingresa la palabra: ")
    key = ""

    while True:
        key = input("Ingresa la llave:")
        if len(key) > len(word):
            print("La llave debe ser de menor o igual tamaño de la palabra.")
        else: break

    bin1, bin2, xor = xor_strings(word, key)

    print(f"bin1: {bin1}")
    print(f"bin2: {bin2}")
    print(f"xor: {xor}")

    data = [["Palabra","Llave","XOR"]]

    for i in range(len(xor)):
        a = bin1[i] if i < len(bin1) else ""
        b = bin2[i] if i < len(bin2) else ""
        data.append([a,b,xor[i]])

    binary = splitBinary(xor)

    ascii = [toDecimal(block) for block in binary]
    text = [chr(d) for d in ascii]

    finalWord = "".join(text)
        
    print("\nRESULTADO:")
    print(tabulate(data, headers="firstrow", tablefmt="grid"))
    print(f"Palabra resultante: {finalWord}")