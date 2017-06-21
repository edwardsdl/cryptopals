import cryptopals.common as common


def test_base64_from_hex():
    expected_output = 'SGVsbG8sIHdvcmxkIQ=='
    actual_output = common.base64_from_hex('48656c6c6f2c20776f726c6421')

    assert expected_output == actual_output


def test_word_list_contains_1000_entries():
    word_list = common.get_word_list()
    expected_output = 1000
    actual_output = len(word_list)

    assert expected_output == actual_output


def test_score_message():
    rows = [
        ('Now is the time for all good men to come to the aid of their country', 13),
        ('The quick brown fox jumps over the lazy dog', 4),
        ('ETAOIN SHRDLU', 0),
    ]

    for row in rows:
        expected_output = row[1]
        actual_output = common.score_message(row[0])

        assert expected_output == actual_output
