import codecs
import functools
import itertools

import pkg_resources


def base64_from_hex(message):
    message = codecs.decode(message, 'hex')
    message = codecs.encode(message, 'base64')
    message = codecs.decode(message, 'utf').strip()

    return message


def compute_hamming_distance(first_bytes, second_bytes):
    zipped_bytes = zip(first_bytes, second_bytes)
    hamming_distance_per_byte = [bin(first_byte ^ second_byte).count('1') for first_byte, second_byte in zipped_bytes]
    hamming_distance = sum(hamming_distance_per_byte)

    return hamming_distance


@functools.lru_cache()
def get_word_list():
    word_list = pkg_resources.resource_string('cryptopals.resources', 'word_list.txt')
    word_list = codecs.decode(word_list, 'utf').split('\n')

    return word_list


def hex_from_repeated_xor(key, message):
    result = perform_repeated_xor(key, message)
    result = codecs.encode(result, 'hex')
    result = codecs.decode(result, 'utf')

    return result


def perform_repeated_xor(key, message):
    zipped_bytes = zip(itertools.cycle(key), message)
    result = bytes(first_byte ^ second_byte for first_byte, second_byte in zipped_bytes)

    return result


def score_message(message):
    if not message.strip().isprintable():
        return 0

    words = message.lower().split(' ')
    word_list = get_word_list()
    score = sum(1 if word in word_list else 0 for word in words)

    return score


def utf_from_repeated_xor(key, message):
    result = perform_repeated_xor(key, message)
    result = codecs.decode(result, 'utf', errors='ignore')

    return result
