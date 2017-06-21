import pytest

import cryptopals.common as common


def test_base64_from_hex():
    assert 'SGVsbG8sIHdvcmxkIQ==' == common.base64_from_hex('48656c6c6f2c20776f726c6421')


@pytest.mark.parametrize('first_bytes, second_bytes, expected_output', [
    (b'Hello,', b'World!', 17),
    (b'foo', b'bar', 8),
    (b'baz', b'qux', 6)
])
def test_compute_hamming_distance(first_bytes, second_bytes, expected_output):
    assert common.compute_hamming_distance(first_bytes, second_bytes) == expected_output


@pytest.mark.parametrize('message, expected_output', [
    ('Now is the time for all good men to come to the aid of their country', 13),
    ('The quick brown fox jumps over the lazy dog', 4),
    ('ETAOIN SHRDLU', 0)
])
def test_score_message(message, expected_output):
    assert common.score_message(message) == expected_output


def test_word_list_contains_1000_entries():
    assert 1000 == len(common.get_word_list())
