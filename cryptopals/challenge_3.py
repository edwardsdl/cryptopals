import codecs
import string

import cryptopals.common as common


def decrypt_xor_cypher(hex_string):
    utf_bytes = codecs.decode(hex_string, 'hex')
    character_bytes = [ord(character) for character in string.ascii_letters + string.digits]

    results = []
    for character_byte in character_bytes:
        result_bytes = common.xor_using_character(character_byte, utf_bytes)
        result_string = codecs.decode(result_bytes, 'utf')
        result_score = common.score(result_string)

        results.append((result_score, result_string))

    return max(results, key=lambda result: result[0])[1]
