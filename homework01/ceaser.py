def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    b = []
    for i in range(len(plaintext)):
        if (plaintext[i] == 'X'):
            s = 'A'
        elif(plaintext[i] == 'Y'):
            s = 'B'
        elif(plaintext[i] == 'Z'):
            s = 'C'
        else:
            s = ord(plaintext[i])
            s += 3
            s = chr(s)
        b.append(s)
        i += 1
        ciphertext = ''.join(b)

    return ciphertext
def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    b = []
    for i in range(len(ciphertext)):
        if (ciphertext[i] == 'A'):
            s = 'X'
        elif(ciphertext[i] == 'B'):
            s = 'Y'
        elif(ciphertext[i] == 'C'):
            s = 'Z'
        else:
            s = ord(ciphertext[i])
            s -= 3
            s = chr(s)
        b.append(s)
        i += 1
        plaintext = ''.join(b)
    return plaintext
print(encrypt_caesar("PYTHON"))
print(decrypt_caesar("SBWKRQ"))