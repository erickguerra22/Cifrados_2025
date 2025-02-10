import math

def toDecimal(binary):
    decimal = 0
    for i in range(len(binary)-1,-1, -1):
        if binary[i] == '1':
            decimal += 2 ** (len(binary) - i - 1)
    return decimal

def splitBinary(binary, blockLength = 8):
    if len(binary) % blockLength != 0:
        lastIndex = math.floor(len(binary) / blockLength) * blockLength
        binary = f"{binary[:lastIndex]}{'0'*(blockLength-len(binary[lastIndex:]))}{binary[lastIndex:]}"
    binaryBlocks = []
    for i in range(len(binary), 0 ,-blockLength):
        binaryBlocks.insert(0, binary[i-blockLength:i])
    return binaryBlocks

if __name__ == "__main__":
    print("-"*40)
    print("CADENA DE BYTES A CARACTERES")
    print("-"*40)

    print("\nEjemplo 1: 01110000011000010111001001100001011011100110011101100001011100100110100101100011011101010111010001101001011100100110100101101101011010010110001101110101011000010111001001101111")
    
    binary = "01110000011000010111001001100001011011100110011101100001011100100110100101100011011101010111010001101001011100100110100101101101011010010110001101110101011000010111001001101111"

    binary = splitBinary(binary)

    ascii = [toDecimal(block) for block in binary]
    text = [chr(d) for d in ascii]

    print(f"\nRESULTADO:\n{"".join(text)}")
    print("-"*40)

    print("\nEjemplo 2: 01101111011101000110111101110010011100100110100101101110011011110110110001100001011100100110100101101110011001111111001101101100011011110110011101101111")
    
    binary = "01101111011101000110111101110010011100100110100101101110011011110110110001100001011100100110100101101110011001111111001101101100011011110110011101101111"

    binary = splitBinary(binary)

    ascii = [toDecimal(block) for block in binary]
    text = [chr(d) for d in ascii]

    print(f"\nRESULTADO:\n{"".join(text)}")
    print("-"*40)
