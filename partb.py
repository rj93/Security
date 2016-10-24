# python partb.py ciphertext.txt 10 15 100GBP 999EUR

from cipher import convert, encrypt

def convert_hex(text):
	return [int(text[n:n+2], 16) for n in range(len(text)) if n % 2 == 0]

def xor(l1, l2, l3):
	return [a ^ b ^ c for a, b, c in zip(l1, l2, l3)]

if __name__ == '__main__':
	import sys
	
	with open(sys.argv[1], 'r') as f:
		ciphertext = f.read()

	start = (int(sys.argv[2]) - 1) * 2
	end = int(sys.argv[3]) * 2
	original = sys.argv[4]
	replacemnet = sys.argv[5]

	c = convert_hex(ciphertext[start:end])
	p = convert(original)
	r = convert(replacemnet)

	replacement_cipher = ''.join(["%02X" % c for c in xor(p, c, r)])
	new_ciphertext = ciphertext[:start] + replacement_cipher + ciphertext[end:]