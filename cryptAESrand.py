import crypto
import sys
sys.modules['Crypto'] = crypto

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'mike'
key = get_random_bytes(16)
print(key)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]