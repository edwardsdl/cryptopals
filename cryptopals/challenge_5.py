import codecs

import cryptopals.common as common


def xor_with_repeating_key(key, message):
    key = codecs.encode(key, 'utf')
    message = codecs.encode(message, 'utf')
    encrypted_message = common.perform_repeated_xor(key, message)
    encrypted_message = codecs.encode(encrypted_message, 'hex')
    encrypted_message = codecs.decode(encrypted_message, 'utf')

    return encrypted_message
