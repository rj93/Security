# python parta.py ciphertext.txt

import string, re, time
from itertools import product
from cipher import convert, decrypt


KEY_LENGTH = 6
CHARS = string.ascii_lowercase

regex = re.compile('^[\w\s.]+$')

def brute_force(ciphertext, key_length=KEY_LENGTH):
	products = product(CHARS, repeat=key_length)
	count = 0
	for chars in products:
		count = count + 1
		key = ''.join(chars)
		plaintext = decrypt(convert(key), ciphertext)
		if regex.search(plaintext) is not None:
			return key, plaintext, count


if __name__ == '__main__':
	import sys
	
	file = open(sys.argv[1], 'r')
	ciphertext = file.read()
	file.close()

	start = time.time()
	key, plaintext, keys = brute_force(ciphertext)
	totalTime = round(time.time() - start, 2)
	keysPerSec = round(keys / time)

	print(key)
	print(plaintext)
	print("time = {}s, keys = {}, keys/second = {}".format(totalTime, keys, keysPerSec))