# python partc.py ciphertextfileA ciphertextfileB plaintextfileA

from cipher import convert
from partb import xor, convert_hex

def read_file(file):
	with open(file, 'r') as f:
		return f.read()

def recover_plaintext(ciphertext1, ciphertext2, plaintext1):
	c1 = convert_hex(ciphertext1)
	c2 = convert_hex(ciphertext2)
	p1 = convert(plaintext1)
	return ''.join([chr(c) for c in xor(c1, c2, p1)])

if __name__ == '__main__':
	import sys

	plaintext = recover_plaintext(read_file(sys.argv[1]), read_file(sys.argv[2]), read_file(sys.argv[3]))
	print(plaintext)