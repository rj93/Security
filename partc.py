# python partc.py ciphertextfileA ciphertextfileB plaintextfileA

from parta import convert, read_file
from partb import xor, convert_hex

def recover_plaintext(ciphertext1, ciphertext2, plaintext1):
	""" recovers the plaintext of ciphertext2 if both ciphertexts 
		used the same key during encryption.
		Returns the recovered plaintext. """

	c1 = convert_hex(ciphertext1)
	c2 = convert_hex(ciphertext2)
	p1 = convert(plaintext1)
	return ''.join([chr(c) for c in xor(c1, c2, p1)]) # XORs the lists, and converts them to a string of characters

if __name__ == '__main__':
	import sys

	ciphertext1 = read_file(sys.argv[1])
	ciphertext2 = read_file(sys.argv[2])
	plaintext1 = read_file(sys.argv[3])
	plaintext2 = recover_plaintext(ciphertext1, ciphertext2, plaintext1)
	print(plaintext2)