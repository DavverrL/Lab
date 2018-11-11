def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    t = len(plaintext) // len(keyword)
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
        elif s >= 97 and s <= 122:
            s = s - 97
        a.append(s)
    for i in range(len(plaintext)):
        s = ord(plaintext[i])
        if(ord('a') <= s <= ord('z')):
            if((s + a[i]) > ord('a')) and ((s + a[i]) > ord('z')):
                p = (s + a[i]) - 122
                s = ord('a') + p
        elif(s + a[i]) > 90:
            p = (s + a[i]) - 90
            s = 64 + p
        else:
            s = s + a[i]
        s = chr(s)
        b.append(s)
        i += 1
    ciphertext = ''.join(b)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    t = len(ciphertext) // len(keyword)
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
        elif s >= 97 and s <= 122:
            s = s - 97
        a.append(s)
    for i in range(len(ciphertext)):
        s = ord(ciphertext[i])
        if(ord('a') <= s <= ord('z')):
            if((s + a[i]) < ord('a')) and ((s + a[i]) < ord('z')):
                p = (s + a[i]) - 122
                s = ord('a') + p - a[i] + 1
        if(s - a[i]) < 65:
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


print(encrypt_vigenere("PYTHON", "A"))
print(decrypt_vigenere("PYTHON", "A"))
