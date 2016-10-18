import string, cipher, re
from itertools import product

KEY_LENGTH = 6
CHARS = string.ascii_lowercase

regex = re.compile('^[\w|\s]+$')

def brute_force(ciphertext, key_length=KEY_LENGTH):
	products = product(CHARS, repeat=key_length)
	for chars in products:
		key = ''.join(chars)
		plaintext = cipher.decrypt(cipher.convert(key), ciphertext)
		if regex.search(plaintext) is not None:
			return key, plaintext

if __name__ == '__main__':
	import sys
	
	file = open(sys.argv[1], 'r')
	ciphertext = file.read()
	file.close()

	print(brute_force(ciphertext))
