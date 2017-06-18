import codecs

import cryptopals.common as common


def xor_with_repeating_key(key, message):
    key = codecs.encode(key, 'utf')
    message = codecs.encode(message, 'utf')
    encrypted_message = common.hex_from_repeated_xor(key, message)

    return encrypted_message
