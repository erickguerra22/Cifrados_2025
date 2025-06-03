'''
    La razón de que una imagen se corrompe cuando se intenta encriptar utilizando una llave de texto plano, se debe a que, si bien la llave se convierte a binario con códigos ASCII, la imagen está empaquetada directamente en bytes, y estos dos enfoques pueden no ser compatibles, por lo que la información almacenada en la imagen no corresponderá con paquetes de bytes, por más que esté escrita en código binario. 
'''

import base64

def image_to_bytes(imagepath):
    with open(imagepath, "rb") as file:
        return file.read()
    
def xor_bytes(data: bytes, key: str) -> bytes:
    key_bytes = key.encode('utf-8')
    key_len = len(key_bytes)
    return bytes(data[i] ^ key_bytes[i % key_len] for i in range(len(data)))

if __name__ == "__main__":
    key = input("Ingrese la clave para cifrar la imagen: ")

    realImage = image_to_bytes("decypher_image.png")
    encryptedBytes = xor_bytes(realImage, key)

    with open("cypher_image.png", "wb") as file:
        file.write(encryptedBytes)

    print("\nRESULTADO:")
    print("Imagen cifrada almacenada en 'cypher_image.png'")

