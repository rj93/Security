# python parta.py ciphertext.txt

import string, re, time, sys
from itertools import product
from cipher import streamcipher
from multiprocessing import Pool, cpu_count

KEY_LENGTH = 4
PRCOESSES = max(cpu_count() - 1, 1)
CHUNKSIZE = 100 # approximately how many products to submit to each of the processes at one time
CHARS = string.ascii_lowercase

regex = re.compile('^[\w\s.,!?:;_\'\"\(\)\[\]\{\}\-]+$') # matches a-z, A-Z, 0-9, any whitespace character, and .,!?:;'"()[]{}-

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

def attempt_decrypt(chars):
	""" performs a decrypt, and checks to 
	see if the plaintext is accepted by the regex. 
	if accepted returns dictionary containing 
	key and plaintext, otherwise returns None """

	try:
		key = ''.join(chars)
		plaintext = decrypt(convert(key), ciphertext)
		if regex.search(plaintext) is not None:
			return {'key' : key, 'plaintext' : plaintext}
	except KeyboardInterrupt:
		pool.terminate() 

def brute_force(key_length=KEY_LENGTH, processes=PRCOESSES, chunksize=CHUNKSIZE):
	""" brute forces the key of the ciphertext.
		Returns a dictionary with the key, plaintext,
		key_attempts, total_time, and keys_per_second """

	products = product(CHARS, repeat=key_length)
	pool = Pool(processes=processes)
	key_attempts = 0

	try:
		start = time.time()
		for result in pool.imap(attempt_decrypt, products, chunksize): 
			key_attempts = key_attempts + 1
			if result: 
				break
		total_time = round(time.time() - start, 2)

		if result:
			keys_per_sec = round(key_attempts / total_time)
			result['key_attempts'] = key_attempts
			result['total_time'] = total_time
			result['keys_per_sec'] = keys_per_sec
			return result
	except KeyboardInterrupt:
		pool.terminate() 
		sys.exit()

if __name__ == '__main__':
	
	ciphertext = read_file(sys.argv[1])
	result = brute_force()
	if result:
		print(result['key'])
		print(result['plaintext'])
		print('time = {}s, key attempts = {}, keys/second = {}'.format(result['total_time'], result['key_attempts'], result['keys_per_sec']))
	else:
		print("Unable to find key")
