import crypto
import sys
sys.modules['Crypto'] = crypto

from Crypto.Cipher import AES

key = b'\x1a\xa0\xd0\x07\xec\x10*\xfb\xfe3\x1c\xd4(\xc5\xea%'

file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)