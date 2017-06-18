import codecs
import string

import cryptopals.common as common


def decrypt_xor_encrypted_message(encrypted_message):
    characters = [[ord(character)] for character in string.ascii_letters + string.digits]
    encrypted_message = codecs.decode(encrypted_message, 'hex')

    highest_score = 0
    highest_scoring_message = ''
    for character in characters:
        message = common.utf_from_repeated_xor(character, encrypted_message)
        score = common.score_message(message)

        if score > highest_score:
            highest_score = score
            highest_scoring_message = message

    return highest_scoring_message
