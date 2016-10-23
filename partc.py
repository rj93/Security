# python partc.py ciphertextfileA ciphertextfileB plaintextfileA

from cipher import convert

def read_file(file):
	with open(file, 'r') as f:
		return f.read()

def convert_hex(text):
	return [int(text[n:n+2], 16) for n in range(len(text)) if n % 2 == 0]

def xor(l1, l2):
	return [a ^ b for a,b in zip(l1,l2)]

if __name__ == '__main__':
	import sys

	ciphertext1 = read_file(sys.argv[1])
	ciphertext2 = read_file(sys.argv[2])
	plaintext1 = read_file(sys.argv[3])

	c1 = convert_hex(ciphertext1)
	c2 = convert_hex(ciphertext2)
	p1 = convert(plaintext1)

	print(''.join([chr(c) for c in xor(xor(c1, c2), p1)]))