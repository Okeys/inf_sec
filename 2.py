import random
import math
from random import randint

class Message(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key
    
    def enc_decr_message(self, message):
        enc_decr_message = ""
        key = self.full_key
        for c in message:
            enc_decr_message += chr(ord(c)^key)
        return enc_decr_message

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def get_prime_number(n):
    while True:
        number = random_with_N_digits(n)
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

message = "Приеду завтра в полдень, Крутицкий Олег Андреевич"

a_public = get_prime_number(int(math.ceil(math.log(len(message),2))))
print("Alice public key: ", a_public)
a_private = get_prime_number(int(math.ceil(math.log(len(message),2))))
print("Alice private key: ", a_private)

b_public = get_prime_number(int(math.ceil(math.log(len(message),2))))
print("Bob public key: ", b_public)
b_private = get_prime_number(int(math.ceil(math.log(len(message),2))))
print("Bob private key: ", b_private)

e_private = get_prime_number(int(math.ceil(math.log(len(message),2))))
print("Eve private ley: ", e_private)

Alice = Message(a_public, b_public, a_private)
Bob = Message(a_public, b_public, b_private)
Eve = Message(a_public, b_public, e_private)

a_partial = Alice.generate_partial_key()
print("Alice partial key: ", a_partial)
b_partial = Bob.generate_partial_key()
print("Bob parial key: ", b_partial)
e_partial = Eve.generate_partial_key()
print("Eve partial key: ", e_partial)
a_full = Alice.generate_full_key(b_partial)

print("Alice full key: ", a_full)
b_full = Bob.generate_full_key(a_partial)
print("Bob full key: ", b_full)
e_full = Eve.generate_full_key(a_partial)
print("Eve full key: ", e_full)

b_encrypted = Bob.enc_decr_message(message)
print("Encrypted message: ", b_encrypted)
desc_message = Alice.enc_decr_message(b_encrypted)
print("Decrypted message: ", desc_message)