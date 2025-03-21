'''
Compilación de funciones AES desarrolladas para el ejercicio Block Cipher.
Se busca cifrar una imagen mediante AES con ECB y CBC.
Autor: Erick Guerra - 21781
Creación: 16/03/2025
'''

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
from PIL import Image
import os

# Funciones útiles
def getRandomKey(keySize=16):
    return get_random_bytes(keySize)

# Cifrado ECB
def cipherAES_ECB(data, key=None):
    if key is None:
        key = getRandomKey()
    
    paddingData = pad(data, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_data = cipher.encrypt(paddingData)
    
    return cipher_data, key

# Descifrado ECB
def decipherAES_ECB(cipher_data, key=None):
    cipher = AES.new(key, AES.MODE_ECB)
    paddingData = cipher.decrypt(cipher_data)
    datos = unpad(paddingData, AES.block_size)
    return datos

# Cifrado CBC
def cipherAES_CBC(data, key=None, initVector=None):
    if key is None:
        key = getRandomKey()
        
    if initVector is None:
        initVector = getRandomKey(AES.block_size)
    
    paddingData = pad(data, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, initVector)
    cipher_data = cipher.encrypt(paddingData)
    
    return cipher_data, key, initVector

# Descifrado CBC
def decipherAES_CBC(cipher_data, key, initVector):
    cipher = AES.new(key, AES.MODE_CBC, initVector)
    paddingData = cipher.decrypt(cipher_data)
    datos = unpad(paddingData, AES.block_size)
    return datos

# Cifrado imagen
def cipherImage_AES(path):
    image = Image.open(path)
    width, height = image.size
    
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    raw_data = image.tobytes()
    
    key = getRandomKey()
    
    cipher_ecb, _ = cipherAES_ECB(raw_data, key)
    
    initVector = get_random_bytes(AES.block_size)
    cipher_cbc, _, _ = cipherAES_CBC(raw_data, key, initVector)
    
    os.makedirs('Images', exist_ok=True)
    
    data_size = width * height * 3
    
    try:
        ecb_data = cipher_ecb[:data_size]
            
        image_ecb = Image.frombytes('RGB', (width, height), ecb_data)
        image_ecb.save('Images/image_ecb.png')
        
        cbc_data = cipher_cbc[:data_size]
            
        image_cbc = Image.frombytes('RGB', (width, height), cbc_data)
        image_cbc.save('Images/image_cbc.png')
        
        return key, initVector
        
    except Exception as e:
        print(f"Error creating encrypted images: {e}")
        raise