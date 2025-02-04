from tabulate import tabulate

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def toDecimal(binary):
    decimal = 0
    for i in range(len(binary)-1,-1, -1):
        if binary[i] == '1':
            decimal += 2 ** (len(binary) - i - 1)
    return decimal

def toBinary(decimal, length):
    binary = ""
    while len(binary)<length:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

print("-"*40)
print("SEXTO SCRIPT")
print("-"*40)
while True:
    bin1 = input("Ingresa el primer binario: ")
    if(bin1.count('1') + bin1.count('0') != len(bin1)):
        print("El binario ingresado no es valido\n")
    else: break

while True:
    bin2 = input("Ingresa el segundo binario: ")
    if(bin2.count('1') + bin2.count('0') != len(bin2)):
        print("El binario ingresado no es valido\n")
    else: break
    
max_len = max(len(bin1), len(bin2))
bin1 = bin1.zfill(max_len)
bin2 = bin2.zfill(max_len)
    
dec1 = toDecimal(bin1)
dec2 = toDecimal(bin2)
xor = toBinary(dec1 ^ dec2, max(len(bin1), len(bin2)))

data = [["A","B","XOR"]]

for i in range(len(xor)):
    a = bin1[i] if i < len(bin1) else ""
    b = bin2[i] if i < len(bin2) else ""
    data.append([a,b,xor[i]])
    
print("\nRESULTADO:")
print(tabulate(data, headers="firstrow", tablefmt="grid"))