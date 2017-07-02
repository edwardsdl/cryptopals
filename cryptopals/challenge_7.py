import codecs

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB


def decrypt_using_aes_ecb(key, message):
    key = codecs.encode(key, 'utf')
    message = codecs.decode(message, 'base64')

    algorithm = AES(key)
    mode = ECB()
    backend = default_backend()
    cipher = Cipher(algorithm, mode, backend=backend)
    cipher_context = cipher.decryptor()
    decrypted_message = cipher_context.update(message) + cipher_context.finalize()

    return decrypted_message
