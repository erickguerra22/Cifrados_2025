import math

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print("-"*40)
print("TERCER SCRIPT")
print("-"*40)
binary = input("Ingresa el binario a convertir en BASE64: ")
equals = int((6 - len(binary)%6) / 2)
binary = f"{binary}{"0"*equals*2}"

def toDecimal(binary):
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** (len(binary) - i - 1)
    return decimal

def splitBinary(binary):
    binaryBlocks = []
    for i in range(len(binary), 0 ,-6):
        binaryBlocks.insert(0, binary[i-6:i])
    return binaryBlocks

binaryBlocks = splitBinary(binary)

ascii = [toDecimal(b) for b in binaryBlocks]
base64List = [base64[n] for n in ascii]
for i in range(equals):
    base64List.append("=")

print(f"\nRESULTADO:\n{"".join(base64List)}")
print("-"*40)