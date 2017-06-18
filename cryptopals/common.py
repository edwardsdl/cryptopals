import codecs
import pkg_resources


def hex_to_base64(hex_string):
    utf_bytes = codecs.decode(hex_string, 'hex')
    base64_bytes = codecs.encode(utf_bytes, 'base64')
    base64_string = codecs.decode(base64_bytes, 'utf').strip()

    return base64_string


def get_word_list():
    word_list = pkg_resources.resource_string('cryptopals.resources', 'word_list.txt')
    word_list = codecs.decode(word_list, 'utf').split('\n')

    return word_list


def score(input_string):
    words = input_string.lower().split(' ')
    word_list = get_word_list()

    return sum([1 if word in word_list else 0 for word in words])


def xor_using_character(character_byte, input_bytes):
    return bytes([character_byte ^ input_byte for input_byte in input_bytes])
