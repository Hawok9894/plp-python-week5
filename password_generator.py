import random
import string
import math


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = generate_password()
print("Generated Password:", password)
print("Password Strength Score:", math.log2(len(password)) * 10)
