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
ciphertext = list(input("Введите зашифрованное сообщение: "))
b = []
for i in range(len(ciphertext)):
    s = ord(ciphertext[i])
    s -= 3
    s = chr(s)
    b.append(s)
    i += 1
laintext = ''.join(b)
print("Расшифрованное сообщение: ", laintext)
    
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
    # PUT YOUR CODE HERE
    return plaintext

print(encrypt_caesar("PYTHON"))
print(decrypt_caesar("SBWKRQ"))
