import math
import random
from import randint

def RSA(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 0
    for i in range(2, z):
        if math.gcd(i, z) == 1:
            e = i
            break
    d = 0
    for i in range(z):
        x = 1+(i*z)
        if x % e == 0:
            d = int(x / e)
            break
    return [e, n], [d, n]

def get_prime_number():
    while True:
        number = random.randint(100, 300)
        if isPrime(number, 6) is True: return number

def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def MillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def isPrime(n, k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    for i in range(6):
        if (MillerTest(d, n) == False):
            return False

    return True

def encrypt(message, key):
    encrypt_message = []
    for m in message:
        encrypt_message.append(pow(ord(m), key[0]) % key[1])
    return encrypt_message

def decrypt(message, key):
    decrypt_message = ''
    for m in message:
        decrypt_message += chr(pow(m, key[0]) % key[1])
    return decrypt_message

public_key, private_key = RSA(get_prime_number(), get_prime_number())

print('Public Key:', public_key)

print('Private Key:', private_key)

message = "Test message"

encrypted = encrypt(message, public_key)
print("Encrypted message: ", encrypted)
decrypted = decrypt(encrypted, private_key)
print('Decrypted message:', decrypted)
