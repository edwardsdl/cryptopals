import cryptopals.challenge_1 as challenge
import unittest


class Tests(unittest.TestCase):
    def test(self):
        hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        actual_output = challenge.hex_to_base64(hex_string)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
