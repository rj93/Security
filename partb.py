#python partb.py ciphertext.txt 10 15 100GBP 999EUR

from parta import brute_force
from cipher import convert, encrypt

if __name__ == '__main__':
	import sys
	
	file = open(sys.argv[1], 'r')
	ciphertext = file.read()
	file.close()

	start = int(sys.argv[2])
	end = int(sys.argv[3])
	orginial = sys.argv[4]
	replacemnet = sys.argv[5]
	key, plaintext = brute_force(ciphertext)
	if (plaintext[start-1:end] == orginial):
		plaintext = plaintext.replace(orginial, replacemnet)
		print(encrypt(convert(key), plaintext))
	else:
		print("Could not find '{}' in '{}' at bytes {} - {}".format(orginial, plaintext, start, end))