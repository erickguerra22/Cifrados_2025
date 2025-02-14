base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def toBinary(decimal):
    binary = ""
    while len(binary)<6:
        binary = f"{decimal % 2}{binary}"
        decimal = int(decimal / 2)
    return binary

def base64_to_bin(base64):
    base64Codes = [base64.index(c) for c in base64 if c != '=']
    bin = [toBinary(d) for d in base64Codes]
    bin = "".join(bin)

    return bin[:len(bin)-(2 * base64.count("="))]

if __name__ == "__main__":
    print("-"*40)
    print("SEGUNDO SCRIPT")
    print("-"*40)
    
    base64 = input("Ingresa el texto en BASE64: ")
    print(f"\nRESULTADO:\n{base64_to_bin(base64)}")
    print("-"*40)
