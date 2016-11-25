# python parta.py ciphertext.txt

import string, re, time
from itertools import product
from cipher import streamcipher

KEY_LENGTH = 4
CHARS = string.ascii_lowercase

regex = re.compile('^[\w\s.,!?:;_\'\"\(\)\[\]\{\}\-]+$') # matches a-z, A-Z, 0-9, and .,!?:;'"()[]{}-

def read_file(file):
	""" returns the contents of a file """
	with open(file, 'r') as f:
		return f.read()

def convert(s):
	""" coverts the string to a list of integers """
	return [ord(c) for c in s]

def decrypt(key, ciphertext):
	""" decrypts the ciphertext with  using the key. Returns the plaintext """
	keystream = streamcipher(key)
	return ''.join([chr(int(ciphertext[n:n+2], 16) ^ next(keystream)) for n in range(len(ciphertext)) if n % 2 == 0]) 

def brute_force(ciphertext, key_length=KEY_LENGTH, count=False):
	""" brute forces the key of the ciphertext.
		Returns the key, the plaintext, 
		and dependant on the count flag how many attempts it took. """
		
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
	
	ciphertext = read_file(sys.argv[1])

	start = time.time()
	key, plaintext, keys = brute_force(ciphertext, count=True)
	totalTime = round(time.time() - start, 2)
	keysPerSec = round(keys / totalTime)

	print(key)
	print(plaintext)
	print('time = {}s, keys = {}, keys/second = {}'.format(totalTime, keys, keysPerSec))