def encrypt_caesar(plaintext):
	b = []
	for i in range(len(plaintext)):
		s = ord(plaintext[i])
		s -= 3
		s = chr(s)
	b.append(s)
	i += 1
	plaintext = ''.join(b)
	return ciphertext

def decrypt_caesar(ciphertext):
	b = []
	for i in range(len(ciphertext)):
		s = ord(ciphertext[i]) 
		s += 3
		s = chr(s)
	b.append(s)
	i += 1
	ciphertext = ''.join(b)
	return plaintext
print(encrypt_caesar("SBWKRQ",5))
print(decrypt_caesar("",5))

	
