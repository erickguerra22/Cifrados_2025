import math
from Parte_A.string_to_binary import toBinary
from Parte_A.bytes_to_string import toDecimal, splitBinary

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_to_text(base64code):
    base64Codes = [base64.index(c) for c in base64code if c != '=']
    bin = [toBinary(d, 6) for d in base64Codes]
    bin = "".join(bin)

    binary = bin[:len(bin)-(2 * base64code.count("="))]

    binary = splitBinary(binary)

    ascii = [toDecimal(block) for block in binary]
    text = [chr(d) for d in ascii]

    return "".join(text)

if __name__ == "__main__":
    print("-"*40)
    print("CADENA BASE 64 A TEXTO")
    print("-"*40)

    print("\nEjemplo 1: cGFyYW5nYXJpY3V0aXJpbWljdWFybw==")
    base64code = "cGFyYW5nYXJpY3V0aXJpbWljdWFybw=="

    print(f"\nRESULTADO:\n{base64_to_text(base64code)}")
    print("-"*40)

    print("\nEjemplo 2: b3RvcnJpbm9sYXJpbmfzbG9nbw==")
    base64code = "b3RvcnJpbm9sYXJpbmfzbG9nbw=="

    print(f"\nRESULTADO:\n{base64_to_text(base64code)}")
    print("-"*40)