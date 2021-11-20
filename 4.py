from math import gcd
import random
import hashlib

def power(base, exp, mod):
    if exp == 0: return 1
    if exp & 1 == 0:
        r = power(base, exp // 2, mod)
        return (r * r) % mod
    else: 
        return (base % mod * power(base, exp - 1, mod)) % mod

def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True

def get_prime(n):
    while True:
        range_start = int("1" + "0" * (n), 2)
        range_end = int("1" + "1" * (n), 2)
        number = random.randint(range_start, range_end)
        if is_prime(number):
            return number

def root(modulo):
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            return g

def hashval(val):
    return int(hashlib.sha256(val.encode('utf-8')).hexdigest(), 16)

def SRP(password):
    N = 1
    q = 1
    g = 1
    while not is_prime(N):
        q = get_prime(4)
        N = 2*q + 1
        g = root(N)
    salt = random.getrandbits(3)
    x = hashval(str(salt) + password)
    v = power(g, x, N)
    a = random.randint(2, 100)
    A = power(g, a, N)
    if A != 0:
        b = random.randint(2, 100)
        k = 3
        B = (k * v + power(g, b, N)) % N
        if B != 0:
            u = hashval(hex(A + B))
            if u != 0:
                S_c = power((B - k * power(g, x, N)), (a + u * x),  N)
                K_c = hashval(hex(S_c))

                S_s = power((A * (power(v, u, N))), b, N)
                K_s = hashval(hex(S_s))

                if K_c == K_s:
                    print ("Key: ")
                    return K_c
                
print(SRP("Test message"))