import codecs
import functools
import itertools

import math
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


def score_message_using_word_list(message):
    if not message.strip().isprintable():
        return 0

    words = message.lower().split(' ')
    word_list = get_word_list()
    score = sum(1 if word in word_list else 0 for word in words)

    return score


def score_message_using_frequency_analysis(message):
    character_distribution = {
        ' ': {'expected_frequency': 0.1217, 'count': 0},
        'a': {'expected_frequency': 0.0609, 'count': 0},
        'b': {'expected_frequency': 0.0105, 'count': 0},
        'c': {'expected_frequency': 0.0284, 'count': 0},
        'd': {'expected_frequency': 0.0292, 'count': 0},
        'e': {'expected_frequency': 0.1136, 'count': 0},
        'f': {'expected_frequency': 0.0179, 'count': 0},
        'g': {'expected_frequency': 0.0138, 'count': 0},
        'h': {'expected_frequency': 0.0341, 'count': 0},
        'i': {'expected_frequency': 0.0544, 'count': 0},
        'j': {'expected_frequency': 0.0024, 'count': 0},
        'k': {'expected_frequency': 0.0041, 'count': 0},
        'l': {'expected_frequency': 0.0292, 'count': 0},
        'm': {'expected_frequency': 0.0276, 'count': 0},
        'n': {'expected_frequency': 0.0544, 'count': 0},
        'o': {'expected_frequency': 0.0600, 'count': 0},
        'p': {'expected_frequency': 0.0195, 'count': 0},
        'q': {'expected_frequency': 0.0024, 'count': 0},
        'r': {'expected_frequency': 0.0495, 'count': 0},
        's': {'expected_frequency': 0.0568, 'count': 0},
        't': {'expected_frequency': 0.0803, 'count': 0},
        'u': {'expected_frequency': 0.0243, 'count': 0},
        'v': {'expected_frequency': 0.0097, 'count': 0},
        'w': {'expected_frequency': 0.0138, 'count': 0},
        'x': {'expected_frequency': 0.0024, 'count': 0},
        'y': {'expected_frequency': 0.0130, 'count': 0},
        'z': {'expected_frequency': 0.0003, 'count': 0},
        'other': {'expected_frequency': 0.0657, 'count': 0}
    }

    for character in message.lower():
        if character in character_distribution:
            character_distribution[character]['count'] += 1
        else:
            character_distribution['other']['count'] += 1

    message_length = len(message)
    result = 0

    for value in character_distribution.values():
        actual_count = value['count']
        expected_count = message_length * value['expected_frequency']
        result += (math.pow(actual_count - expected_count, 2) / expected_count)

    return result


def utf_from_repeated_xor(key, message):
    result = perform_repeated_xor(key, message)
    result = codecs.decode(result, 'utf', errors='ignore')

    return result
