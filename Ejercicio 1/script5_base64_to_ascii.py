import math

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print("-"*40)
print("QUINTO SCRIPT")
print("-"*40)
word = input("Ingresa el texto en BASE64: ")

def toBinary(decimal):
    binary = ""
    while len(binary)<6:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

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

base64Codes = [base64.index(c) for c in word if c != '=']
bin = [toBinary(d) for d in base64Codes]
bin = "".join(bin)

binary = bin[:len(bin)-(2 * word.count("="))]

binary = splitBinary(binary)

ascii = [toDecimal(block) for block in binary]
text = [chr(d) for d in ascii]

print(f"\nRESULTADO:\n{"".join(text)}")
print("-"*40)
