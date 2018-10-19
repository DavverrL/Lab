ciphertext = list(input("Введите зашифрованное сообщение: "))
key = list(input("Введите ключевое слово: "))
b = []
a = []
for i in range(len(key)):
    s = ord(key[i])
    if (s >= 65) and (s < 97):
        s = s - 65
    elif (s >= 97) and (s < 1040):
        s = s - 97
    elif (s >= 1040) and (s < 1072):
        s = s - 1040
    else:
        s = s - 1072
    a.append(s)
for i in range(len(ciphertext)):
    s = ord(ciphertext[i])
    s = s + a[i]
    s = chr(s)
    b.append(s)
    i += 1
laintext = ''.join(b)
print("Расшифрованное сообщение: ", laintext)
