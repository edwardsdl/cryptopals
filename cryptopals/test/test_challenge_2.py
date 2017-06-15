import cryptopals.challenge_2 as challenge
import unittest


class Tests(unittest.TestCase):
    def test(self):
        first_hex_string = '1c0111001f010100061a024b53535009181c'
        second_hex_string = '686974207468652062756c6c277320657965'
        expected_output = '746865206b696420646f6e277420706c6179'
        actual_output = challenge.hex_xor(first_hex_string, second_hex_string)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
