from PIL import Image
import numpy as np

def get_image(imagepath):
    return Image.open(imagepath)

mainImage = get_image("images/main_image.jpg")
keyImage = get_image("images/key_image.jpg")

keyImage = keyImage.resize(mainImage.size)

mainArray = np.array(mainImage)
keyArray = np.array(keyImage)

xor = np.bitwise_xor(mainArray, keyArray)

encryptedImage = Image.fromarray(xor)

encryptedImage.save("xor_images_result.png")

print("\nRESULTADO:")
print("Imagen cifrada almacenada en 'xor_images_result.png'")