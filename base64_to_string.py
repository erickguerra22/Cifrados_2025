import math
from string_to_binary import toBinary
from bytes_to_string import toDecimal, splitBinary

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

if __name__ == "__main__":
    print("-"*40)
    print("CADENA BASE 64 A TEXTO")
    print("-"*40)

    print("\nEjemplo 1: cGFyYW5nYXJpY3V0aXJpbWljdWFybw==")
    word = "cGFyYW5nYXJpY3V0aXJpbWljdWFybw=="

    base64Codes = [base64.index(c) for c in word if c != '=']
    bin = [toBinary(d, 6) for d in base64Codes]
    bin = "".join(bin)

    binary = bin[:len(bin)-(2 * word.count("="))]

    binary = splitBinary(binary)

    ascii = [toDecimal(block) for block in binary]
    text = [chr(d) for d in ascii]

    print(f"\nRESULTADO:\n{"".join(text)}")
    print("-"*40)

    print("\nEjemplo 2: b3RvcnJpbm9sYXJpbmfzbG9nbw==")
    word = "b3RvcnJpbm9sYXJpbmfzbG9nbw=="

    base64Codes = [base64.index(c) for c in word if c != '=']
    bin = [toBinary(d, 6) for d in base64Codes]
    bin = "".join(bin)

    binary = bin[:len(bin)-(2 * word.count("="))]

    binary = splitBinary(binary)

    ascii = [toDecimal(block) for block in binary]
    text = [chr(d) for d in ascii]

    print(f"\nRESULTADO:\n{"".join(text)}")
    print("-"*40)
