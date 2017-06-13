import codecs


def hex_to_base64(hex_string):
    hex_bytes = codecs.decode(hex_string, 'hex')
    base64_bytes = codecs.encode(hex_bytes, 'base64')
    base64_string = base64_bytes.decode().strip()

    return base64_string
