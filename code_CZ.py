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
