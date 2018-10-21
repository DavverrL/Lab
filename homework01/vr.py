def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    t = len(plaintext)//len(keyword)
    keyword = keyword * (t)
    t1 = len(plaintext) % len(keyword)
    for i in range(t1):
        keyword += keyword[i]
        i += 1
    b = []
    a = []
    for i in range(len(keyword)):
        s = ord(keyword[i])
        if (s >= 65) and (s < 90):
            s = s - 65
        a.append(s)
    for i in range(len(plaintext)):
        s = ord(plaintext[i])
        if(s + a[i])>90:
            p = (s + a[i]) - 90
            s = 64 + p
            s = chr(s)
        else:
            s = s + a[i]
            s = chr(s)
        b.append(s)
        i += 1
    ciphertext = ''.join(b)
    return ciphertext

def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    t = len(ciphertext)//len(keyword)
    keyword = keyword * (t)
    t1 = len(ciphertext) % len(keyword)
    for i in range(t1):
        keyword += keyword[i]
        i += 1
    b = []
    a = []
    for i in range(len(keyword)):
        s = ord(keyword[i])
        if (s >= 65) and (s < 90):
            s = s - 65
        a.append(s)
    for i in range(len(ciphertext)):
        s = ord(ciphertext[i])
        if(s - a[i])<65:
            p = s - 65
            s = 91 + p - a[i]
            s = chr(s)
        else:
            s = s - a[i]
            s = chr(s)
        b.append(s)
        i += 1
    plaintext = ''.join(b)
    return plaintext
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))