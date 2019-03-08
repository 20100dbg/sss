import rsa
import os
from Crypto.Cipher import AES

#pip install rsa
#pip install cryptography



def pad(str):
    y = len(str)
    
    while not y % 16 == 0:
        y = y +1
    
    return str.ljust(y, " ")




(pubkey, privkey) = rsa.newkeys(512)


message = 'hello Bob!'.encode('utf8')

crypto = rsa.encrypt(message, pubkey)

message = rsa.decrypt(crypto, privkey)

print(message.decode('utf8'))
print(pubkey)


aes_key = os.urandom(32)
aes_iv = os.urandom(16)

aes = AES.new(aes_key, AES.MODE_CBC, aes_iv)
cipher_text = aes.encrypt(pad("A really secret message. Not for prying eyes."))

aes = AES.new(aes_key, AES.MODE_CBC, aes_iv)
plain_text = aes.decrypt(cipher_text)

print(plain_text)

