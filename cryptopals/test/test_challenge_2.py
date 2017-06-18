import unittest

import cryptopals.challenge_2 as challenge


class Tests(unittest.TestCase):
    def test(self):
        key = '686974207468652062756c6c277320657965'
        encrypted_message = '1c0111001f010100061a024b53535009181c'
        expected_output = '746865206b696420646f6e277420706c6179'
        actual_output = challenge.decrypt_xor_encrypted_message(key, encrypted_message)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
