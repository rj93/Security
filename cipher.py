#python cipher.py e key.txt plaintext.txt 
#python cipher.py d key.txt ciphertext.txt 

def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K

def streamcipher(key):
    S = KSA(key)
    return PRGA(S)

def convert(s):
    return [ord(c) for c in s]

def encrypt(key, plaintext):
    keystream = streamcipher(key)
    return ''.join(["%02X" % (ord(c) ^ next(keystream)) for c in plaintext])

def decrypt(key, ciphertext):
    keystream = streamcipher(key)
    return ''.join([chr(int(ciphertext[n:n+2], 16) ^ next(keystream)) for n in range(len(ciphertext)) if n % 2 == 0])



if __name__ == '__main__':
    import sys
    file = open(sys.argv[2], 'r')
    key = file.read()
    file.close()

    file = open(sys.argv[3], 'r')
    if sys.argv[1] == 'e':  #encryption
        plaintext = file.read()
    else:                   #decryption
        ciphertext = file.read()
    file.close()
    
    key = convert(key)
    keystream = streamcipher(key)

    if sys.argv[1] == 'e':  #encryption
        print(encrypt(key, plaintext))
    else:                   #decryption
        print(decrypt(key, ciphertext))
