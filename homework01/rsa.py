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
    x = 0
    for i in range(0, n):
        i += 1
        if (n % i == 0):
            x += 1
    return True if (x == 2) else False


def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while (a % b != 0):
        c = a % b
        a = b
        b = c
    return(b)


def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    d = 0
    i = 0
    while (d * e % phi != 1):
        d = (phi * i + 1) // e
        i += 1
    return(d)


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
    print("RSA Encrypter/ Decrypter")
    p = int(input("Введите простое число: "))
    q = int(input("Введите ещё одно простое чило, отличное от первого: "))
    print("Введите ключ. . .")
    public, private = generate_keypair(p, q)
    print("Ваш открытый ключ ", public, " ваш частный ключ ", private)
    message = input("Введите сообщение для шифрования с помощью частного ключа: ")
    encrypted_msg = encrypt(private, message)
    print("Зашифрованное сообщение: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Расшифровка сообщения с помощью открытого ключа ", public, " . . .")
    print("Сообщение:")
    print(decrypt(public, encrypted_msg))
