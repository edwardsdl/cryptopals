import codecs
import string

import cryptopals.common as common


def find_xor_encrypted_message(encrypted_messages):
    characters = [[ord(character)] for character in string.ascii_letters + string.digits]
    encrypted_messages = [codecs.decode(encrypted_message, 'hex') for encrypted_message in encrypted_messages]

    highest_score = 0
    highest_scoring_message = ''
    for character in characters:
        for encrypted_message in encrypted_messages:
            message = common.utf_from_repeated_xor(character, encrypted_message).strip()
            score = common.score_message_using_word_list(message)

            if score > highest_score:
                highest_score = score
                highest_scoring_message = message

    return highest_scoring_message
