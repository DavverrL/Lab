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
        s = ord(plaintext[i])
        s += 3
        if s > ord('Z') and s < ord('a') or s > ord('z'):
            s -= 26
            s = chr(s)
        else:
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
        s = ord(ciphertext[i])
        s -= 3
        if s < ord('a') and s > ord('Z') or s < ord('A'):
            s += 26
            s = chr(s)
        else:
            s = chr(s)
        b.append(s)
        i += 1
        plaintext = ''.join(b)
    return plaintext
print(encrypt_caesar("PYTHON"))
print(decrypt_caesar("SBWKRQ"))