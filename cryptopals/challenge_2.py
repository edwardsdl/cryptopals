import codecs

import cryptopals.common as common


def decrypt_xor_encrypted_message(key, encrypted_message):
    key = codecs.decode(key, 'hex')
    encrypted_message = codecs.decode(encrypted_message, 'hex')
    result = common.hex_from_repeated_xor(key, encrypted_message)

    return result
