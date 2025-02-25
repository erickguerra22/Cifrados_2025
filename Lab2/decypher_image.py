import base64
from Ejercicio_1.script1_ascii_to_bin import text_to_bin

def image_to_base64(imagepath):
    with open(imagepath, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

def base64_to_binary(base64code):
    binary = base64.b64decode(base64code)
    return ''.join(format(byte, '08b') for byte in binary)

def binary_to_bytes(binary):
    return bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))

if __name__ == "__main__":
    key = "cifrados_2025"
    
    cypherImage = image_to_base64("imagen_xor.png")
    imageBinary = base64_to_binary(cypherImage)
    
    keyBinary = text_to_bin(key)
    keyBinary = keyBinary * (len(imageBinary) // len(keyBinary)) + keyBinary[:len(imageBinary) % len(keyBinary)]
    
    decryptedBinary = ''.join('1' if a != b else '0' for a, b in zip(imageBinary, keyBinary))
    realImage = binary_to_bytes(decryptedBinary)
    
    with open("decypher_image.png", "wb") as file:
        file.write(realImage)
        
    print("\nRESULTADO:")
    print("Imagen descifrada almacenada en 'decypher_image.png'")