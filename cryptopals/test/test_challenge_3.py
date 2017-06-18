import cryptopals.challenge_3 as challenge
import unittest


class Tests(unittest.TestCase):
    def test(self):
        message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        expected_output = "Cooking MC's like a pound of bacon"
        actual_output = challenge.decrypt_xor_cipher(message)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
