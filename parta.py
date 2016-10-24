# python parta.py ciphertext.txt

import string, re, time
from itertools import product
from cipher import convert, decrypt

KEY_LENGTH = 6
CHARS = string.ascii_lowercase

regex = re.compile('^[\w\s.]+$')

def brute_force(ciphertext, key_length=KEY_LENGTH, count=False):
	products = product(CHARS, repeat=key_length)
	attempts = 0
	for chars in products:
		attempts = attempts + 1
		key = ''.join(chars)
		plaintext = decrypt(convert(key), ciphertext)
		if regex.search(plaintext) is not None:
			if not count:
				return key, plaintext
			else:
				return key, plaintext, attempts

if __name__ == '__main__':
	import sys
	
	with open(sys.argv[1], 'r') as f:
		ciphertext = f.read()

	start = time.time()
	key, plaintext, keys = brute_force(ciphertext, count=True)
	totalTime = round(time.time() - start, 2)
	keysPerSec = round(keys / totalTime)

	print(key)
	print(plaintext)
	print('time = {}s, keys = {}, keys/second = {}'.format(totalTime, keys, keysPerSec))