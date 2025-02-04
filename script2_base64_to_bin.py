base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print("-"*40)
print("SEGUNDO SCRIPT")
print("-"*40)
word = input("Ingresa el texto en BASE64: ")

def toBinary(decimal):
    binary = ""
    while len(binary)<6:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

base64Codes = [base64.index(c) for c in word if c != '=']
bin = [toBinary(d) for d in base64Codes]
bin = "".join(bin)

print(f"\nRESULTADO:\n{bin[:len(bin)-(2 * word.count("="))]}")
print("-"*40)
