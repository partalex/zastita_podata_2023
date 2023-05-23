from base64 import b64encode, b64decode
import rsa
from Crypto.Hash import SHA

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5


def importKey(externKey):
    return RSA.importKey(externKey)


def getpublickey(priv_key):
    return priv_key.publickey()


def encrypt(message, pub_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)


def decrypt(ciphertext, priv_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


def sign(message, priv_key):
    signer = PKCS1_v1_5.new(priv_key)
    digest = SHA.new()
    digest.update(message)
    return signer.sign(digest)


def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    if (hash == "SHA-1"):
        digest = SHA.new()
    digest.update(message)
    return signer.verify(digest, signature)


def keyToPem(key):
    return key.save_pkcs1().decode('utf8')


def pemToPUKey(pem):
    return rsa.PublicKey.load_pkcs1(pem.encode('utf8'))


def pemToPRKey(pem):
    return rsa.PrivateKey.load_pkcs1(pem.encode('utf8'))


keySize = 512
publicKey, privateKey = rsa.newkeys(keySize)

# stari kod
plaintext = b"Hello Tony, I am Jarvis!"
msg2 = b"Hello Toni, I am Jarvis!"
cyphertext = b64encode(rsa.encrypt(plaintext, publicKey))
originalMessage = rsa.decrypt(b64decode(cyphertext), privateKey)
signature = b64encode(rsa.sign(plaintext, privateKey, "SHA-1"))
verify = rsa.verify(plaintext, b64decode(signature), publicKey)

PUPem = publicKey.save_pkcs1().decode()
# print(PUPem)
PUReloaded = rsa.PublicKey.load_pkcs1(PUPem.encode())

if PUPem == PUReloaded:
    print("radi")

PRPem = privateKey.save_pkcs1().decode()

with open("./privateKey.pem", 'a') as the_file:
    print(PRPem, file=the_file)

print("Encrypted: " + cyphertext.decode())
print("Decrypted: '%s'" % originalMessage)
print("Signature: " + signature)
print("Verify: %s" % verify)
rsa.verify(msg2, b64decode(signature), publicKey)
