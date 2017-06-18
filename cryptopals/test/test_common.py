import cryptopals.common as common
import unittest


class Tests(unittest.TestCase):
    def test_base64_from_hex(self):
        expected_output = 'SGVsbG8sIHdvcmxkIQ=='
        actual_output = common.base64_from_hex('48656c6c6f2c20776f726c6421')

        self.assertEqual(expected_output, actual_output)

    def test_get_word_list(self):
        word_list = common.get_word_list()
        expected_output = 10000
        actual_output = len(word_list)

        self.assertEqual(expected_output, actual_output)

    def test_score_message(self):
        rows = [
            ('Now is the time for all good men to come to the aid of their country', 16),
            ('The quick brown fox jumps over the lazy dog', 8),
            ('ETAOIN SHRDLU', 0),
        ]

        for row in rows:
            expected_output = row[1]
            actual_output = common.score_message(row[0])

            self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
