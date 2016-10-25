# python partb.py ciphertext.txt 10 15 100GBP 999EUR

from cipher import convert, encrypt

def read_file(file):
	with open(file, 'r') as f:
		return f.read()

def convert_hex(text):
	return [int(text[n:n+2], 16) for n in range(len(text)) if n % 2 == 0]

def xor(l1, l2, l3):
	return [a ^ b ^ c for a, b, c in zip(l1, l2, l3)]

def replace(ciphertext, start, end, original, replacement):
	c = convert_hex(ciphertext[start:end])
	p = convert(original)
	r = convert(replacement)

	replacementHex = ''.join(["%02X" % c for c in xor(p, c, r)])
	return ciphertext[:start] + replacementHex + ciphertext[end:]

if __name__ == '__main__':
	import sys
	
	ciphertext = read_file(sys.argv[1])
	start = (int(sys.argv[2]) - 1) * 2
	end = int(sys.argv[3]) * 2

	newCiphertext = replace(ciphertext, start, end, sys.argv[4], sys.argv[5])
	print(newCiphertext)