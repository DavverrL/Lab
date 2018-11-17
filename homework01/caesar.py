def encrypt_caesar(plaintext: str) -> str:
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
    if plaintext == (""):
        ciphertext = ''
    else:
        b = []
        for i in range(len(plaintext)):
            s = ord(plaintext[i])
            if 46 <= s <= 57:
                st = chr(s)
            else:
                s += 3
                if s > ord('Z') and s < ord('a') or s > ord('z'):
                    s -= 26
                    st = chr(s)
                else:
                    st = chr(s)
            b.append(st)
            i += 1
        ciphertext = ''.join(b)

    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
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
    if ciphertext == (""):
        plaintext = ''
    else:
        b = []
        for i in range(len(ciphertext)):
            s = ord(ciphertext[i])
            if 46 <= s <= 57:
                st = chr(s)
            else:
                s -= 3
                if s < ord('a') and s > ord('Z') or s < ord('A'):
                    s += 26
                    st = chr(s)
                else:
                    st = chr(s)
            b.append(st)
            i += 1
            plaintext = ''.join(b)
    return plaintext


print(encrypt_caesar("PYTHON"))
print(decrypt_caesar("SBWKRQ"))
