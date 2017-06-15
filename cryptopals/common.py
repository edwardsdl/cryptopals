import codecs


def hex_to_base64(hex_string):
    utf_bytes = codecs.decode(hex_string, 'hex')
    base64_bytes = codecs.encode(utf_bytes, 'base64')
    base64_string = codecs.decode(base64_bytes, 'utf').strip()

    return base64_string
