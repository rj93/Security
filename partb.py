# python partb.py ciphertext.txt 10 15 100GBP 999EUR

from parta import convert, read_file

def convert_hex(text):
	""" Converts a string of hex values to a list of integers """
	return [int(text[n:n+2], 16) for n in range(len(text)) if n % 2 == 0]

def xor(l1, l2, l3):
	""" XORs three lists of integers and returns the resulting list """
	return [a ^ b ^ c for a, b, c in zip(l1, l2, l3)]

def replace(ciphertext, start, end, original, replacement):
	""" Replaces the original plaintext with the replacement plaintext
		in the given ciphertext at between the start and end values.
		Returns the new ciphertext. """
	c = convert_hex(ciphertext[start:end])
	p = convert(original)
	r = convert(replacement)

	replacementHex = ''.join(["%02X" % c for c in xor(p, c, r)]) # convert ints list to string of hex values
	return ciphertext[:start] + replacementHex + ciphertext[end:]

if __name__ == '__main__':
	import sys
	
	ciphertext = read_file(sys.argv[1])
	start = (int(sys.argv[2]) - 1) * 2 # values have to be adjusted for hex values
	end = int(sys.argv[3]) * 2

	newCiphertext = replace(ciphertext, start, end, sys.argv[4], sys.argv[5])
	print(newCiphertext)