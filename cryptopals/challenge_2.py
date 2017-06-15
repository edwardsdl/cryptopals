import codecs


def hex_xor(first_hex_string, second_hex_string):
    first_utf_bytes = codecs.decode(first_hex_string, 'hex')
    second_utf_bytes = codecs.decode(second_hex_string, 'hex')

    zipped_utf_bytes = zip(first_utf_bytes, second_utf_bytes)

    result_utf_bytes = bytes(first_byte ^ second_byte for first_byte, second_byte in zipped_utf_bytes)
    result_hex_bytes = codecs.encode(result_utf_bytes, 'hex')
    result_utf_string = codecs.decode(result_hex_bytes, 'utf')

    return result_utf_string
