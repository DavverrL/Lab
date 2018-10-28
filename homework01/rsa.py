import random
import math


def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi



def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p*q

    
    phi = (p-1)*(q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((int(char ** key)) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    p = int(input("Введите простое число: "))
    q = int(input("Введите ещё одно простое число, не равное первому: "))
    pub, priv = generate_keypair(p, q)
    print(" Открытый ключ", pub, " приватный ключ ", priv)
    message = input("Введите сообщение для шифрования: ")
    encrypted_msg = encrypt(priv, message)
    print("Зашифрованное сообщение: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Расшифрованное сообщение с открытым ключём: ", pub, " . . .")
    print("Исходное сообщение: ")
    print(decrypt(pub, encrypted_msg))
