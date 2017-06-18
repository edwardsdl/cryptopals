import codecs

import cryptopals.common as common


def decrypt_xor_cipher(key, message):
    key = codecs.decode(key, 'hex')
    message = codecs.decode(message, 'hex')
    result = common.hex_from_repeated_xor(key, message)

    return result
