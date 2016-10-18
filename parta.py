# python parta.py ciphertext.txt

import string, re
from itertools import product
from cipher import convert, decrypt

KEY_LENGTH = 6
CHARS = string.ascii_lowercase

regex = re.compile('^[\w|\s]+$')

def brute_force(ciphertext, key_length=KEY_LENGTH):
	products = product(CHARS, repeat=key_length)
	for chars in products:
		key = ''.join(chars)
		plaintext = decrypt(convert(key), ciphertext)
		if regex.search(plaintext) is not None:
			return key, plaintext

if __name__ == '__main__':
	import sys
	
	file = open(sys.argv[1], 'r')
	ciphertext = file.read()
	file.close()

	key, plaintext = brute_force(ciphertext)
	print(key)
	print(plaintext)
