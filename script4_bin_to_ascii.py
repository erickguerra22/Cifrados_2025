import math

print("-"*40)
print("CUARTO SCRIPT")
print("-"*40)
binary = input("Ingresa el binario a convertir en texto: ")

def toDecimal(binary):
    decimal = 0
    for i in range(len(binary)-1,-1, -1):
        if binary[i] == '1':
            decimal += 2 ** (len(binary) - i - 1)
    return decimal

def splitBinary(binary):
    if len(binary) % 8 != 0:
        lastIndex = math.floor(len(binary) / 8) * 8
        binary = f"{binary[:lastIndex]}{'0'*(8-len(binary[lastIndex:]))}{binary[lastIndex:]}"
    binaryBlocks = []
    for i in range(len(binary), 0 ,-8):
        binaryBlocks.insert(0, binary[i-8:i])
    return binaryBlocks

binary = splitBinary(binary)

ascii = [toDecimal(block) for block in binary]
text = [chr(d) for d in ascii]

print(f"\nRESULTADO:\n{"".join(text)}")
print("-"*40)
