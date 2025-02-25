from random import randint
import random

def generate_keystream(length, key):
    random.seed(hash(key))
    keystream = ""
    for _ in range(length):
        keystream += chr(randint(32, 126))
    return keystream
    