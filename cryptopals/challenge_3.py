import codecs
import string

import cryptopals.common as common


def decrypt_xor_cipher(encrypted_message):
    characters = [[ord(character)] for character in string.ascii_letters + string.digits]
    encrypted_message = codecs.decode(encrypted_message, 'hex')
    messages = [common.utf_from_repeated_xor(character, encrypted_message) for character in characters]
    scores = [common.score_message(message) for message in messages]
    results = list(zip(scores, messages))

    return max(results, key=lambda result: result[0])[1]
