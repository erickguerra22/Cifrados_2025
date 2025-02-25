import math

def toDecimal(binary):
    return int(binary, 2)

def splitBinary(binary, block_length=8):
    blocks = []
    for i in range(0, len(binary), block_length):
        if i + block_length <= len(binary):
            blocks.append(binary[i:i+block_length])
        else:
            last_block = binary[i:]
            blocks.append(last_block.ljust(block_length, '0'))
    return blocks

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
